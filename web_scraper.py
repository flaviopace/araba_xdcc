import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool

def f(x):
    return x*x



base_url = 'http://www.lista.arabaphenix.it/'

def parseHTML(number):
    vgm_url =  base_url + str(number) + ".php"
    #print("Scraping {}".format(vgm_url))
    html_text = requests.get(vgm_url).text
    soup = BeautifulSoup(html_text, 'html.parser')

    if soup:
        if soup.find_all("div", {"id" : 'container_vetrina'}):
            print("List Can be found here: {}".format(vgm_url))


if __name__ == '__main__':
    with Pool(50) as p:
        p.map(parseHTML, range(1,9000))
    print("Scan complete")