from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

def json_format(working_photos,data,url,other_links):
    llm = ChatGroq(temperature=0.6, model_name="Deepseek-R1-Distill-Llama-70b", api_key="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")
    response = llm.invoke(f'''
    message = "Extract the following details for each business in the given JSON list:
                1- A short description (max 30 words)
                2- A long description (max 300 words)
                3- Relevant tags/keywords (comma-separated)
                4- {working_photos} A list of logo URLs related to the business use only one of these link in logo url
                5- {working_photos} A list of images URLs related to the business use only three of these these link in images link
                6- {url} Use this link in website link
                7- {other_links['facebook_url']} if link found write it in facebook / if not found write facebook.com
                8- {other_links['twitter_url']} if link found write it in twitter / if not found write twitter.com
                9- {other_links['youtube_url']} if link found write it in youtube / if not found write youtube.com.com
                10- {other_links['linkedin_url']} if link found write it in linkedin / if not found write linkedin.com
                10- {other_links['email']} if email found write it in email / if not found write example@.com

                Here is the business data:
                {data}
                Return the result in the following structured JSON format and no other thing will be print in response:
                {{
                    "businesses\": [
                        {{
                            "id\": \"\",
                            "name\": \"\",
                            "short_description\": \"\",
                            "long_description\": \"\",
                            "tags\": \"\",
                            "logo_url\": \"\",
                            "image_links\": [\"\", \"\", \"\"],
                            "website\": \"\"
                            "facebook\": \"\",
                            "twitter\": \"\",
                            "youtube\": \"\",
                            "linkedin\": \"\",
                            "email\": \"\"
                        }}
                    ]
                }}";
    '''
    )
    parse = JsonOutputParser()
    prompt = PromptTemplate(
        template="Answer the user query.\n{format_instructions}\n{query}\n",
        input_variables=["query"],
        partial_variables={"format_instructions": parse.get_format_instructions()},
    )
    chain = prompt | llm | parse
    result = chain.invoke({"query": response})
    return result

                