# Sınıflar ve objeler (def __init__)

class ogrenci:
    def __init__(self,isim,soyisim,vize,final):
        self.isim = isim
        self.vize = vize
        self.final = final
        self.soyisim= soyisim

    def ortalama_hesaplama(self):
        ortalama = self.vize * 0.4 + self.final*0.6

        if ortalama > 50:
            return "Geçti!"
        elif ortalama <51:
            return "Kaldı!"

ogrenci1 = ogrenci("Mustafa","Korkmaz",50,60)
ogrenci2 = ogrenci("Mehmet","Avcı",25,30)

print(ogrenci1.isim+" "+ogrenci1.ortalama_hesaplama())
print(ogrenci2.isim+ " "+ogrenci2.soyisim+ " " + ogrenci2.ortalama_hesaplama())


