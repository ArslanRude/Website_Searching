import serpapi

def google_search(data):
    websites_links = []
    business_data = data
    client = serpapi.Client(api_key = 'add2fee9cf6f22f1bb48eda0b42ba9744fd4e990a309f46ffc02adbe51acbf7a')
    query = f"{business_data['name']} {business_data['industry']} {business_data['country']}"
    result = client.search(
    q = query,
    engine = 'google',
    hl = 'en',
    gl = 'ca',
    num = '10',
    )
    for i in result['organic_results']:
        websites_links.append(i['link'])
    return websites_links
