from mcp.server import MCPServer


# ============================================================
# MCP SERVER
# ============================================================

mcp = MCPServer("AI Startup Analyzer MCP Server")


# ============================================================
# TOOL 1: MARKET SCORE
# ============================================================

@mcp.tool()
def calculate_market_score(
    market_size: float,
    demand: float,
    competition: float
) -> dict:
    """
    Calculate a startup market opportunity score.

    Inputs:
    - market_size: Market size score from 0 to 100.
    - demand: Customer demand score from 0 to 100.
    - competition: Competition intensity from 0 to 100.

    Higher market size and demand increase the score.
    Higher competition decreases the score.
    """

    market_size = max(0, min(100, market_size))
    demand = max(0, min(100, demand))
    competition = max(0, min(100, competition))

    score = (
        market_size * 0.40
        + demand * 0.40
        + (100 - competition) * 0.20
    )

    score = round(score, 2)

    if score >= 75:
        rating = "Excellent"
    elif score >= 60:
        rating = "Good"
    elif score >= 40:
        rating = "Moderate"
    else:
        rating = "Weak"

    return {
        "market_score": score,
        "rating": rating,
        "market_size": market_size,
        "demand": demand,
        "competition": competition
    }


# ============================================================
# TOOL 2: WEB SEARCH
# ============================================================

@mcp.tool()
def search_web(query: str) -> dict:
    """
    Simulate a web research operation for the startup analyzer.

    This V1 implementation returns structured search guidance.
    A real search API can be connected later.
    """

    if not query or not query.strip():
        return {
            "query": query,
            "status": "error",
            "message": "Search query cannot be empty."
        }

    query = query.strip()

    return {
        "query": query,
        "status": "success",
        "search_type": "startup_market_research",
        "recommended_sources": [
            "Industry reports",
            "Competitor websites",
            "Product Hunt",
            "Crunchbase",
            "Google Trends",
            "News articles",
            "Research papers"
        ],
        "message": f"Research query prepared for: {query}"
    }


# ============================================================
# TOOL 3: COMPETITOR DATA
# ============================================================

@mcp.tool()
def get_competitor_data(
    startup_category: str
) -> dict:
    """
    Return a structured competitor-analysis template.

    This V1 implementation provides the structure required by
    the Competitor Agent. Real competitor APIs can be integrated later.
    """

    if not startup_category or not startup_category.strip():
        return {
            "status": "error",
            "message": "Startup category cannot be empty."
        }

    category = startup_category.strip()

    return {
        "status": "success",
        "category": category,
        "competitor_fields": [
            "Company name",
            "Product",
            "Target customers",
            "Pricing",
            "Key features",
            "Strengths",
            "Weaknesses",
            "Market positioning"
        ],
        "message": (
            f"Competitor research structure generated for "
            f"{category}."
        )
    }


# ============================================================
# TOOL 4: MARKET ANALYSIS
# ============================================================

@mcp.tool()
def analyze_market(
    market_size: float,
    demand: float,
    competition: float,
    growth_potential: float
) -> dict:
    """
    Produce a combined startup market analysis.

    All scores are expected between 0 and 100.
    """

    market_size = max(0, min(100, market_size))
    demand = max(0, min(100, demand))
    competition = max(0, min(100, competition))
    growth_potential = max(0, min(100, growth_potential))

    opportunity_score = (
        market_size * 0.30
        + demand * 0.30
        + (100 - competition) * 0.15
        + growth_potential * 0.25
    )

    opportunity_score = round(opportunity_score, 2)

    if opportunity_score >= 80:
        recommendation = "Highly attractive market"
    elif opportunity_score >= 65:
        recommendation = "Attractive market"
    elif opportunity_score >= 50:
        recommendation = "Potential market requiring validation"
    else:
        recommendation = "High-risk market"

    return {
        "market_size": market_size,
        "demand": demand,
        "competition": competition,
        "growth_potential": growth_potential,
        "opportunity_score": opportunity_score,
        "recommendation": recommendation
    }


# ============================================================
# SERVER START
# ============================================================

if __name__ == "__main__":
    mcp.run()