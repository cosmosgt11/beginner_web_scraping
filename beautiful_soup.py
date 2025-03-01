
from bs4 import BeautifulSoup

# örnek bir HTML
html = """
        <!DOCTYPE html><html><head><title>Example HTML</title></head><body><h1>Hello, World!</h1><p>A simple HTML page for testing web scraping with BeautifulSoup.</p>
                <a class='link' href='www.miuul.com' target='blank' aria-label='Miuul (Opens Miuul Page)'>Click</a>
                <li>Outsider</li>
                <ul>
                    <li>Item 1</li>
                    <li>Item 2</li>
                </ul>
            </body>
            </html>
"""

soup = BeautifulSoup(html, "html.parser")
# ilk argüman içeriğin konumunu; ikinci argüman html üzerinde işlem yapılacağını belirtir
# İkinci argümanın veriliş nedeni: beautifulsoup'un hem HTML hem de XML üzerinde işlem yapabilmesi

title = soup.title
type(title)
title.text
title.string

print(soup.prettify())   # HTML'in daha düzenli görülmesini sağlar

ul = soup.ul       # ul içerisindeki listeyi çeker
ul.li              # ul içerisindeki li elementini çağır



#################################
# Navigating and Searching HTML
#################################


html = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>Example HTML</title>
            </head>
            <body>
                <h1>Hello, World!</h1>
                <p id="paragraph" >A simple HTML page for testing web scraping with BeautifulSoup.</p>
                <a class='link' href='www.miuul.com' target='blank' aria-label='Miuul (Opens Miuul Page)'>Click</a>
                <li>Outsider</li>
                <ul>
                    <li class="list-item">Item 1</li>
                    <li class="list-item">Item 2</li>
                </ul>
                <li>Outsider 2</li>
            </body>
            </html>
"""
soup = BeautifulSoup(html, "html.parser")

soup.a    # döküman içerisindeki ilk a'yı bulur

soup.find("a", attrs={"class": "link", "target": "blank"})   # attribute'larından class'ı link olan a'yı bul

soup.find_all("li")     # bir liste içerisinde bütün li- leri getirir

li_elements = soup.find_all("li", attrs={"class": "list-item"})  # birden fazla li bulunacağı için böyle _all kullandık
li_elements[-1]



#######################################
# Extracting Data from HTML Elements
#######################################

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Animal Table</title>
  <style>
    table {
      width: 80%;
      border-collapse: collapse;
      margin: 20px;
    }

    th, td {
      border: 1px solid #dddddd;
      text-align: left;
      padding: 8px;
    }

    th {
      background-color: #f2f2f2;
    }

    img {
object-fit: cover;
      max-width: 50px;
      max-height: 50px;
    }
  </style>
</head>
<body>

  <h2>Animal Table</h2>

  <table>
    <thead><tr>
      <th>Image</th>
      <th>Animal</th>
      <th>Description</th>
      <th>Nickname</th>
    </tr></thead>
    <tbody>
    <tr>
      <td><img src="https://images.unsplash.com/photo-1534188753412-3e26d0d618d6?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Lion"></td>
      <td><a href="https://en.wikipedia.org/wiki/Lion" target="_blank">Lion</a></td>
      <td>The lion is a large carnivorous mammal. It is known for its majestic appearance and is often referred to as the "king of the jungle."</td>
      <td> Majestic<br>King  </td>
    </tr>
    <tr>
      <td><img src="https://images.unsplash.com/photo-1551316679-9c6ae9dec224?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Elephant"></td>
      <td><a href="https://en.wikipedia.org/wiki/Elephant" target="_blank">Elephant</a></td>
      <td>Elephants are the largest land animals. They are known for their long trunks and large ears.</td>
      <td> Trunked<br>  Giant</td>
    </tr>
    <tr>
      <td><img src="https://images.unsplash.com/photo-1570481662006-a3a1374699e8?q=80&w=1965&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Dolphin"></td>
      <td><a href="https://en.wikipedia.org/wiki/Dolphin" target="_blank">Dolphin</a></td>
      <td>Dolphins are highly intelligent marine mammals known for their playful behavior and communication skills.</td>
      <td> Playful<br>Communicator</td>
    </tr>
    <tr>
      <td><img src="https://images.unsplash.com/photo-1599631438215-75bc2640feb8?q=80&w=2127&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Butterfly"></td>
      <td><a href="https://en.wikipedia.org/wiki/Butterfly" target="_blank">Butterfly</a></td>
      <td>Butterflies are beautiful insects with colorful wings. They undergo a process called metamorphosis from caterpillar to butterfly.</td>
      <td> Colorful<br>Metamorphosis</td>
    </tr>
    <tr>
      <td><img src="https://images.unsplash.com/photo-1552633832-4f5a1b110980?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Penguin"></td>
      <td><a href="https://en.wikipedia.org/wiki/Penguin" target="_blank">Penguin</a></td>
      <td>Penguins are flightless birds that are well-adapted to life in the water. They are known for their tuxedo-like black and white plumage.</td>
      <td> Tuxedoed     <br>Adaptation  </td>
    </tr>
  </tbody>
  </table>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

tbody_tag = soup.find("tbody")
tr_tag_list = tbody_tag.find_all("tr")
print(tr_tag_list)

# ilkinin
tr_tag = tr_tag_list[0]
tr_tag

img_tag = tr_tag.find("img")
a_tag = tr_tag.find("a")
nickname_td = tr_tag.find_all("td")[-1]
desc_td = tr_tag.find_all("td")[-2]
desc_td.text

nickname_td.text
nickname_td.get_text(separator=" ", strip=True)  # strip -> önce kelimelerin sağındaki ve solundaki boşlukları silerim
# sonra separator -> kelimelerin arasında x olacak şekilde düzenlerim.


img_tag
alt_attr = img_tag["alt"]     # attribute ismi değiştirme
alt_attr

src_attr = img_tag["src"]
src_attr

a_tag
a_tag["href"]
a_tag["target"]



#######################################
# Scraping a Web Page
#######################################

import requests
from bs4 import BeautifulSoup

requests.get("https://www.example.com")
# İşleminin sonucu <Response [200]> basarsa istek olumludur.

result = requests.get("https://www.example.com")   # bir web sayfasından istek yapma
result.status_code       # status kodunu getirir, 200 ise olumlu

html = result.content                               # sayfanın içeriği olan html'i alma

soup = BeautifulSoup(html, "html.parser")
soup.find("h1").text
