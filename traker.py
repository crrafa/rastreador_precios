from bs4 import BeautifulSoup
import requests


url = "https://www.mercadolibre.com.mx/laptop-lenovo-ideapad-14igl05-ice-blue-14-intel-pentium-silver-n5030-4gb-de-ram-128gb-ssd-intel-uhd-graphics-605-1366x768px-windows-10-home/p/MLM16029714?pdp_filters=category:MLM1652#searchVariation=MLM16029714&position=1&search_layout=stack&type=product&tracking_id=602e052f-3a94-46f2-a689-d34b79167772"
html =requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')

datos = {}
datos["producto"] = soup.find("h1",class_="ui-pdp-title").get_text()
datos["precio"] = soup.find("span",class_="price-tag-fraction").get_text()
datos["diponibles"] = soup.find("span",class_="ui-pdp-buybox__quantity__available").get_text()
datos["msi"] = soup.find("div",class_="ui-pdp-price__subtitles").get_text()

print(datos)