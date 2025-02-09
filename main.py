from llm_search import get_link
from link_structured import structured_link
from image_extract import get_image
from llm_for_json_format import json_format

data = '''
        [
        {
            \"id\": 8608,
            \"name\": \"Xelent Solution\",
            \"address\": \"p 58 Usman town\",
            \"city\": \"Faisalabad\",
            \"province\": \"Punjab\",
            \"post_code\": \"38000\",
            \"phone\": \"+92 300 1076788\",
            \"contact_name\": null,
            \"title\": null,
            \"employee_count\": \"1 TO 20\",
            \"employee_code\": \"1\",
            \"annual_sales\": \"LESS THAN $500,000\",
            \"sale_code\": \"1\",
            \"sic_code\": null,
            \"industry\": \"Software House\",
            \"type\": \"apparel\",
            \"country\": \"pakistan\",
        }
    ]
'''

raw_url = get_link(data)
structured_url = structured_link(raw_url)
working_photos = get_image(structured_url)
result = json_format(data=input,working_photos=working_photos,url=structured_url)
print(result) 
 


