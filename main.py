from llm_search import get_link
from link_structured import structured_link
from image_extract import get_image
from llm_for_json_format import json_format
from website_link_extract import get_link_from_website
from serpapi_search import google_search
import json

data = '''
                {   
                    \"name\":\"HEART SOLE\",
                    \"address\":\"153 CONCEPTION BAY HWY\",
                    \"city\":\"BAY ROBERTS\",
                    \"province\":\"NL\",
                    \"post_code\":\"A0A 1G0\",
                    \"phone\":\"7097862553\",
                    \"contact_name\":null,
                    \"title\":null,
                    \"employee_count\":\"1 TO 4\",
                    \"employee_code\":\"1\",
                    \"annual_sales\":\"LESS THAN $500,000\",
                    \"sale_code\":\"1\",
                    \"sic_code\":\"569913\",
                    \"industry\":\"SPORTSWEAR-RETAIL\",
                    \"type\":\"apparel\",
                    \"country\":\"canada\",
                }


'''

structured_url = google_search(data)
working_photos = get_image(structured_url)
web_other_links = get_link_from_website(structured_url)
result = json_format(
    data=data,
    working_photos=working_photos,
    url=structured_url,
    other_links = web_other_links
)
print(result)