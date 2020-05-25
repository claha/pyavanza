"""Common code for unit testing pyavanza."""
import asyncio
import unittest


def sync(coro):
    """Use this wrapper to run a asynchronous test."""

    def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(coro(*args, **kwargs))

    return wrapper


class TestCase(unittest.TestCase):
    """Base test case class for all pyavanza unit test."""

    def shortDescription(self):
        """Disable printing of docstring in test runner."""
        return None
