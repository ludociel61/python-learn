# ============================================
# 06 - KREDI ONAY


# Musteri bilgileri
musteri = {
    "ad": "Ludociel",
    "yas": 21,
    "calisma": "evet",
    "maas": 15000,
    "bakiye": 0
}

# Kredi bilgileri
kredi_ad = "Hizli Kredi"
kredi_faiz = 5.06
kredi_vade = 48
kredi_miktar = 5000

print("=" * 40)
print("        KREDI BASVURUSU")
print("=" * 40)
print(f"Kredi : {kredi_ad}")
print(f"Tutar : {kredi_miktar} TL")
print(f"Faiz  : %{kredi_faiz}")
print(f"Vade  : {kredi_vade} ay")
print()

# Kontrol 1: Yas
if musteri["yas"] < 18:
    print(f"REDDEDILDI: 18 yas ve uzeri olmalisiniz.")
    print(f"Mevcut yasiniz: {musteri['yas']}")
else:
    # Kontrol 2: Calisma durumu
    calisiyor = musteri["calisma"] == "evet" or musteri["calisma"] == "emekli"

    if not calisiyor:
        print(f"REDDEDILDI: Calisiyor veya emekli olmaniz gerekiyor.")
        print(f"Durumunuz: {musteri['calisma']}")
    else:
        # Kontrol 3: Maas
        min_maas = kredi_miktar * 0.3

        if musteri["maas"] < min_maas:
            print(f"REDDEDILDI: Minimum {min_maas:.0f} TL maas gerekiyor.")
            print(f"Mevcut maasiniz: {musteri['maas']} TL")
        else:
            # ONAYLANDI
            musteri["bakiye"] += kredi_miktar

            toplam = kredi_miktar * (1 + (kredi_faiz / 100) * (kredi_vade / 12))
            taksit = toplam / kredi_vade

            print("=" * 40)
            print("        ONAYLANDI")
            print("=" * 40)
            print(f"Kredi Tutari  : {kredi_miktar} TL")
            print(f"Aylik Taksit  : {taksit:.2f} TL")
            print(f"Toplam Odeme  : {toplam:.2f} TL")
            print(f"Yeni Bakiye   : {musteri['bakiye']:.2f} TL")
