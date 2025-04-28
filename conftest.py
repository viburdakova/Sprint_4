import pytest

from qa_python.main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()