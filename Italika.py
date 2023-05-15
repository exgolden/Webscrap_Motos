# Inicializacion
import requests
import pandas as pd
from bs4 import BeautifulSoup

#Extraccion
Tipos=["Trabajo", "Motoneta", "LineaZ", "Deportiva", "DobleProposito", "Chopper", "Adventure", "VortX", "CafeRacer", "Crossover"]
final = pd.DataFrame()
for tipo in Tipos:
    url = "https://www.italika.mx/Modelos/"+tipo
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    list_items = soup.find_all("li")
    modelos = []
    for li in list_items:
        h3s = li.find_all("h3")
        for h3 in h3s:
            modelos.append(h3.text)
    df = pd.DataFrame()
    df["Marca"] = ["Italika"]*len(modelos)
    df["Tipo"] = [tipo]*len(modelos)
    df["Modelos"] = modelos
    trasera = []
    delantera = []
    for model in modelos:
        response = requests.get(url+"/"+model+"/")
        soup = BeautifulSoup(response.content, "lxml")
        delantera.append(soup.find('td', text='Llanta delantera').find_next_sibling(class_="lastChild").text)
        trasera.append(soup.find('td', text='Llanta trasera').find_next_sibling(class_="lastChild").text)
    df["Trasera"] = trasera
    df["Delantera"] = delantera
    final = pd.concat([final, df])
final.to_csv("Italika.csv", index=False)
print("Done")