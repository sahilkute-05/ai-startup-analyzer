from models.synthesis import SynthesisResult

from agents.base_agent import BaseAgent
from services.llm_service import LLMService


class SynthesisAgent(BaseAgent):

    def __init__(
        self,
        llm_service: LLMService
    ):

        system_prompt = """
You are a senior startup strategist and product advisor.

Your job is to analyze the research, competitor analysis,
and technical analysis provided to you.

Based ONLY on the provided information:

1. Evaluate the startup opportunity.
2. Assess the competitive situation.
3. Assess technical feasibility.
4. Recommend the smallest useful MVP.
5. Identify the most important risks.
6. Give a final recommendation.

Be realistic.

Do not blindly recommend building the startup.

The overall score must be an integer between 0 and 100.

Return the result using the required structured format.
"""

        super().__init__(
            name="Synthesis Agent",
            role="Senior startup strategist and product advisor",
            system_prompt=system_prompt
        )

        self.llm_service = llm_service

    async def run_async(
        self,
        context: str
    ) -> SynthesisResult:

        return await self.llm_service.generate_structured_async(
            system_prompt=self.system_prompt,
            user_prompt=context,
            response_model=SynthesisResult
        )

    def run(
        self,
        context: str
    ) -> SynthesisResult:

        return self.llm_service.generate_structured(
            system_prompt=self.system_prompt,
            user_prompt=context,
            response_model=SynthesisResult
        )