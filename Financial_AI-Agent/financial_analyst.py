from phi.agent import Agent 
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv


#Agent for the searching on the web
web_search_agent =Agent(
    name="Web Search Agent",
    role ="search the web for the info",
    model = Groq(id="llama-3.2-11b-vision-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always includes sources that are perfectly match with the given content"],
    show_tool_calls=True,
    markdown=True
)

# Financial Agent 
finance_agent =Agent(
    name="Finance AI Agent",
    role ="Give the analysis of the finance informaation",
    model = Groq(id="llama-3.2-11b-vision-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True)],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent=Agent(
    team=[web_search_agent,finance_agent],
    model = Groq(id="llama-3.2-11b-vision-preview"),
    instructions=["Always includes sources ","Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent.print_response("Summarize analyst reccommondation and give me the latest news of the NVDA",stream=True)