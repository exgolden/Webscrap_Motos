import requests
from bs4 import BeautifulSoup

response = requests.get("https://mexico.globalbajaj.com/Brands/Pulsar/Pulsar-N-250")
soup = BeautifulSoup(response.content, "lxml")
caracteristicas = soup.find("h2", text="FRENOS Y LLANTAS")
caracteristicas = caracteristicas.find_next_sibling("ul").find_all("li")
trasera = []
delantera = []
for item in caracteristicas:
    item = item.text
    if "Llanta delantera" in item:
        item = item.split(":")[1]
        delantera.append(item)
    elif "Llanta trasera" in item:
        item = item.split(":")[1]
        trasera.append(item)

# print(delantera)
# print(trasera)
