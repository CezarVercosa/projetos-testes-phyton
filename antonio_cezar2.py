import requests, os
from pycep_correios import get_address_from_cep, WebService, exceptions # Comando para instalar a biblioteca: pip install pycep-correios

cep = str(input("Digite seu cep: "))
def getTemperature(ceparg):
    try:
        address = get_address_from_cep(ceparg, webservice=WebService.APICEP)
        re = requests.get(f"https://weather.contrateumdev.com.br/api/weather/city/?city={address['cidade']}")
        cep = "Cep: " + address["cep"]
        cidade = "Cidade: " + address["cidade"]
        rua = "Rua: " + address["logradouro"]
        bairro ="Bairro: " + address["bairro"]
        temp = f"Temperatura: {round(re.json()['main']['temp'])}"
        return cep, cidade, rua, bairro, str(temp).replace('(', "").replace(')', "") + "ºC"
    except exceptions.InvalidCEP as eic:
        print("Cep Invalido.")

    except exceptions.CEPNotFound as ecnf:
        print("Cep não encontrado.")

    except exceptions.ConnectionError as errc:
        print("Erro de conexão.")

    except exceptions.Timeout as errt:
        print("Tempo de conexão excedido.")

    except exceptions.HTTPError as errh:
        print("Erro de solicitação.")

    except exceptions.BaseException as e:
        print("Formato do cep invalido, digite somente números.")    
temp = getTemperature(cep)
os.system("cls")
for i in temp:
    print(i)

