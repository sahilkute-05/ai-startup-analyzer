# 🚀 AI Startup Analyzer

> **An AI-powered multi-agent platform that analyzes startup ideas through market research, competitor intelligence, technology recommendations, and strategic synthesis.**

AI Startup Analyzer takes a startup idea as input and uses a **multi-agent AI architecture** to evaluate its market potential, competition, technical feasibility, risks, and MVP direction.

The system combines **Google Gemini, specialized AI agents, MCP (Model Context Protocol), FastAPI, React, PostgreSQL, and Docker** into a production-oriented application.

---
## 🎥 Demo

[▶️ Watch the Demo](https://drive.google.com/file/d/14EOiB1_paIuoeCX1DXNGaNnGzg6aKYdZ/view?usp=drive_link)

## ✨ Features

### 🤖 Multi-Agent AI Analysis

The application divides startup analysis into specialized agents:

* **Research Agent** — Understands the startup idea, target customers, problems, opportunities, and risks.
* **Competitor Agent** — Identifies competitors, their strengths and weaknesses, competitive advantages, and market gaps.
* **Tech Stack Agent** — Recommends an appropriate technology stack and explains architectural decisions.
* **Synthesis Agent** — Combines all previous analyses into a final strategic assessment.

### 📊 Startup Scoring

The platform evaluates the startup across multiple dimensions:

* Market potential
* Competitive landscape
* Technical feasibility
* Overall opportunity

### 🧠 LLM Abstraction Layer

The application separates AI agents from the underlying LLM provider:

```text
Agent
  ↓
LLMService
  ↓
LLMProvider
  ↓
GeminiProvider
  ↓
Google Gemini API
```

This makes the system easier to maintain and allows additional LLM providers to be added in the future.

### 🔌 MCP Integration

The project uses **Model Context Protocol (MCP)** to provide tools for market analysis and external data operations.

Current MCP capabilities include:

* `calculate_market_score`
* `search_web`
* `get_competitor_data`
* `analyze_market`

The MCP server is launched and managed by the backend rather than requiring a separate Docker container.

### ⚡ Parallel Agent Execution

Research and competitor analysis are executed concurrently using Python's asynchronous capabilities:

```python
await asyncio.gather(...)
```

This reduces unnecessary sequential execution time.

### 🐳 Dockerized

The entire application can be run using Docker Compose.

```text
React/Vite Frontend
        ↓
     FastAPI
        ↓
 StartupAnalyzer
        ↓
 ┌──────┴────────┐
 │               │
Research     Competitor
 │               │
 └──────┬────────┘
        ↓
   MCP Analysis
        ↓
   Tech Stack
        ↓
    Synthesis
        ↓
 Final Analysis
```

---

# 🏗️ System Architecture

```text
                         ┌─────────────────────────┐
                         │      React + Vite       │
                         │        Frontend         │
                         │        Port 3000         │
                         └────────────┬────────────┘
                                      │
                                      │ POST /analyze
                                      ▼
                         ┌─────────────────────────┐
                         │        FastAPI          │
                         │         Backend         │
                         │        Port 8000         │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │    StartupAnalyzer      │
                         │      Orchestrator       │
                         └────────────┬────────────┘
                                      │
                   ┌──────────────────┼──────────────────┐
                   │                  │                  │
                   ▼                  ▼                  ▼
            Research Agent     Competitor Agent    MCP Analysis
                   │                  │                  │
                   └──────────────────┼──────────────────┘
                                      ▼
                             Tech Stack Agent
                                      │
                                      ▼
                              Synthesis Agent
                                      │
                                      ▼
                              StartupAnalysis
                                      │
                                      ▼
                              React Results UI
```

---

# 🧩 Multi-Agent Workflow

## 1. Research Agent

The Research Agent analyzes the startup idea and identifies:

* Startup concept
* Target customers
* Customer problems
* Market opportunities
* Potential risks

Example output:

```text
Startup Idea
    ↓
Target Customers
    ↓
Problems
    ↓
Opportunities
    ↓
Risks
```

---

## 2. Competitor Agent

The Competitor Agent evaluates the competitive environment.

It identifies:

* Existing competitors
* Competitor descriptions
* Strengths
* Weaknesses
* Competitive advantages
* Market gaps

This helps determine whether the proposed startup has meaningful differentiation.

---

## 3. MCP Market Analysis

The orchestrator uses MCP tools to perform additional market-level analysis.

Available tools include:

```text
calculate_market_score
search_web
get_competitor_data
analyze_market
```

MCP allows the AI system to interact with tools through a standardized interface rather than tightly coupling tools directly to individual agents.

---

## 4. Tech Stack Agent

The Tech Stack Agent determines the technology required to build the proposed product.

It evaluates:

* Frontend
* Backend
* Database
* AI/ML
* Infrastructure
* External APIs
* Architecture

The agent also provides reasoning behind the recommendations rather than simply returning a list of technologies.

---

## 5. Synthesis Agent

Finally, the Synthesis Agent combines the outputs from the previous stages.

It produces:

* Overall score
* Market assessment
* Competitive assessment
* Technical feasibility
* Recommended MVP
* Key risks
* Final recommendation

The result is returned to the frontend as a structured `StartupAnalysis`.

---

# 🛠️ Tech Stack

| Category             | Technology                      |
| -------------------- | ------------------------------- |
| Frontend             | React 19                        |
| Frontend Build Tool  | Vite                            |
| Backend              | FastAPI                         |
| Programming Language | Python                          |
| AI / LLM             | Google Gemini                   |
| Gemini SDK           | `google-genai`                  |
| Agent Architecture   | Custom Multi-Agent Architecture |
| Tool Integration     | MCP                             |
| Data Validation      | Pydantic                        |
| Database             | PostgreSQL                      |
| ORM / Database Layer | Prisma                          |
| Containerization     | Docker                          |
| Orchestration        | Docker Compose                  |
| API Communication    | REST                            |
| Async Processing     | Python `asyncio`                |

---

# 📁 Project Structure

```text
ai-startup-analyzer/
│
├── agents/
│   ├── base_agent.py
│   ├── research.py
│   ├── competitor.py
│   ├── tech_stack.py
│   ├── synthesis.py
│   ├── planner.py
│   └── report.py
│
├── api/
│   └── main.py
│
├── mcp_integration/
│   ├── __init__.py
│   ├── mcp_client.py
│   └── server.py
│
├── orchestrator/
│   └── startup_analyzer.py
│
├── providers/
│   ├── llm_provider.py
│   └── gemini_provider.py
│
├── services/
│   └── llm_service.py
│
├── frontend/
│   ├── src/
│   │   └── App.jsx
│   ├── package.json
│   └── Dockerfile
│
├── test/
│   ├── test_gemini.py
│   ├── test_research.py
│   ├── test_orchestrator.py
│   └── test_async_orchestrator.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

---

# 🔄 Request Flow

When a user submits a startup idea, the request follows this pipeline:

```text
User enters startup idea
        │
        ▼
React Frontend
        │
        │ POST /analyze
        ▼
FastAPI Backend
        │
        ▼
StartupAnalyzer
        │
        ├───────────────┐
        ▼               ▼
Research Agent    Competitor Agent
        │               │
        └───────┬───────┘
                │
                ▼
          MCP Analysis
                │
                ▼
        Tech Stack Agent
                │
                ▼
        Synthesis Agent
                │
                ▼
       Structured Analysis
                │
                ▼
          React Frontend
                │
                ▼
          Results Dashboard
```

---

# 🚀 Getting Started

## Prerequisites

Make sure the following are installed:

* Python 3.11+
* Node.js
* npm
* Docker Desktop
* Git
* A Google Gemini API key

---

# 🔐 Environment Variables

Create a `.env` file based on `.env.example`.

Example:

```env
GEMINI_API_KEY=your_gemini_api_key
```

> Never commit your actual API key to GitHub.

---

# 🐳 Running with Docker

The recommended way to run the complete application is Docker Compose.

### 1. Clone the repository

```bash
git clone https://github.com/sahilkute-05/ai-startup-analyzer.git
cd ai-startup-analyzer
```

### 2. Configure environment variables

Create your `.env` file:

```bash
cp .env.example .env
```

Then add your Gemini API key.

### 3. Build the containers

```bash
docker compose build
```

### 4. Start the application

```bash
docker compose up -d
```

### 5. Check running containers

```bash
docker compose ps
```

### 6. Open the application

Frontend:

```text
http://localhost:3000
```

Backend:

```text
http://localhost:8000
```

Health check:

```text
http://localhost:8000/health
```

---

# 💻 Running Without Docker

## Backend

Create and activate a virtual environment:

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start FastAPI:

```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

---

## Frontend

Navigate to the frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will be available at:

```text
http://localhost:3000
```

---

# 🔗 API Endpoints

## `GET /`

Returns basic information about the API.

```http
GET /
```

---

## `GET /health`

Checks whether the backend is running.

```http
GET /health
```

Example:

```json
{
  "status": "healthy"
}
```

---

## `POST /analyze`

Analyzes a startup idea using the complete multi-agent pipeline.

```http
POST /analyze
```

Example request:

```json
{
  "idea": "An AI platform that helps small businesses automate customer support."
}
```

The backend processes the idea through the agent pipeline and returns structured startup analysis.

---

# 🧪 Testing

The project contains tests for individual components and the orchestration pipeline.

Example:

```bash
python test/test_gemini.py
```

Research agent:

```bash
python -m test.test_research
```

Orchestrator:

```bash
python -m test.test_orchestrator
```

Async orchestrator:

```bash
python -m test.test_async_orchestrator
```

---

# 🔌 Why MCP?

A major goal of this project was to explore how AI agents can interact with external tools through a standardized protocol.

Instead of embedding every tool directly inside an agent, the system exposes capabilities through an MCP server.

```text
AI Agent
   │
   ▼
MCP Client
   │
   ▼
MCP Server
   │
   ├── Market Score
   ├── Web Search
   ├── Competitor Data
   └── Market Analysis
```

This makes the architecture more modular and provides a foundation for adding additional tools in the future.

---

# 🧠 Why a Multi-Agent Architecture?

A single LLM prompt could theoretically generate the entire startup analysis, but separating responsibilities provides several advantages.

### Specialization

Each agent focuses on a specific problem.

### Modularity

Agents can be independently modified or replaced.

### Parallelism

Independent agents can run concurrently.

### Maintainability

The orchestration layer controls workflow while agents focus on their individual tasks.

### Extensibility

Additional agents can be introduced without redesigning the entire application.

---

# ⚡ Performance Consideration

Research and competitor analysis are independent operations.

Instead of:

```text
Research
   ↓
Competitor
```

the orchestrator executes them concurrently:

```text
       ┌── Research ──┐
Start ─┤              ├─→ Continue
       └─ Competitor ─┘
```

using:

```python
await asyncio.gather(
    research_task,
    competitor_task
)
```

This improves pipeline efficiency when both operations require LLM calls.

---

# 🔮 Future Improvements

Potential future enhancements include:

* [ ] Persistent analysis history
* [ ] User authentication
* [ ] PostgreSQL-backed startup reports
* [ ] Streaming agent responses
* [ ] Real-time progress indicators
* [ ] More external MCP tools
* [ ] Additional LLM providers
* [ ] Advanced competitor intelligence
* [ ] Market trend visualization
* [ ] PDF report generation
* [ ] Startup comparison
* [ ] Deployment to a cloud platform
* [ ] Automated evaluation of agent responses
* [ ] Agent observability and tracing

---

# 📸 Screenshots

<img width="1915" height="853" alt="Screenshot 2026-08-18 183952" src="https://github.com/user-attachments/assets/7640bddb-6720-4737-980c-3da23be9b563" />
<img width="1919" height="849" alt="Screenshot 2026-08-18 184000" src="https://github.com/user-attachments/assets/0dec6f1d-8a1c-4b62-a8fe-c33f433f9546" />
<img width="1915" height="850" alt="Screenshot 2026-08-18 184013" src="https://github.com/user-attachments/assets/a85e02c1-a06b-4ac9-9586-adde7772b2fb" />
<img width="1919" height="852" alt="Screenshot 2026-08-18 184028" src="https://github.com/user-attachments/assets/ef238a7a-a63e-48b3-b887-781af7bfa9c2" />
<img width="1919" height="838" alt="Screenshot 2026-08-18 184037" src="https://github.com/user-attachments/assets/afcc1d93-0352-4f22-ac38-955af3d2211e" />
<img width="1919" height="839" alt="Screenshot 2026-08-18 184048" src="https://github.com/user-attachments/assets/990ca56c-a5fd-4338-ba3c-0f6cc1067abb" />


---

# 🎯 What This Project Demonstrates

This project demonstrates practical implementation of:

* Multi-agent AI systems
* LLM provider abstraction
* Google Gemini integration
* Structured LLM outputs
* Pydantic data validation
* Async Python programming
* Parallel agent execution
* Model Context Protocol
* FastAPI REST APIs
* React frontend development
* Docker containerization
* Docker Compose
* Modular backend architecture
* AI-driven business analysis

---

# 📚 Key Learning Outcomes

Building this project involved solving several real-world engineering problems, including:

* Designing an extensible multi-agent architecture
* Separating business logic from LLM provider logic
* Handling structured LLM responses
* Managing asynchronous AI operations
* Integrating MCP tools with an AI workflow
* Handling API errors, timeouts, and retries
* Connecting a React frontend to a FastAPI backend
* Containerizing frontend and backend services
* Managing multi-container applications with Docker Compose

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/your-feature
```

3. Commit your changes

```bash
git commit -m "Add your feature"
```

4. Push the branch

```bash
git push origin feature/your-feature
```

5. Open a Pull Request

---


# 👨‍💻 Author

**Sahil Kute**

Computer Engineering Student
Pune, India

---

⭐ If you found this project interesting, consider giving the repository a star!

**Built with Python, React, FastAPI, Gemini, MCP, and Docker.**
