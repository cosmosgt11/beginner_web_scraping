# XPATH ve CSS en sık kullanılan metodlardır.

# CSS Selectors:
# CSS Seçiciler, web sayfalarındaki HTML ögelerini seçmek ve stil uygulamak için kullanılan bir yöntemdir.

# Web kazımada kullanılan CSS Seçiciler:
# Ögeleri adlarına, id’lerine veya class’larına göre segmek icin kullanılırlar.
# Örneğin: id'si main olan div'i bul ---> div#main
# NOT: id => #  ve  class => . (nokta) kullanılır.

# Simple Selectors:
# Ögeleri adlarına, id’lerine veya class’larına göre seçmek icin kullanılırlar.

# Combinator Selectors:
# Elementleri diğer elementlerle olan özel ilişkilerine (div içerisindeki p <- div p) göre seçmek için kullanılırlar
# NOT: div p --> kapsayıcı element + space + kapsanan element

# Attribute Selector:
# Elementlerin attribute'u olup olmamasına göre veya attribute değerine göre seçmek için kullanılırlar.
# Örnek: class='text-red' --> class değeri text-red olanı getir;           class burada attribute değeridir
#        class~='text-red' --> class değeri içinde text-red geçeni getir;  class burada attribute değeridir


# XPath (XML Path Language):
# XML veya HTML belgelerinde belirli ögeleri bulmak ve seçmek için kullanılan bir dil ve yol belirleme tekniğidir.
# Ağaç yapısını kullanarak ögeleri belirler ve sorguları bu yapıya göre oluşturur.

# Node, Element, tag: bulmak istediğimiz öge
# Attribute: elementlerin özellikleri; örnek id, class
# text: element içerisindeki içerik
# Child: bir elementin içerisindeki element
# Parent: Elementi kapsayan element. İçerisinde bulunduğumuz element
# Ancestor: tüm atalarımız, yani elementimizi içerisine alıp kapsayan tüm elementler.
# //: belgenin herhangi bir yerindeki elementleri aramak için kullanılır; belgenin tamamında arama yapar
# /: sadece child elementleri aramamızı sağlar.
# elementName: bu element adına sahip olan tüm elementleri seçer
# @attributeName: bir attribute'u seçer
# text(): bir elementin içindeki metni/içeriği seçer


# XPath Operatörleri
# '|' (Pipe) Operatörü: Birden fazla Operatörü aynı anda seçmek için kullanılır. ör: //h2 | //p
# 'and' Operatörü: iki farklı attribute koşulu tek sorguda yazılabilir. ör: //input[@type='text' and @name='username']
# 'or' Operatörü: iki attribute'den birini sağlasın demek için kullan. ör: //a[@class='external' or @target='_blank']

# XPath Fonksiyonları
# Diğer dillerde olduğu gibi built-in (gömülü) fonksiyonlardır.
# contains(): Özellik değerlerinde belirli bir parçayı arar.
# ör: //a[contains(@href, 'example')] -> href özelliği example içeren <a> öğelerini seçer.

# text() : Metin içeriğini seçer.
# ör: //p[text()='Hello'] -> İçeriği Hello olan <p> öğelerini seçer.

# starts-with() : Özellik değerlerinin belirli bir metin ile başladığını kontrol eder.
# Ör: //input[starts-with(@id, 'user')] -> id özelliği user ile başlayan <input> öğelerini seçer.

# not(): belirtilen bir koşulu sağlamayan ögeleri seçmek için kullanılır.
# ör: //div[not(@class='important')] -> class attribute'u important olmayan <div> ögelerini seçer.

# last(): bir listedeki son öğeyi, bir tabloda son satırı veya bir menüdeki son seçeneği belirlemek için kullanılır.
# ör: //ul/li[last()] -> <ul> etiketinin içindeki tüm <li> etiketlerinden (liste öğeleri) sonuncusunu seçer.
