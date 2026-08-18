"""
FastAPI backend for AI Startup Analyzer.

Request flow:

Frontend
    ↓
POST /analyze
    ↓
FastAPI
    ↓
LLMService
    ↓
Agents
    ↓
StartupAnalyzer
    ↓
StartupAnalysis JSON
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from providers.gemini_provider import GeminiProvider
from services.llm_service import LLMService

from agents.research import ResearchAgent
from agents.competitor import CompetitorAgent
from agents.tech_stack import TechStackAgent
from agents.synthesis import SynthesisAgent

from orchestrator.startup_analyzer import StartupAnalyzer


# ============================================================
# FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="AI Startup Analyzer API",
    description=(
        "AI-powered startup analysis using "
        "multi-agent orchestration and MCP."
    ),
    version="1.0.0"
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",   # Added for Docker React frontend
        "http://127.0.0.1:3000",   # Added for Docker React frontend
        "http://localhost:5173",   # Original local vite port
        "http://127.0.0.1:5173",   # Original local vite port
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# REQUEST MODEL
# ============================================================

class AnalyzeRequest(BaseModel):
    startup_idea: str


# ============================================================
# CREATE STARTUP ANALYZER
# ============================================================

def create_analyzer() -> StartupAnalyzer:
    """
    Create the complete AI Startup Analyzer dependency chain.

    GeminiProvider
        ↓
    LLMService
        ↓
    Agents
        ↓
    StartupAnalyzer
    """

    # --------------------------------------------------------
    # LLM provider
    # --------------------------------------------------------

    provider = GeminiProvider()

    # --------------------------------------------------------
    # LLM service
    # --------------------------------------------------------

    llm_service = LLMService(
        provider=provider
    )

    # --------------------------------------------------------
    # Agents
    # --------------------------------------------------------

    research_agent = ResearchAgent(
        llm_service=llm_service
    )

    competitor_agent = CompetitorAgent(
        llm_service=llm_service
    )

    tech_stack_agent = TechStackAgent(
        llm_service=llm_service
    )

    synthesis_agent = SynthesisAgent(
        llm_service=llm_service
    )

    # --------------------------------------------------------
    # Orchestrator
    # --------------------------------------------------------

    return StartupAnalyzer(
        research_agent=research_agent,
        competitor_agent=competitor_agent,
        tech_stack_agent=tech_stack_agent,
        synthesis_agent=synthesis_agent
    )


# ============================================================
# ROOT ENDPOINT
# ============================================================

@app.get("/")
async def root():

    return {
        "status": "success",
        "service": "AI Startup Analyzer API",
        "version": "1.0.0"
    }


# ============================================================
# HEALTH ENDPOINT
# ============================================================

@app.get("/health")
async def health():

    return {
        "status": "healthy"
    }


# ============================================================
# ANALYZE ENDPOINT
# ============================================================

@app.post("/analyze")
async def analyze_startup(
    request: AnalyzeRequest
):
    """
    Analyze a startup idea using the complete
    multi-agent pipeline.
    """

    startup_idea = request.startup_idea.strip()

    # --------------------------------------------------------
    # Validate input
    # --------------------------------------------------------

    if not startup_idea:

        raise HTTPException(
            status_code=400,
            detail="startup_idea cannot be empty."
        )

    try:

        print(
            "\n============================================"
        )

        print(
            "Received startup analysis request:"
        )

        print(
            startup_idea
        )

        print(
            "============================================"
        )

        # ----------------------------------------------------
        # Create analyzer
        # ----------------------------------------------------

        print("\nCreating Startup Analyzer...")

        analyzer = create_analyzer()

        print("Startup Analyzer created.")

        # ----------------------------------------------------
        # Run complete async pipeline
        # ----------------------------------------------------

        print("\nStarting analysis pipeline...")

        result = await analyzer.analyze_async(
            startup_idea
        )

        print("\nAnalysis pipeline completed successfully.")

        # ----------------------------------------------------
        # Return JSON
        # ----------------------------------------------------

        response_data = result.model_dump()

        print("\nReturning analysis result to frontend.")

        return {
            "status": "success",
            "data": response_data
        }

    except Exception as error:

        print(
            "\n============================================"
        )

        print(
            "STARTUP ANALYSIS FAILED"
        )

        print(
            f"Error type: {type(error).__name__}"
        )

        print(
            f"Error: {error}"
        )

        print(
            "============================================"
        )

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


# ============================================================
# LOCAL DEVELOPMENT SERVER
# ============================================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )