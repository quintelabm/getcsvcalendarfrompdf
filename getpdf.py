import requests
from bs4 import BeautifulSoup
import os.path


# get the pdf from propp ufjf
url = 'https://www2.ufjf.br/propp/pesquisa/'

response = requests.get(url)

# parse html
page = str(BeautifulSoup(response.content,features="html.parser"))

def getURL(page):
    """

    :param page: html of web page (here: Python home page) 
    :return: urls in that page 
    """
    start_link = page.find("a href")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote

def getpdfurl(str,page):
    while True:
        url, n = getURL(page)
        page = page[n:]
        if url:
            #print(url)
            if str  in url:
                break
        else:
            break
    return url

def downloadpdf():
    print('------------------------------')
    print('Acessing url...')
    if not os.path.isfile('calendario.pdf'):
        # download and save the pdf
        response = requests.get(getpdfurl('RIO-DE-BOLSAS-',page))

        with open('calendario.pdf', 'wb') as f:
            f.write(response.content)
            
        print('------------------------------')
        print('PDF downloaded... wait...')
        print('------------------------------')
    else:
        print('File already downloaded.')
        print('Nothing else to do :)')
        print('------------------------------')