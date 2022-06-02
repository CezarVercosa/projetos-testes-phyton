import requests
from pycep_correios import get_address_from_cep, WebService, exceptions # Comando para instalar a biblioteca: pip install pycep-correios

cep = str(input("Digite seu cep: "))
def getTemperature(ceparg):
    try:
        address = get_address_from_cep(cep, webservice=WebService.APICEP)
        re = requests.get(f"https://weather.contrateumdev.com.br/api/weather/city/?city={address['cidade']}")
        print("CEP: ", address["cep"])
        print("Cidade: ", address["cidade"])
        print("Rua: ", address["logradouro"])
        print("Bairro: ", address["bairro"])
        print("Temperatura: ", round(re.json()['main']['temp']),"ºC")
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
getTemperature(cep)

