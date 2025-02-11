import requests
from bs4 import BeautifulSoup

def get_link_from_website(link):
    try:
        geturl = requests.get(link)
        soup = BeautifulSoup(geturl.text, "html.parser")
        footer = soup.find("footer")
        links = [a['href'] for a in footer.find_all('a', href=True)]
        links_from_website = {'linkedin_url':'',
                        'facebook_url':'',
                        'twitter_url':'',
                        'youtube_url':'',
                        'email' : '',
                        }
        for i in links:
            if i.count('linkedin.'):
                links_from_website['linkedin_url'] = i
            if i.count('facebook.'):
                links_from_website['facebook_url'] = i
            if (i.count('twitter.') or i.count('x.')):
                links_from_website['twitter_url'] = i
            if i.count('youtube.'):
                links_from_website['youtube_url'] = i
            if i.count('@'):
                links_from_website['email'] = i
        return links_from_website
    except:
        return ""
