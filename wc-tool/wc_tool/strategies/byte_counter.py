from ..result import WCResult
from wc_tool.strategies.counter import Counter


class ByteCounter(Counter):
    def __init__(self, content: str) -> None:
        self.content: str = content

    def count(self) -> WCResult:
        return WCResult(byte_count=len(self.content.encode("utf-8")))
