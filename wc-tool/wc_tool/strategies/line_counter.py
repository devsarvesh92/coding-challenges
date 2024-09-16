from ..result import WCResult
from wc_tool.strategies.counter import Counter


class LineCounter(Counter):
    def __init__(self, content: str) -> None:
        self.content: str = content

    def count(self) -> WCResult:
        return WCResult(line_count=len(self.content.splitlines()))
