from fastapi import FastAPI

from wayne_vault.cache.client import initialize_redis
from wayne_vault.core.bootstrap import load_logging_config, load_routers, load_admin
from wayne_vault.core.config import settings
from wayne_vault.db.session import initialize_database

app: FastAPI = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"/openapi.json")

load_logging_config()
initialize_database()
initialize_redis()
load_routers(app)
load_admin()
