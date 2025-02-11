from langchain_groq import ChatGroq 
from langchain_core.prompts import ChatPromptTemplate
from typing_extensions import TypedDict,Annotated
class Format(TypedDict):
    """Result containing Businness data"""
    name: Annotated[str, "Businness name"]
    address: Annotated[str, "Businness address"]
    city: Annotated[str, "Businness city"]
    province: Annotated[str, "Businness province"]
    country: Annotated[str, "Businness country"]

def data_extract(data):
    llm = ChatGroq(temperature=0,model_name="Deepseek-R1-Distill-Llama-70b",api_key="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")
    prompt = ChatPromptTemplate.from_messages(
    [
        ('system','You are a help full AI assistant whos work is to extract name, address, city, province and country from the given data'),
        ('user','{data}')
    ]
    )
    structured_llm = llm.with_structured_output(schema=Format,include_raw=False)
    result = structured_llm.invoke(prompt.invoke(data))
    return result