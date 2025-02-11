import requests
from bs4 import BeautifulSoup

def get_link_from_website(link):
    try:
        geturl = requests.get(link)
        soup = BeautifulSoup(geturl.text, "html.parser")
        footer = soup.find("footer")
        links = [a['href'] for a in footer.find_all('a', href=True)]
        links_from_website = {'linkedin_url':{'url' : '','found': False},
                        'facebook_url':{'url' : '','found': False},
                        'twitter_url':{'url' : '','found': False},
                        'youtube_url':{'url' : '','found': False},
                        'email' : {'url' : '','found': False},
                        }
        for i in links:
            if i.count('linkedin.'):
                links_from_website['linkedin_url']['url'] = i
                links_from_website['linkedin_url']['found'] = True
            if i.count('facebook.'):
                links_from_website['facebook_url']['url'] = i
                links_from_website['facebook_url']['found'] = True
            if (i.count('twitter.') or i.count('x.')):
                links_from_website['twitter_url']['url'] = i
                links_from_website['twitter_url']['found'] = True
            if i.count('youtube.'):
                links_from_website['youtube_url']['url'] = i
                links_from_website['youtube_url']['found'] = True
            if i.count('@'):
                links_from_website['email']['url'] = i
                links_from_website['email']['found'] = True
        return links_from_website
    except:
        return ""
