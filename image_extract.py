import requests
from bs4 import BeautifulSoup

def get_image(structured_link):
  try:
    link = structured_link['url']
    geturl = requests.get(link)
    soup = BeautifulSoup(geturl.text, "html.parser")
    images = soup.find_all("img")
    
    page_images = []
    page_logo = []
    for i in images:
      if not(i.get("src").endswith("svg") or i.get("src").count("logo")):
          page_images.append(i["src"])
      if i.get("src").count("logo"):
          page_logo.append(i["src"])
    page_images = list(map( lambda x: x.replace("../", ""), page_images))
    page_logo = list(map( lambda x: x.replace("../", ""), page_logo))


    def set_up_image(x):
      if x.startswith("assets"):
          if link.endswith("/"):
            return f"{link}{x}"
          else:
            return f"{link}/{x}"
      else:
          return x
    page_images = list(map(set_up_image, page_images))
    page_logo = list(map(set_up_image, page_logo))

    from PIL import Image
    working_images = []
    for i in page_images:
      try:
        img = Image.open(requests.get(i, stream=True).raw)
        if img:
          working_images.append(i)
      except:
        pass
    from PIL import Image
    working_logo = []
    for i in page_logo:
      try:
        img = Image.open(requests.get(i, stream=True).raw)
        if img:
          working_logo.append(i)
      except:
        pass
    working_photos = {
      "images": working_images,
      "logo": working_logo
    }
    return working_photos
  except:
    return ""
  