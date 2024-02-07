"""# Hesap makinesi (Orta)
sayi1 = float(input("İlk sayıyı giriniz:"))
islem = input("İşlemi giriniz:")
sayi2 = float(input("İkinci sayıyı giriniz:"))

if islem == "+":
    print(sayi1+sayi2)
elif islem== "-":
    print(sayi1-sayi2)
elif islem=="*":
    print(sayi1*sayi2)
elif islem =="/":
    print(sayi1/sayi2)
else:
    print("Hatalı işlem yaptınız!")
    """
"""# Mil Kilometre Çevirici (Denizcilik)
while True:
    tur = input("(M)il mi yoksa (K)ilometre mi?, çıkış için (q):")
    deger = float(input("Değeri giriniz:"))

    if tur.lower() == "m":
        print((deger*1.6),"Kilometre")
    elif tur.lower() == "k":
        print((deger*0.6), "Mil")
    elif tur.lower() == "q":
        break
    else:
        print("Hatalı işlem yaptınız!")
"""
"""# While döngüsü
a = 0
while True:"""


# Try/Except

try:
    a = float(input("Değer giriniz:"))
    print(a)
except ValueError:
    print("Hatalı veri yazdınız!")
