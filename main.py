from image_extract import get_image
from llm_for_json_format import json_format
from website_link_extract import get_link_from_website
from serpapi_search import google_search

data = input("Enter Data : ")


structured_url = google_search(data)
if structured_url['found']:
    working_photos = get_image(structured_url)
    web_other_links = get_link_from_website(structured_url)
    result = json_format(
        data=data,
        working_photos=working_photos,
        url=structured_url,
        other_links = web_other_links
    )