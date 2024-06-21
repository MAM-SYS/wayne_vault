"""
If you follow the rules below, your models will be loaded automatically:
1- Your model must inherit from `wayne_vault.db.base.Base` class.
2- Your model can be loaded from `root_dir/any_dir/model.py.
    Description:
        - root_dir => means root of project
        - any_dir => any directory inside root_dir
    Examples:
        Assume you have a file `user/models.py`:
        ```
        >>> from wayne_vault.db.base import Base
        >>> class User(Base):
        >>>    state = Column(Enum(DealState, name="deal_state"), nullable=False, default=DealState.Init)
        ```
        This User model will be automatically loaded in alembic.
"""
import importlib
import importlib.util
import os
import sys
from logging.config import fileConfig

from alembic import context
from sqlalchemy import create_engine
from sqlalchemy import pool
from sqlalchemy.orm import sessionmaker, scoped_session

from wayne_vault.core.config import settings
from wayne_vault.db.base import Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.

config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support


DB_URI = f"mysql://" \
         f"{settings.DB_USER}:{settings.DB_PASSWORD.get_secret_value()}" \
         f"@{settings.DB_HOST}:{settings.DB_PORT}" \
         f"/{settings.DB_NAME}"
engine = create_engine(DB_URI, pool_recycle=3600)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


def add_models(path):
    module_name = f"{path}.models"
    if module_name in sys.modules:
        return
    spec = importlib.util.spec_from_file_location(module_name, str(settings.BASE_DIR / path))
    print(spec)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.modules[module_name] = module


def add_all_models():
    dirs = os.listdir(settings.BASE_DIR.joinpath("internal"))
    for d in dirs:
        possible_model_path = "internal/" + d + "/models.py"
        if not os.path.isfile(possible_model_path):
            continue
        add_models(possible_model_path)


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    context.configure(
        url=DB_URI,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True
    )

    with context.begin_transaction():
        context.run_migrations()


def engine_from_config(configuration, prefix="sqlalchemy.", **kwargs):
    # overriding the method from sqlalchemy to use the custom DB_URI
    options = dict((key[len(prefix):], configuration[key]) for key in configuration if key.startswith(prefix))
    options["_coerce_config"] = True
    options.update(kwargs)
    return create_engine(DB_URI, **options)


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata, compare_type=True)

        with context.begin_transaction():
            context.run_migrations()


add_all_models()
target_metadata = Base.metadata

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
