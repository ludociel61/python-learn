# Kredi Türleri 

"""
<div class="kredi-karti">Hızlı Kredi</div>
<div class="kredi-karti">Maaş Müşterisi</div>
<div class="kredi-karti">Emekli Kredisi</div>
<div class="kredi-karti">Kampanyalı Kredi</div>
"""


# Listeler + Döngüler + Menü
# ============================================

# 1. KREDİ LİSTELERİ
# ============================================
krediler = [
    "Hızlı Kredi",
    "Maaş Müşterisine Özel Kredi",
    "Mutlu Emekli Kredisi",
    "Kampanyalı İhtiyaç Kredisi"
]

faizler = [5.06, 3.99, 4.25, 6.75]
vadeler = [48, 36, 24, 60]

# 2. BASİT LİSTELEME
# ============================================
print("#" * 40)
print("        KREDİ TÜRLERİ")
print("#" * 40)

for kredi in krediler:
    print(f"{kredi}")

print()

# ============================================
# 3. NUMARALI LİSTELEME (enumerate)
# ============================================
print("Numaralı liste:")
for i, kredi in enumerate(krediler, start=1):
    print(f"  {i}. {kredi}")

print()

# 4. DETAYLI LİSTELEME (zip ile)
# ============================================
# zip: iki listeyi yan yana getirir


print("Detaylı liste:")
for i, (kredi, faiz, vade) in enumerate(zip(krediler, faizler, vadeler), start=1):
    print(f"  {i}. {kredi}")
    print(f"     Faiz: %{faiz}  |  Vade: {vade} ay")

print()

# 5. MENÜ while 
# ============================================
bakiye = 161.61

print("=" * 40)
print("        LudoBank Ana Menü")
print("=" * 40)

while True:
    print("\n--- MENÜ ---")
    print("1. Bakiye Görüntüle")
    print("2. Para Çek")
    print("3. Para Yatır")
    print("4. Kredileri Gör")
    print("5. Çıkış")

    secim = input("Seçim: ")

    # ----------------------------------------
    # 1. BAKİYE
    # ----------------------------------------
    if secim == "1":
        print(f"\n Bakiyeniz: {bakiye} TL")

    # ----------------------------------------
    # 2. PARA ÇEK
    # ----------------------------------------
    elif secim == "2":
        miktar = float(input("Çekilecek miktar: "))

        if miktar <= 0:
            print("Geçersiz miktar! 0'dan büyük olmalı.")
        elif miktar > bakiye:
            print(f"Yetersiz bakiye! Mevcut: {bakiye} TL")
        else:
            bakiye = bakiye - miktar
            print(f"{miktar} TL çekildi. Kalan: {bakiye} TL")

    # ----------------------------------------
    # 3. PARA YATIR
    # ----------------------------------------
    elif secim == "3":
        miktar = float(input("Yatırılacak miktar: "))

        if miktar <= 0:
            print("Geçersiz miktar! 0'dan büyük olmalı.")
        else:
            bakiye = bakiye + miktar
            print(f"{miktar} TL yatırıldı. Yeni bakiye: {bakiye} TL")

    # ----------------------------------------
    # 4. KREDİLERİ GÖR
    # ----------------------------------------
    elif secim == "4":
        print("\nKredi Türleri:")
        for i, (kredi, faiz, vade) in enumerate(zip(krediler, faizler, vadeler), start=1):
            print(f"  {i}. {kredi}  —  %{faiz}  —  {vade} ay")

    # ----------------------------------------
    # 5. ÇIKIŞ
    # ----------------------------------------
    elif secim == "5":
        print("\nÇıkış yapılıyor... İyi günler!")
        break

    # ----------------------------------------
    # GEÇERSİZ SEÇİM
    # ----------------------------------------
    else:
        print("Geçersiz seçim! 1-5 arası bir sayı girin.")

print("\n--- Program sonlandı ---")