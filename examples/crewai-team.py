"""Create a CrewAI research team powered by VEROQ.

Defines three specialized agents — a market analyst, a fact-checker,
and a portfolio strategist — that collaborate to produce a verified
investment thesis for any ticker.
"""
from crewai import Agent, Task, Crew, Process
from crewai_veroq import VeroqAskTool, VeroqVerifyTool, VeroqFullTool

# Shared VEROQ tools for the crew
ask_tool = VeroqAskTool()
verify_tool = VeroqVerifyTool()
full_tool = VeroqFullTool()  # Cross-reference: 9 data sources in one call

# Agent 1: Market Analyst — gathers data and technicals
analyst = Agent(
    role="Market Analyst",
    goal="Gather comprehensive data on the target ticker",
    backstory="Senior equity analyst with 15 years of experience.",
    tools=[ask_tool, full_tool],
    verbose=True,
)

# Agent 2: Fact Checker — verifies claims from the analyst
checker = Agent(
    role="Fact Checker",
    goal="Verify every quantitative claim the analyst makes",
    backstory="Former auditor who trusts nothing without evidence.",
    tools=[verify_tool],
    verbose=True,
)

# Agent 3: Strategist — synthesizes into actionable advice
strategist = Agent(
    role="Portfolio Strategist",
    goal="Turn verified research into a clear buy/hold/sell thesis",
    backstory="CFA charterholder managing a $500M fund.",
    tools=[ask_tool],
    verbose=True,
)

# Define the sequential workflow
research = Task(description="Analyze NVDA: price, technicals, earnings, sentiment", agent=analyst)
verify = Task(description="Verify the analyst's top 3 claims", agent=checker)
thesis = Task(description="Write a 3-paragraph investment thesis with risk factors", agent=strategist)

# Run the crew — agents collaborate sequentially
crew = Crew(agents=[analyst, checker, strategist], tasks=[research, verify, thesis], process=Process.sequential)
result = crew.kickoff()
print("\n--- Investment Thesis ---")
print(result)
