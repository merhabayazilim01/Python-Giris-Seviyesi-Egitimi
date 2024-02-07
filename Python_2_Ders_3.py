#Liste ve liste fonksiyonları

list1 = [1,2,3,4] # Liste oluşturma
print(list1) # Listeyi yazdırma
list1.append(5) # Listenin sonuna eleman ekleme
print(list1)
list1.pop() # Listenin sonundan eleman çıkarma
print(list1)
list1.remove(4) # list1 içindeki 4 verisini silme
print(list1)
print(list1.index(2)) # Elemanın indeksini verme


#Dictionary
sozluk = {"isim":"Ali", "soyisim":"Veli"} # Sözlük oluşturma
print(sozluk) # Sözlük yazdırma
sozluk["yas"] = 25 # Anahtar-değer ekleme
print(sozluk)
print(sozluk["isim"])

#Fonksiyonlar
def toplama(a,b): # Fonksiyon tanımlama
    return a+b

print(toplama(5,3)) # Fonksiyon çağırma