import logging
import logging.config
import re
from importlib import import_module
from pathlib import Path

import sentry_sdk
from fastapi import FastAPI

from wayne_vault.core.config import settings
from wayne_vault.core.utilities import finder


def load_logging_config():
    logging.info("Loading logging config")

    logging.config.fileConfig(settings.LOGGING_CONFIG)


def load_routers(app: FastAPI = None):
    logging.info("Loading routers...")
    # TODO: Refactor loading routers
    for posix_path in finder(Path(settings.BASE_DIR), file_name="routes", suffix=".py"):
        route_file = re.sub(f'^{settings.BASE_DIR}/', '', str(posix_path)).replace('/', '.')
        mod = import_module(route_file[:-3])
        if router := getattr(mod, "router", None):
            app.include_router(router)


def load_admin():
    logging.info("Loading admin...")

    for posix_path in finder(Path(settings.BASE_DIR), file_name="admin", suffix=".py"):
        route_file = re.sub(f'^{settings.BASE_DIR}/', '', str(posix_path)).replace('/', '.')
        import_module(route_file[:-3])


def initiate_sentry(sentry_dsn: str):
    sentry_sdk.init(dsn=sentry_dsn,
                    traces_sample_rate=1,
                    send_default_pii=False)
