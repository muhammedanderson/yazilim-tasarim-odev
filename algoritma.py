def hesapla(sayi1, sayi2):
    # Bu fonksiyon iki sayi ile islem yapar
    sonuc = sayi1 + sayi2
    print("Sonuc:", sonuc)

# --- SENİN EKLEYECEĞİN KISIM ---
def cikarma(sayi1, sayi2):
    sonuc = sayi1 - sayi2
    print("Çıkarma Sonucu:", sonuc) # print'i içeri aldık, böylece hata vermez.

# -------------------------------
def carpma(sayi1, sayi2):
    sonuc = sayi1 * sayi2
    print("Çarpma Sonucu:", sonuc)

def bolme(sayi1, sayi2):
    if sayi2 != 0:
        sonuc = sayi1 / sayi2
        print("Bölme Sonucu:", sonuc)
    else:
        print("Hata: Bir sayı 0'a bölünemez!")

hesapla(10, 5)
cikarma(10, 5)
carpma(10, 5)
bolme(10, 5)

def mod_alma(sayi1, sayi2):
    print("Mod Sonucu:", sayi1 % sayi2)

mod_alma(10, 3)


