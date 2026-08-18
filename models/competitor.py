from pydantic import BaseModel


class Competitor(BaseModel):
    name: str
    description: str
    strengths: list[str]
    weaknesses: list[str]


class CompetitorResult(BaseModel):
    competitors: list[Competitor]
    competitive_advantages: list[str]
    market_gaps: list[str]