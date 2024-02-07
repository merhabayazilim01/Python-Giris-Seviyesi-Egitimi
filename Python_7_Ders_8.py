def kontrol():
    if sayi >= 1:
        print("Sayı pozitiftir!")
    elif sayi == 0:
        print("Sayı 0'a eşittir.")
    elif sayi <0:
        print("Sayı negatiftir!")

while True:
    try:
        sayi = float(input("Sayıyı giriniz:"))
        kontrol()
        break
    except ValueError:
        print("Hatalı giriş yaptınız!")