from src.utils.unitofworks import UnitOfWork

from tests.db import async_session_maker


class TestUnitOfWork(UnitOfWork):
    def __init__(self):
        self.session_factory = async_session_maker