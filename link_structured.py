from typing_extensions import TypedDict,Annotated
from langchain_groq import ChatGroq

class Link(TypedDict):
  "Working Website link for the user"
  url : Annotated[str, "The website link dont add ant other string chraracter."]

def structured_link(data):
  llm = ChatGroq(
        temperature=0,
        model_name="mixtral-8x7b-32768",
        api_key="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"
    )
  structured_llm = llm.with_structured_output(Link)
  response = structured_llm.invoke(f'''{data} 
                                   Here is the data extract the website link from it.''')
  return response