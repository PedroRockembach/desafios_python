import requests
import os 

os.system("cls")

def verifica_acesso(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            print("Site acessivel!")
            return True
        else:
            print("Site não acessivel")
            return False
        
    except requests.exceptions.RequestException:
        print("Site não acessivel")
        return False     
    
url_site = str(input("digite o url: ")) 

verifica_acesso(url_site)