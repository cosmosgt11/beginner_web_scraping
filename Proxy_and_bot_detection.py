# "Headers" (başlıklar), HTTP (Hypertext Transfer Protocol) iletişimi sırasında sunucu
# ve istemci (örneğin, web tarayıcınız ve web sunucusu) arasında ek bilgi ileten veri parçalarıdır.
# Başlıklar, bir HTTP isteği (request) veya HTTP cevabı (response) içinde yer alabilir ve genellikle metin tabanlıdır.
# İşte temel başlık türlerine ve kullanım alanlarına dair ayrıntılar:

# HTTP İstek Başlıkları (Request Headers)
# HTTP istek başlıkları, istemcinin (örneğin, tarayıcınız) bir sunucuya gönderdiği istekte ek bilgi sağlar.
# Bazı yaygın istek başlıkları şunlardır:
# User-Agent: İstemcinin yazılım türünü ve sürümünü tanımlar.
# Accept: İstemcinin kabul edebileceği içerik türlerini belirtir.
# Host: Hedef sunucuya ait alan adını belirtir.
# Authorization: İstemcinin kimliğini doğrulamak için kimlik bilgilerini gönderir.

# Proxy, internet trafiğini bir cihaz ile internet arasında yönlendiren bir ara sunucudur.
# Proxy sunucuları, kullanıcıların internete bağlanırken anonim kalmalarına,
# erişim kısıtlamalarını aşmalarına ve ağ performansını artırmalarına yardımcı olabilir.



#########################################
# Using Proxy with Beautiful Soup
#########################################

import requests
from bs4 import BeautifulSoup

url = 'https://www.ipaddress.my/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7",
    "Accept-Language": "en-US,en;q=0.5"
}
proxies = {
    #username:password@ip_address:port
    "http": 'http://JX2kX2Gf:eWKNTTTF@216.19.205.244:6565',
    "https": 'http://JX2kX2Gf:eWKNTTTF@216.19.205.244:6565',
}

response = requests.get(url,  headers=headers, proxies=proxies)
response.status_code

soup = BeautifulSoup(response.content, 'html.parser')
ip_address_element = soup.find("div", attrs={"class":"panel-body"}).find("li").find("span")
flag_element = soup.find("div", attrs={"class":"panel-body"}).find_all("li")[-1].find("img")
ip_address = ip_address_element.text
flag = flag_element["alt"]

print(ip_address)
print(flag)



#########################################
# Using Proxy with Selenium
#########################################

import requests
from selenium import webdriver
from extension import proxies

url = 'https://www.ipaddress.my/'

proxy_username = 'JX2kX2Gf'
proxy_password = 'eWKNTTTF'
proxy_ip_address = '104.239.108.144'
proxy_port = '6379'

# username:password@ip_address:port
options = webdriver.ChromeOptions()
# options.add_argument(f'--proxy-server={proxy_ip_address}:{proxy_port}')

proxies_extension_path = proxies(proxy_username, proxy_password, proxy_ip_address, proxy_port)
options.add_extension(proxies_extension_path)
# selenium-wire

driver = webdriver.Chrome(options=options)
driver.get(url)



######################################################
# Using undetected-chromedriver to Pass Bot Tests
######################################################
import undetected_chromedriver as uc
# pip install undetected_chromedriver
from selenium import webdriver

url = "https://bot.sannysoft.com"

driver = uc.Chrome()    # bu şekilde yeni bir chrome tarayıcısı oluşturulur
with driver:
    driver.get(url)      # driver ile bu sayfayı aç