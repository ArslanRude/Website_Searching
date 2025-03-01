from data_extract import data_extract
import http.client
import json


def google_search(data):
    try:
        query = data_extract(data)
        conn = http.client.HTTPSConnection("google.serper.dev")
        payload = json.dumps({
        "q": f'''{query['name']} -inurl:facebook.com -inurl:linkedin.com -inurl:instagram.com -inurl:twitter.com -inurl:x.com'''
        })
        headers = {
        'X-API-KEY': '4cd45d1da1d32811c599c80ae57bfdd0faaf3e39',
        'Content-Type': 'application/json'
        }
        conn.request("POST", "/search", payload, headers)
        res = conn.getresponse()
        data = res.read()
        links = []
        search_results = json.loads(data.decode('utf-8'))
        for link in search_results.get('organic'):
            links.append(link.get('link'))
        return links
    except:
        return {'url':"Error occur while fetching Link from Google.",
                'found':False}
