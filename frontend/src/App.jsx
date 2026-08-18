import { useState } from "react";
import "./App.css";

const API_URL =
  import.meta.env.VITE_API_URL || "http://localhost:8000";

function App() {
  const [startupIdea, setStartupIdea] = useState("");
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const analyzeStartup = async () => {
    const idea = startupIdea.trim();

    if (!idea) {
      setError("Please enter a startup idea.");
      return;
    }

    setLoading(true);
    setError("");
    setAnalysis(null);

    try {
      const response = await fetch(`${API_URL}/analyze`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          startup_idea: idea,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || "Startup analysis failed."
        );
      }

      setAnalysis(data.data);
    } catch (err) {
      setError(
        err.message ||
          "Unable to connect to the AI Startup Analyzer API."
      );
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (event) => {
    if (event.key === "Enter" && (event.ctrlKey || event.metaKey)) {
      analyzeStartup();
    }
  };

  return (
    <div className="app">
      {/* ================= HEADER ================= */}

      <header className="header">
        <div className="brand">
          <div className="brand-icon">AI</div>

          <div>
            <h1>AI Startup Analyzer</h1>
            <p>Multi-Agent Startup Intelligence</p>
          </div>
        </div>

        <div className="status">
          <span className="status-dot"></span>
          AI Engine
        </div>
      </header>

      {/* ================= MAIN ================= */}

      <main className="container">

        {/* ================= HERO ================= */}

        <section className="hero">
          <div className="hero-badge">
            MULTI-AGENT AI ANALYSIS
          </div>

          <h2>
            Turn your startup idea into
            <span> actionable insights.</span>
          </h2>

          <p>
            Analyze your startup idea using specialized AI agents
            for market research, competitors, technology and
            strategic evaluation.
          </p>
        </section>

        {/* ================= INPUT ================= */}

        <section className="input-card">
          <div className="section-heading">
            <div>
              <h3>Startup Idea</h3>
              <p>
                Describe your startup idea in a few sentences.
              </p>
            </div>

            <span className="shortcut">
              Ctrl + Enter
            </span>
          </div>

          <textarea
            value={startupIdea}
            onChange={(event) =>
              setStartupIdea(event.target.value)
            }
            onKeyDown={handleKeyDown}
            placeholder="Example: An AI-powered fitness application tailored for college students..."
            rows={6}
          />

          <div className="input-footer">
            <span>
              {startupIdea.length} characters
            </span>

            <button
              onClick={analyzeStartup}
              disabled={loading}
            >
              {loading ? (
                <>
                  <span className="spinner"></span>
                  Analyzing...
                </>
              ) : (
                <>
                  Analyze Startup
                  <span>→</span>
                </>
              )}
            </button>
          </div>
        </section>

        {/* ================= LOADING ================= */}

        {loading && (
          <section className="loading-card">
            <div className="loading-animation">
              <div></div>
              <div></div>
              <div></div>
            </div>

            <h3>AI agents are analyzing your idea...</h3>

            <p>
              Research Agent → Competitor Agent →
              Tech Stack Agent → Synthesis Agent
            </p>

            <span>
              This can take a little while because multiple
              AI agents are being executed.
            </span>
          </section>
        )}

        {/* ================= ERROR ================= */}

        {error && !loading && (
          <section className="error-card">
            <div className="error-icon">!</div>

            <div>
              <h3>Analysis failed</h3>
              <p>{error}</p>
            </div>
          </section>
        )}

        {/* ================= RESULTS ================= */}

        {analysis && !loading && (
          <Results analysis={analysis} />
        )}

      </main>

      {/* ================= FOOTER ================= */}

      <footer>
        <p>
          AI Startup Analyzer · Multi-Agent Architecture
        </p>

        <span>
          Research · Competition · Technology · Strategy
        </span>
      </footer>
    </div>
  );
}


/* ============================================================
   RESULTS COMPONENT
============================================================ */

function Results({ analysis }) {
  const {
    research,
    competitors,
    tech_stack,
    synthesis,
  } = analysis;

  return (
    <section className="results">

      <div className="results-header">
        <div>
          <div className="hero-badge">
            ANALYSIS COMPLETE
          </div>

          <h2>Startup Analysis</h2>

          <p>
            AI-generated analysis based on your startup idea.
          </p>
        </div>

        <div className="score-card">
          <span>Overall Score</span>

          <strong>
            {synthesis.overall_score}
          </strong>

          <small>/ 100</small>
        </div>
      </div>


      {/* ================= RESEARCH ================= */}

      <ResultSection
        number="01"
        title="Market Research"
        subtitle="Understanding the startup opportunity"
      >

        <div className="idea-box">
          <span>Startup Idea</span>
          <p>{research.startup_idea}</p>
        </div>

        <ListSection
          title="Target Customers"
          items={research.target_customers}
        />

        <ListSection
          title="Problems"
          items={research.problems}
        />

        <ListSection
          title="Market Opportunities"
          items={research.opportunities}
        />

        <ListSection
          title="Risks"
          items={research.risks}
        />

      </ResultSection>


      {/* ================= COMPETITORS ================= */}

      <ResultSection
        number="02"
        title="Competitive Analysis"
        subtitle="Understanding the competitive landscape"
      >

        <div className="competitor-grid">
          {competitors.competitors.map(
            (competitor, index) => (
              <div
                className="competitor-card"
                key={index}
              >
                <h4>{competitor.name}</h4>

                <p className="competitor-description">
                  {competitor.description}
                </p>

                <div className="two-column">
                  <div>
                    <h5>Strengths</h5>

                    <ul>
                      {competitor.strengths.map(
                        (item, i) => (
                          <li key={i}>{item}</li>
                        )
                      )}
                    </ul>
                  </div>

                  <div>
                    <h5>Weaknesses</h5>

                    <ul>
                      {competitor.weaknesses.map(
                        (item, i) => (
                          <li key={i}>{item}</li>
                        )
                      )}
                    </ul>
                  </div>
                </div>
              </div>
            )
          )}
        </div>

        <ListSection
          title="Competitive Advantages"
          items={competitors.competitive_advantages}
        />

        <ListSection
          title="Market Gaps"
          items={competitors.market_gaps}
        />

      </ResultSection>


      {/* ================= TECH STACK ================= */}

      <ResultSection
        number="03"
        title="Technology Stack"
        subtitle="Recommended technical architecture"
      >

        <div className="tech-grid">

          <TechCard
            title="Frontend"
            items={tech_stack.frontend}
          />

          <TechCard
            title="Backend"
            items={tech_stack.backend}
          />

          <TechCard
            title="Database"
            items={tech_stack.database}
          />

          <TechCard
            title="AI / ML"
            items={tech_stack.ai_ml}
          />

          <TechCard
            title="Infrastructure"
            items={tech_stack.infrastructure}
          />

          <TechCard
            title="External APIs"
            items={tech_stack.external_apis}
          />

        </div>

        <div className="reasoning-box">
          <h4>Architectural Reasoning</h4>
          <p>{tech_stack.reasoning}</p>
        </div>

      </ResultSection>


      {/* ================= SYNTHESIS ================= */}

      <ResultSection
        number="04"
        title="Strategic Synthesis"
        subtitle="Final startup evaluation"
      >

        <div className="assessment-grid">

          <Assessment
            title="Market Assessment"
            text={synthesis.market_assessment}
          />

          <Assessment
            title="Competitive Assessment"
            text={synthesis.competitive_assessment}
          />

          <Assessment
            title="Technical Feasibility"
            text={synthesis.technical_feasibility}
          />

        </div>

        <div className="mvp-box">

          <h4>Recommended MVP</h4>

          <ul>
            {synthesis.recommended_mvp.map(
              (item, index) => (
                <li key={index}>{item}</li>
              )
            )}
          </ul>

        </div>

        <div className="risk-box">

          <h4>Key Risks</h4>

          <ul>
            {synthesis.key_risks.map(
              (item, index) => (
                <li key={index}>{item}</li>
              )
            )}
          </ul>

        </div>

        <div className="recommendation">

          <span>FINAL RECOMMENDATION</span>

          <p>
            {synthesis.final_recommendation}
          </p>

        </div>

      </ResultSection>

    </section>
  );
}


/* ============================================================
   REUSABLE COMPONENTS
============================================================ */

function ResultSection({
  number,
  title,
  subtitle,
  children,
}) {
  return (
    <article className="result-section">

      <div className="result-section-header">

        <div className="section-number">
          {number}
        </div>

        <div>
          <h3>{title}</h3>
          <p>{subtitle}</p>
        </div>

      </div>

      <div className="result-content">
        {children}
      </div>

    </article>
  );
}


function ListSection({ title, items }) {
  return (
    <div className="list-section">

      <h4>{title}</h4>

      <ul>
        {items.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>

    </div>
  );
}


function TechCard({ title, items }) {
  return (
    <div className="tech-card">

      <h4>{title}</h4>

      <div className="tag-container">
        {items.map((item, index) => (
          <span key={index}>{item}</span>
        ))}
      </div>

    </div>
  );
}


function Assessment({ title, text }) {
  return (
    <div className="assessment-card">

      <h4>{title}</h4>

      <p>{text}</p>

    </div>
  );
}


export default App;