import queue, requests, threading, time, validators
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
# Comandos para instalar as bibliotecas: pip3 install pandas, pip3 install beautifulsoup, pip3 install validators

def searchLinks(q, urls, colecao):
    while 1:
        try:
            url, level = q.get()
        except queue.Empty:
            continue
        if level <= 0:
            break
        try:
            soup = BeautifulSoup(requests.get(url).content, "html.parser")
            for x in soup.find_all("a", href=True):
                link = x["href"]

                if link and link[0] in "#/":
                    link = url + link[1:]
                if link not in colecao:
                    colecao.add(link)
                    urls.append(link)
                    q.put((link, level - 1))
        except (requests.exceptions.InvalidSchema, requests.exceptions.ConnectionError, requests.exceptions.MissingSchema):
            pass

def getLinks(url, depth, filename):
    colecao = set()
    urls = list()
    processos = list()
    fila = queue.Queue()
    fila.put((url, depth+1))
    inicio = time.time()
    for j in range(30):
        t = threading.Thread(target=searchLinks, args=(fila, urls, colecao))
        processos.append(t)
        t.daemon = True
        t.start()
    for thread in processos:
        thread.join()
    linkDict = dict()
    horarioList = list()
    cleanUrl = list(set(urls))
    cleanUrlList = list()
    for i in cleanUrl:
        if validators.url(i):
            horarioList.append(datetime.now().strftime('%H:%M:%S')) 
            cleanUrlList.append(i)
    linkDict["Link"] = cleanUrlList
    linkDict["Horario"] = horarioList
    linkDict["Depth"] = depth
    dados = pd.DataFrame(data= linkDict)
    with pd.ExcelWriter(f"{filename}.xls", engine="openpyxl") as writerXls:
        dados.to_excel(writerXls, sheet_name=f"{filename}.xls", index=False)

    print(f"Encontrado: {len(cleanUrlList)} URLs\n"
        f"Profundidade: {depth}\nEm: {time.time() - inicio:.2f} Segundos")


getLinks("https://dolarhoje.com/", 1, "linkEnttry2")