from sqlmodel import SQLModel, Field


class X(SQLModel, table=True):
    name: str = Field(default=None, primary_key=True)
    age: str
