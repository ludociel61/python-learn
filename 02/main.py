
# Giriş Kontrolü + Para Çekme
# ============================================

# 1. VERİTABANI 
# ============================================
db_hesapno = "6161"
db_sifre = "6161"
db_isim= "Ludociel"

# ============================================
# 2. HOŞ GELDİN EKRANI
# ============================================
print("=" * 40)
print("        LudoBank Giriş Ekranı")
print("=" * 40)

hesap_no = input("Hesap No: ")
sifre = input("Şifre: ")

print()

# 3. GİRİŞ KONTROLÜ (nested yapı)

if hesap_no != db_hesapno:
    print("Bu hesap numarası sistemde kayıtlı değil.")

elif sifre != db_sifre:
    print("Şifre hatalı!")

else:
    print(f"Hoş geldin, {db_isim}!")

    bakiye = 161.61
    print(f"\nMevcut bakiyen: {bakiye} TL")

    miktar = float(input("Çekilecek miktar: "))

    if miktar <= 0:
        print("Geçersiz miktar! 0'dan büyük olmalı.")
    elif miktar > bakiye:
        print(f"Yetersiz bakiye! Mevcut: {bakiye} TL")
    else:
        bakiye = bakiye - miktar
        print(f"{miktar} TL çekildi.")
        print(f"Kalan bakiye: {bakiye} TL")

print("\n--- Program sonlandı ---")