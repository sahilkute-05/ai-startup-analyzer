from pathlib import Path

from agents.base_agent import BaseAgent
from services.llm_service import LLMService


class ResearchAgent(BaseAgent):

    def __init__(self, llm_service: LLMService):
        super().__init__(
            name="Research Agent",
            role="Market research specialist",
            system_prompt=self.load_prompt()
        )

        self.llm_service = llm_service

    def load_prompt(self) -> str:
        prompt_path = (
            Path(__file__).parent.parent
            / "prompts"
            / "research_prompt.txt"
        )

        return prompt_path.read_text(encoding="utf-8")

    def run(self, task: str) -> str:
        return self.llm_service.generate(
            system_prompt=self.system_prompt,
            user_prompt=task
        )