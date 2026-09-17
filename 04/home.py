# ============================================
# 04 - ANA MENU


bakiye = 0.00
musteri_adi = "Ludociel"

while True:
    print("\n" + "=" * 40)
    print("        LudoBank Ana Menu")
    print("=" * 40)
    print("1. Bakiye Goruntule")
    print("2. Kredi Basvurusu")
    print("3. Faiz Hesapla")
    print("4. Cikis")
    print("=" * 40)

    secim = input("Secim (1-4): ")

    if secim == "1":
        print(f"\nBakiyeniz: {bakiye:.2f} TL")

    elif secim == "2":
        print("\nKredi basvurusu sayfasina yonlendiriliyor...")

    elif secim == "3":
        print("\nFaiz hesaplama sayfasina yonlendiriliyor...")

    elif secim == "4":
        print(f"\nGule gule, {musteri_adi}!")
        break

    else:
        print("\nGecersiz secim! 1-4 arasi bir sayi girin.")