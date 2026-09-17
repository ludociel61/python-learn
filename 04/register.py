# ============================================
# 01 - KAYIT FORMU


print("=" * 40)
print("        LudoBank Kayit Formu")
print("=" * 40)

# Kullanicidan veri al
ad      = input("Ad Soyad: ")
yas     = int(input("Yas: "))
tc      = input("TC Kimlik No: ")
telefon = input("Telefon: ")
calisma = input("Calisma Durumu (evet/hayir/ogrenci/emekli): ")
maas    = float(input("Aylik Maas (TL): "))
sifre   = input("Sifre: ")

# Kayit onayi
print()
print("=" * 40)
print("        KAYIT OZETI")
print("=" * 40)
print(f"Ad Soyad : {ad}")
print(f"Yas      : {yas}")
print(f"TC       : {tc}")
print(f"Telefon  : {telefon}")
print(f"Calisma  : {calisma}")
print(f"Maas     : {maas} TL")
print(f"Sifre    : {'*' * len(sifre)}")
print("=" * 40)

print(f"\nSayin {ad}, hesabiniz olusturuldu.")