from image_extract import get_image
from llm_for_json_format import json_format
from website_link_extract import get_link_from_website
from serpapi_search import google_search
from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/get_data/<params>",methods = ["POST"])
def get_data(params):
    data = request.json
    url = google_search(f'{data}')
    if url:
        working_images = get_image(url)
        web_other_links = get_link_from_website(url)
        result = json_format(
        data=data,
        working_photos=working_images,
        url=url,
        other_links = web_other_links
        )
        return jsonify(result), 200
    else:
        return jsonify(url),300

if __name__ == '__main__':
    app.run(debug=True)





# working_photos = get_image(structured_url)
# web_other_links = get_link_from_website(structured_url)
# result = json_format(
#     data=data,
#     working_photos=working_photos,
#     url=structured_url,
#     other_links = web_other_links
# )






# ----------------------------------------------------------------------------------------------------------------
# data = '''
# {
#     "name": "Xelent Solution",
#     "address": "p 58 Usman town",
#     "city": "Faisalabad",
#     "province": "Punjab",
#     "post_code": "38000",
#     "phone": "+92 300 1076788",
#     "contact_name": null,
#     "title": null,
#     "employee_count": "1 TO 20",
#     "website": "xelent.pk",
#     "employee_code": "1",
#     "annual_sales": "LESS THAN $500,000",
#     "sale_code": "1",
#     "sic_code": null,
#     "industry": "Software House",
#     "type": "apparel",
#     "country": "pakistan"
# }

# '''

# url = google_search(data)
# print(url)