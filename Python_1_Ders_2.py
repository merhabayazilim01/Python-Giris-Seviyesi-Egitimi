# Değişkenler ve data türleri
isim = "Hasan"
karne = 85
gpa = 3.45
sicak = True

# String ile çalışma
print(isim[2])
print(isim.index("s"))
print(isim.count("a"))

isim1 = "MuStAfa eMRe"
print(isim1.capitalize())
print(isim1.lower())
print(isim1.upper())

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
