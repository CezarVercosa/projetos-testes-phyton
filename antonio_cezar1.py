import requests, os, json
from bs4 import BeautifulSoup #Comando para instalar a biblioteca: pip3 install beatifulsoup


def getMetas(url):
    try:
        os.system('cls')
        re = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        if re.status_code != 200:
            return "Erro ao Estabelecer Conexão Com o Site"
        else:
            soup = BeautifulSoup(re.content, "html.parser")
            meta = soup.find_all("meta")
            metaTagsList = list()
            MetaTagsDict = dict()
            MetaTagsDict2 = dict()
            MetaTagsDict2["tags"] = metaTagsList 
            for tags in meta:
                MetaTagsDict.clear()
                tagName = tags.get("name")
                tagContent = tags.get("content")
                if tagName == None:
                    tagName = "Meta Tag Sem Nome"
                if tagContent == None:
                    tagName = "Meta Tag Sem Conteúdo"
                MetaTagsDict["Nome"] = tagName
                MetaTagsDict["Conteudo"] = tagContent
                metaTagsList.append(MetaTagsDict.copy())
            return json.dumps(MetaTagsDict2,indent=1, ensure_ascii=False)
    except Exception as ex:
        return "Erro ao Acessar o Site.", ex

metaTags = getMetas("https://enttry.com.br/contato") #Coloque o URL dentro da string
print(metaTags)