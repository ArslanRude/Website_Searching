from langchain.chat_models import init_chat_model
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage
from langchain_core.tools import Tool

def get_link(data):
    llm = init_chat_model(model="Deepseek-R1-Distill-Llama-70b",
                          temperature=.666,
                          api_key="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",
                          model_provider="groq")

    search = SerpAPIWrapper(serpapi_api_key="add2fee9cf6f22f1bb48eda0b42ba9744fd4e990a309f46ffc02adbe51acbf7a")
    tools = Tool(
        name= "search",
        func= search.run,
        description = "Useful for when you need to answer questions about current events or search the internet"
    )
    tools = [tools]

    system_prompt = """You are a helpful AI assistant that can search the internet. 
    Process the provided JSON input and use the internet search for fet the website link. 
    Use the search tool for any queries requiring up-to-date information, website details, 
    or online resources. Return the website link that should work properly.
    Note:Don't give me dummy link."""

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ])

    agent = create_tool_calling_agent(llm, tools, prompt ,)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True,)

    def process_json_input(json_data):
        """
        Process JSON input and execute the agent
        Example json_data format:
        {
            "query": "Find recent articles about AI advancements",
            "parameters": {
                "max_results": 5,
                "time_period": "past month"
            }
        }
        """
        try:

            query = json_data.get("query", "")
            parameters = json_data.get("parameters", {})
            

            input_msg = HumanMessage(content=f"Search query: {query}\nParameters: {parameters}")
            

            result = agent_executor.invoke({
                "input": input_msg,
                "chat_history": []
            })
            
            return result["output"]
        
        except Exception as e:
            return f"Error processing request: {str(e)}"
    response = process_json_input({
        "query": f''' {data}
    Here is the data of website in json format, now your job is to read the data carefully and search the website on the internet according to the data and give me the link of the website, website should be work properly, dont give me dummy link
''',
        "parameters": {
            "max_results": 1,
        }
    })
    return response

