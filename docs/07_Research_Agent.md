# Research Agent

## Responsibility

The Research Agent analyzes a startup idea from a market perspective.

## Input

A startup idea provided as a string.

## Output

A market research response.

## Architecture

User
 ↓
ResearchAgent
 ↓
LLMService
 ↓
LLM

## Important Concepts

### Inheritance

ResearchAgent inherits from BaseAgent.

### Dependency Injection

LLMService is passed into ResearchAgent.

### Prompt Separation

The system prompt is stored in prompts/research_prompt.txt.

### Single Responsibility

ResearchAgent only handles market research.