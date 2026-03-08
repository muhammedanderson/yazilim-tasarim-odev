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

 def kalan_bul(a, b):
    print("Kalan Değer:", a % b)

kalan_bul(10, 3)
hesapla(10, 5)
cikarma(10, 5)
carpma(10, 5)
bolme(10, 5)