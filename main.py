# Sayıların toplamını hesaplayan fonksiyon
def sayilari_topla(sayilar):
    toplam = 1
    for sayi in sayilar:
        toplam += sayi  # Her sayıyı toplama ekliyoruz
    return toplam

if __name__ == "__main__":
    # Fonksiyonu kullanarak bir listeyi işliyoruz
    sayilar = [1, 2, 3, 4, 5]
    sonuc = sayilari_topla(sayilar)

    # Sonucu ekrana yazdırıyoruz
    print("Sayıların toplamı:", sonuc)
