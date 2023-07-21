""" A placeholder docstring"""

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://help.ivanti.com/iv/help/en_US/isec/API/Topics/"

page = requests.get(BASE_URL + "Welcome.htm")

#print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

links = list(soup.find_all('a'))

endpoints = []

for link in links:
    href = link.get("href")
    if href not in ["http://www.ivanti.com/en-US/company/legal", "#",None]:
        #print("|"+href+"|")
        endpoints.append(href)
output = []
for endpoint_url in endpoints:
    try:

        url = BASE_URL + endpoint_url
        #print(url)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        endpoint_base_url = soup.find('pre', {'class': 'prettyprint'}).text
        #print(endpoint_base_url)
        if "\n" in endpoint_base_url:
            for el in endpoint_base_url.split():
                output.append(el.strip())
        else:
            output.append(endpoint_base_url.strip())
    except AttributeError:
        print("attempted item endpoint_url")

with open('base_urls.txt','w+') as f:
    for url in sorted(output,key=lambda x: x.split('v1.0/')[-1]):
        print(url)
        f.write(f'{url}\n')
