


from pydantic import BaseModel, Field


class WCResult(BaseModel):
    byte_count:int = Field(default=0)
    line_count:int = Field(default=0)