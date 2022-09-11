import requests
import re
from bs4 import BeautifulSoup

URL = "https://derechadiario.com.ar/"
r = requests.get(URL)

soup = BeautifulSoup(r.text, "html.parser")

#print("Los links son:")
#for link in soup.find_all('a'):
    #print(link)

for tag in soup.find_all(href=re.compile("^https://derechadiario.com.ar/latinoamerica/latinoamerica_chile")):
    print(tag['href'])
    x = requests.get(tag['href'])
    soup2 = BeautifulSoup(x.text, "html.parser")
    for para in soup2.find_all("p"):
        print(para.get_text())