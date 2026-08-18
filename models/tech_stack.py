from pydantic import BaseModel


class TechStackResult(BaseModel):
    frontend: list[str]
    backend: list[str]
    database: list[str]
    ai_ml: list[str]
    infrastructure: list[str]
    external_apis: list[str]
    reasoning: str