import requests
from bs4 import BeautifulSoup
url = "https://github.com/leijingxing/python-project"
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
soup.title
