import pytest
from wc_tool.strategies.byte_counter import ByteCounter

pytestmark = pytest.mark.bytecounter


def test_byte_counter():
    assert 7 == ByteCounter(content="sarvesh").count().byte_count
