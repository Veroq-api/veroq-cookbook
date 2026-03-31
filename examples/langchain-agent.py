"""Build a research agent with LangChain + VEROQ.

Uses LangChain's ReAct agent pattern to combine VEROQ's financial
intelligence tools into an autonomous research assistant that can
answer multi-step questions like "Compare NVDA and AMD earnings,
then verify which had better guidance."
"""
from langchain_veroq import VeroqAskTool, VeroqVerifyTool, VeroqScreenerTool
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate

# Initialize VEROQ tools — each wraps a VEROQ API capability
tools = [
    VeroqAskTool(),        # Natural language financial Q&A
    VeroqVerifyTool(),     # Claim verification with evidence chain
    VeroqScreenerTool(),   # NLP stock screener
]

# Build the ReAct agent with a financial research prompt
llm = ChatOpenAI(model="gpt-4o", temperature=0)
prompt = PromptTemplate.from_template(
    "You are a financial research assistant. Use VEROQ tools to answer "
    "questions with real data. Always verify bold claims.\n\n"
    "Tools: {tools}\nTool names: {tool_names}\n\n"
    "Question: {input}\n{agent_scratchpad}"
)
agent = create_react_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Run a multi-step research query
result = executor.invoke({
    "input": "Find oversold AI stocks, then verify if NVDA beat earnings last quarter"
})
print("\n--- Final Answer ---")
print(result["output"])
