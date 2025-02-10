from typing_extensions import TypedDict,Annotated
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", 
     """You are a link extraction assistant. Analyze the input data and return:
     - 'found': True/False if a valid URL exists
     - 'url': The first working URL found (or empty string if none)
     Return JSON format with these keys ONLY."""),
    ("user", "Input data: {input}")
])

class LinkResult(TypedDict):
    """Result containing URL information"""
    url: Annotated[str, "The working website link if found"]
    found: Annotated[bool, "Whether a valid link was found"]

def structured_link(data):
  llm = ChatGroq(
        temperature=0,
        model_name="Deepseek-R1-Distill-Llama-70b",
        api_key="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"
    )
  structured_llm = llm.with_structured_output(
    schema=LinkResult,
    method="json_mode",
    include_raw=False
    )
  response = structured_llm.invoke(prompt.invoke(input=data))
  return response