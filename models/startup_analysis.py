from pydantic import BaseModel

from models.research import ResearchResult
from models.competitor import CompetitorResult
from models.tech_stack import TechStackResult
from models.synthesis import SynthesisResult


class StartupAnalysis(BaseModel):

    research: ResearchResult

    competitors: CompetitorResult

    tech_stack: TechStackResult

    synthesis: SynthesisResult