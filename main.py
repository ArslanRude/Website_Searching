from image_extract import get_image
from llm_for_json_format import json_format
from website_link_extract import get_link_from_website
from serperdevtool_search import google_search
from flask import Flask,request,jsonify
import concurrent.futures

app = Flask(__name__)

@app.route("/get_data/<params>",methods = ["POST"])
def get_data(params = 1):
    try:
        data = request.json
        links = google_search(f'{data}')
        url = links[0]
        working_images = dict()
        web_other_links = dict()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future1 = executor.submit(get_image,url)
            future2 = executor.submit(get_link_from_website,url) 
            working_images = future1.result()
            web_other_links = future2.result()
        result = json_format(
        data=data,
        working_photos=working_images,
        url=url,
        other_links = web_other_links
        )
        return jsonify(result), 200
    except :
        return jsonify({
            'Error Occure'
        }),300
    
@app.route("/hello")
def hello():
    return 'Hello'


if __name__ == '__main__':
    app.run(debug=True)
    
