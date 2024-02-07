"""# For komutu
a = [1,2,3,4]

for isim in a:
    isim=isim+1
    print(isim)"""

"""# If komutu
kullanici_adi = input("Kullanıcı adınızı giriniz:")
sifre = input("Şifre giriniz:")

if kullanici_adi == "kirmiziayran" and sifre == "3853":
        print("Başarıyla giriş yaptınız!")
elif kullanici_adi == "beyazvisnesuyu" and sifre == "2538":
    print("Başarıyla giriş yaptınız Ertuğrul Bey.")
else:
    print("Hatalı giriş yaptınız.")"""

# Mantık operatörleri (>=,<=,==,!=,>,<)

vize = float(input("Vize notunuzu giriniz:"))
final = float(input("Final notunuzu giriniz:"))

ortalama = (vize+final)/2

if ortalama >= 70:
    print("Geçtiniz")
elif ortalama <= 69:
    print("Kaldınız")
else:
    print("Hatalı giriş yaptınız!")
