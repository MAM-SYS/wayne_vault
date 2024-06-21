from fastapi import FastAPI

from escrow.cache.client import initialize_redis
from escrow.core.bootstrap import load_logging_config, load_routers, load_admin, initiate_sentry
from escrow.core.config import settings
from escrow.db.session import initialize_database

app: FastAPI = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"/openapi.json")

load_logging_config()
initialize_database()
initialize_redis()
initiate_sentry(settings.SENTRY_DSN)
load_routers(app)
load_admin()
