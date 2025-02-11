from serpapi import GoogleSearch

def google_search(data):
    websites_links = []
    business_data = data
    query = f"{business_data['name']} {business_data['industry']} {business_data['country']}"

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
    links 
    if "organic_results" in results:
        for item in results["organic_results"]:
            links = item.get("link")
            break
    return links
