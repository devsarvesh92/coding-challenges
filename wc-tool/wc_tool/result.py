


from pydantic import Field


class WCResult:
    byte_count:int = Field(default=0)