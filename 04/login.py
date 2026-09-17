# ============================================
# 02 - GIRIS KONTROLU


# Veritabani register.py kaydettigimiz veriler
db_tc    = "12345678901"
db_sifre = "1234"
db_ad    = "Ludociel Yilmaz"

print("=" * 40)
print("        LudoBank Giris Ekrani")
print("=" * 40)

# Kullanicidan veri al
tc    = input("TC Kimlik No: ")
sifre = input("Sifre: ")

print()

# Kontrol zinciri
if tc != db_tc:
    print("Bu TC ile kayit bulunamadi.")
elif sifre != db_sifre:
    print("Sifre hatali.")
else:
    print(f"Hos geldin, {db_ad}!")
    print("Panele yonlendiriliyorsunuz...")