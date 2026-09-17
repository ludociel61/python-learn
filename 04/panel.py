# ============================================
# 03 - PANEL GOSTERIMI


# Aktif musteri bilgileri
musteri = {
    "ad": "Ludociel Yilmaz",
    "tc": "12345678901",
    "calisma": "Calisiyor",
    "bakiye": 0.00
}

# Panel basligi
print("=" * 50)
print(f"        LudoBank Musteri Paneli")
print("=" * 50)

# Musteri bilgileri
print(f"\nMusteri : {musteri['ad']}")
print(f"TC      : {musteri['tc']}")
print(f"Durum   : {musteri['calisma']}")

# Bakiye
print(f"\n{'=' * 50}")
print(f"        MEVCUT BAKIYE")
print(f"{'=' * 50}")
print(f"\n        {musteri['bakiye']:.2f} TL")
print(f"\n{'=' * 50}")