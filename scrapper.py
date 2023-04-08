import requests
from bs4 import BeautifulSoup
from unidecode import unidecode

class Scrapper:
    def __init__(self, string, country, sinons = []):
        self.string = string
        self.country = country
        self.sinons = sinons

        self.get_sinons()

    def get_sinons(self):

        text = unidecode(self.string)
        clean_text = text.replace("ç", "c")

        if self.country == 'br':    
            try:
                page = requests.get("https://www.sinonimos.com.br/" + clean_text)

                soup = BeautifulSoup(page.content, 'html.parser')

                attrs = {"class": "sinonimo"}

                resps = soup.find_all("a", attrs=attrs)

                self.sinons = [resp.text for resp in resps]

            except: 
                print("erro")

        elif self.country == 'us':
            try:
                page = requests.get("https://www.thesaurus.com/browse/" + clean_text)

                soup = BeautifulSoup(page.content, 'html.parser')

                attrs = {"class": "css-1gyuw4i eh475bn0"}

                resps = soup.find_all("a", attrs=attrs)

                self.sinons = [resp.text for resp in resps]
                
            except:
                print("erro")