import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://mexico.globalbajaj.com"
final = pd.DataFrame()
response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")
refs = soup.find_all(class_="btn readmore")
links = []
modelos = []
tipos = []
for ref in refs:
    link = ref.get("href")
    if link.count("/") == 4:
        link = "/".join(link.split("/")[2:])
        links.append(link)
        modelos.append(link.split("/")[-1])
        tipos.append(link.split("/")[-2])
trasera = []
delantera = []
for link in links:
    response = requests.get(url+"/"+link)
    soup = BeautifulSoup(response.content, "lxml")
    caracteristicas = soup.find("h2", text="FRENOS Y LLANTAS")
    caracteristicas = caracteristicas.find_next_sibling("ul").find_all("li")
    for item in caracteristicas:
        item = item.text
        if "Llanta delantera" in item:
            item = item.split(":")[1]
            delantera.append(item)
        elif "Llanta trasera" in item:
            item = item.split(":")[1]
            trasera.append(item)
final["Marca"] = ["Bajaj"]*len(modelos)
final["Tipo"] = tipos
final["Modelos"] = modelos
final["Trasera"] = trasera
final["Delantera"] = delantera
final.to_csv("Bajaj.csv", index=False)
print("Done")