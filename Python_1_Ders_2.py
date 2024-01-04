# Değişkenler ve data türleri
isim = "Hasan" #String
karne = 85 #Integer
gpa = 3.45 #Float
sicak = True #Bool

# String ile çalışma
print(isim[2]) # 2. index olan 's' harfini yazdırma
print(isim.index("n")) #'n' harfinin kaçıncı indexte olduğunu bulmak
print(isim.count("a")) # Kaç tane a harfi olduğunu yazdırma
print(isim.replace("a","o") # 'a' harflerinin hepsini 'o' harfine çevirmek

isim1 = "MuStAfa eMRe"
print(isim1.capitalize()) # İlk harf büyük olacak şekilde yazdırmak.
print(isim1.lower()) # Bütün harfleri küçük yazdırmak
print(isim1.upper()) # Bütün harfleri büyük yazdırmak

#Numaralar ile Çalışma

print(karne + 5) #Toplama
print(karne - 10) #Çıkarma
print(karne * 2) #Çarpma
print(karne / 5) #Bölme
print(karne // 3) #Bölme işlemi sonrası tam bölünmez ise sonucu integer sayıya yuvarlama
print(karne % 3) #Mod alma (Bölme işlemi sonrası kalan sayıyı yazdırma)
print(karne ** 2) #Üslü ifade

#İnput almak

isim2 = input("Bir isim giriniz:")
print(isim2)

yas = int(input("Yaşınızı giriniz:"))
print(yas * 5)

karne1 = float(input("Karne ortalamanızı giriniz:"))
print(karne1 / 2)

# Basit bir ortalama hesaplayıcı

vize = float(input("Vize notunuzu giriniz:"))
final = float(input("Final notunuzu giriniz:"))

sonuc = (vize + final)/2

print(sonuc)
