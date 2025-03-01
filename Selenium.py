
# Selenium, web tarayıcılarını otomatikleştirmek için kullanılan güçlü bir test aracıdır.
# Genellikle web uygulamalarını test etmek ve tarayıcı tabanlı görevleri otomatikleştirmek için kullanılır.
# Selenium, çeşitli programlama dillerinde yazılmış komut dosyaları ile
# web tarayıcılarını kontrol edebilme yeteneği sağlar ve
# Chrome, Firefox, Safari gibi çeşitli tarayıcılarla uyumludur.

# Selenium'un Avantajları
# Çapraz Tarayıcı Desteği: Selenium, birçok popüler web tarayıcısı ile uyumludur.
# Bu, testlerinizi farklı tarayıcılarda çalıştırarak
# uygulamanızın farklı ortamlarda nasıl davrandığını doğrulamanızı sağlar.
#
# Çoklu Programlama Dili Desteği: Selenium, Java, Python, C#, Ruby ve JavaScript
# gibi birçok programlama dili ile kullanılabilir.
# Bu esneklik, farklı programlama dillerini tercih eden geliştiriciler için büyük bir avantajdır.
#
# Dağıtık Test İmkanı: Selenium Grid ile testlerinizi paralel olarak
# birden fazla makinede çalıştırabilirsiniz.
# Bu, test süresini önemli ölçüde azaltır ve daha geniş kapsamlı testler yapmanıza olanak tanır.
#
# Açık Kaynak: Selenium açık kaynak kodlu bir araçtır ve ücretsizdir.
# Bu, küçük işletmeler ve bağımsız geliştiriciler için maliyet açısından büyük bir avantaj sağlar.

################
# Main  (This file is only for initializing driver)
################
# Önce terminalde conda install selenium ile selenium paketini yükle envda


from selenium import webdriver
driver = webdriver.Chrome()       # Chrome tarayıcısını başlatır ve kodun geri kalanında bu tarayıcıyı kontrol etmek için kullanılır.
driver.get("https://www.example.com")         # herhangi sayfayı açmak için
driver.title                                  # driver'ın title attribute'sini getirir
driver.current_url                            # driver'ın açık url'sini getirir
driver.quit()                                 # driver kapatılır

# Initialize Driver
options = webdriver.ChromeOptions()            # driver'ımız farklı seçeneklerle açılır
options.add_argument("--start-maximized")      # driveri full ekran acsin
driver = webdriver.Chrome(options)
driver.get("https://miuul.com/")



#########################################
# Finding Elements and Extracting Data
#########################################

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# .find_element metodu ile element bulunur
# İlk argümanı: elementi hangi yolla bulacağımız;
# ikinci argüman: hangi elementi bulacaksan onu bulduran sorguyu yazıyoruz
element = driver.find_element(By.XPATH, "//a")
element
element.text
element.get_attribute("innerHTML")



#########################################
# Finding Elements (Better Approach)
#########################################

from selenium import webdriver
from selenium.webdriver.common.by import By

import time


driver = webdriver.Chrome()
driver.get("https://www.example.com")
time.sleep(5)
h1_elem = driver.find_element(By.XPATH, "//h1")
a_elem = driver.find_element(By.XPATH, "//a")
p_elem = driver.find_element(By.XPATH, "//p")
#.....
#.....
#.....


p_elements = driver.find_elements(By.XPATH, "//p")
p_elements

elem = None
if p_elements:
    elem = p_elements[0]
else:
    print("Element not found")

print(elem)



##################################
# Interacting with Elements
##################################
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.miuul.com")
time.sleep(2)

btn_elements = driver.find_elements(By.XPATH, "//a[@id='login']")   # giriş yap butonunu çeker
btn = btn_elements[0]
btn.click()             # click() ile butona tıkla

inputs = driver.find_elements(By.XPATH, "//input[@name='arama']")   # arama butonunu çeker
input = inputs[0]
input.send_keys("Data Science", Keys.ENTER)     # element içine yazı yazmak için .send_keys() metodu kullanılır
# içerisine "Data Science" yaz ve Keys.ENTER ile entere bas



##############################################
# Scrolling and Scrolling Inside Dropdown
##############################################
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)
driver.get("https://miuul.com/katalog")
time.sleep(2)

dropdown_button = driver.find_elements(By.XPATH, "//a[@data-bs-toggle='dropdown']")[1]
dropdown_button.click()
time.sleep(0.5)
ul_element = driver.find_elements(By.XPATH, "//ul[@aria-labelledby='navbarDropdown']")[1]
driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", ul_element, "overflow: scroll; height:80px;")

driver.execute_script("arguments[0].focus();", ul_element)
from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(driver)
actions.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(0.25)
actions.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(0.25)
actions.send_keys(Keys.ARROW_DOWN).perform()



######################
# Pagination
######################
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Initialize Driver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)
driver.get("https://learning.miuul.com/enrollments")

course_titles = []
for i in range(1,999):
    driver.get(f"https://learning.miuul.com/enrollments?page={i}")
    time.sleep(3)
    # Get Course Titles Per Page
    course_elements = driver.find_elements(By.XPATH, "//ul//h3")
    if not course_elements:                 # len(course_elements) <= 0
        break
    for course in course_elements:
        title = course.get_attribute("innerText")
        course_titles.append(title)

print(course_titles)
print(len(course_titles))