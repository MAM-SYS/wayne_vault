import logging
from typing import Optional

import aioredis
from aioredis import Redis, BlockingConnectionPool

from wayne_vault.core.config import settings

redis: Optional[Redis] = None


def initialize_redis():
    global redis

    logging.info("Initializing redis client...")

    pool = BlockingConnectionPool.from_url(url=settings.REDIS_URI, decode_responses=True)
    redis = aioredis.Redis(connection_pool=pool)
