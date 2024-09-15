from abc import ABC, abstractmethod
from wc_tool.result import WCResult


class Counter(ABC):
    @abstractmethod
    def count() -> WCResult:
        """Abstract method for counting"""
