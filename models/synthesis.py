from pydantic import BaseModel, Field


class SynthesisResult(BaseModel):

    overall_score: int = Field(
        ge=0,
        le=100
    )

    market_assessment: str

    competitive_assessment: str

    technical_feasibility: str

    recommended_mvp: list[str]

    key_risks: list[str]

    final_recommendation: str