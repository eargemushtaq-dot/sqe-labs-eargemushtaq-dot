import pytest
import auth

@pytest.fixture(autouse=True)


def fresh_store():
    """give every test a clean in-memory store."""
    auth.initialize_store()