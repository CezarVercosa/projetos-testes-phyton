import requests, os
from pycep_correios import get_address_from_cep, WebService, exceptions #Comando para instalar a biblioteca: pip3 install pycep-correios

def getTemperature(ceparg):
    try:
        os.system("cls")
        address = get_address_from_cep(ceparg, webservice=WebService.APICEP)
        re = requests.get(f"https://weather.contrateumdev.com.br/api/weather/city/?city={address['cidade']}")
        cep = "Cep: " + address["cep"]
        cidade = "Cidade: " + address["cidade"]
        rua = "Rua: " + address["logradouro"]
        bairro ="Bairro: " + address["bairro"]
        temp = f"Temperatura: {round(re.json()['main']['temp'])}ºC".replace('(', "").replace(')', "")
        print(f"{cep}\n{cidade}\n{rua}\n{bairro}\n{temp.replace('(', '').replace(')', '')}")
        return temp 
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
getTemperature("95020-360") #Coloque o cep dentro da string, o uso de hífen é opcional.
