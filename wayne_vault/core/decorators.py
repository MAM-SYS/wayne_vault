import asyncio
import functools


def synchronize(func):
    """Async task synchronizer"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(func(*args, **kwargs))

    return wrapper
