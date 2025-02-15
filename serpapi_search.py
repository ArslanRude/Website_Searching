from serpapi import GoogleSearch
from data_extract import data_extract

def google_search(data):
    try:
        business_data = data_extract(data)
        query = f"{business_data['name']} {business_data['industry']} {business_data['country'] } -inurl:facebook.com -inurl:linkedin.com -inurl:instagram.com -inurl:twitter.com -inurl:x.com"

        params = {
            'q' : query,
            'engine' : 'google',
            'hl' : 'en',
            'gl' : 'ca',
            'num' : '10',
            'api_key' : 'add2fee9cf6f22f1bb48eda0b42ba9744fd4e990a309f46ffc02adbe51acbf7a'
        }

        client = GoogleSearch(params)
        
        results = client.get_dict()
        link = {'url':results['organic_results'][0]['link'],
        'found':True}
        return link
    except:
        return {'url':"Error occur while fetching Link from Google.",
                'found':False}
