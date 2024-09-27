

import pytest
from wc_tool.strategies.line_counter import LineCounter

pytestmark = pytest.mark.linecounter

def test_line_counter():
    assert 2 == LineCounter(content="My name is sarvesh \n How about you?").count().line_count
