from bs4 import BeautifulSoup
import requests

def rastrear(url):
    html =requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')

    datos = {}
    datos["producto"] = soup.find("h1",class_="ui-pdp-title").get_text()
    datos["precio"] = soup.find("span",class_="price-tag-fraction").get_text()
    datos["diponibles"] = soup.find("span",class_="ui-pdp-buybox__quantity__available").get_text()
    datos["msi"] = soup.find("div",class_="ui-pdp-price__subtitles").get_text()

    return datos

def imprimir(dicc):
    for x,y in dicc.items():
        print(x,y)
    print("")

if __name__ == '__main__':
    laptop = rastrear("https://www.mercadolibre.com.mx/laptop-dell-inspiron-3505-gris-156-amd-ryzen-5-3450u-8gb-de-ram-256gb-ssd-amd-radeon-vega-8-60-hz-1366x768px-windows-10-home/p/MLM16537306?pdp_filters=category:MLM1652#searchVariation=MLM16537306&position=2&search_layout=stack&type=product&tracking_id=8defb765-9e97-4fe3-922a-be9e9b0fa052")
    imprimir(laptop)