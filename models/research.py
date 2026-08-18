from pydantic import BaseModel


class ResearchResult(BaseModel):
    startup_idea: str
    target_customers: list[str]
    problems: list[str]
    opportunities: list[str]
    risks: list[str]