import logging
from functools import wraps
from traceback import print_exc


def tracer(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            logging.exception(e)
            print_exc()
            raise e

    return wrapper
