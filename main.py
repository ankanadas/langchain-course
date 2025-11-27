from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

@tool
def search(query: str) -> str:
    """Search over internet

    Args:
        query: Search term to look for
    Returns: 
        The search result
    """
    print(f"Searching for {query}")
    return "Tokyo weather is sunny"

llm = ChatOpenAI(model = "gpt-5")
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content="Whats the weather in Tokyo?")})
    print(result)


if __name__ == "__main__":
    main()
