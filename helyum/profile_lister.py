import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

# main page
url = "https://www.behance.net/search/projects?field=photography&sort=appreciations&country=AR&time=week"
r = requests.get(url)
data = r.text

soup = BeautifulSoup(data, "html5lib")
text = soup.find_all("a", href=True)

# profile opener
def url_finder(div, class_name):
    return soup.find_all(div, {"class": class_name})
pattern = re.compile('https://www.behance(?:[^"])*')  # regex for profile urls
urls = [
    re.findall(pattern, str(i))
    for i in url_finder("a", "Owners-owner-EEG e2e-Owner-user-link")
