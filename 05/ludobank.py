# LudoBank - Tam Uygulama

import json
import os

# SABITLER
# ============================================
SITE_ADI = "LudoBank"
SLOGAN = "Gelecegin Bankasi"
DB_DOSYA = "musteriler.json"

# Kredi verileri (site'deki kredi kartlari)
KREDILER = [
    {"ad": "Hizli Kredi",            "faiz": 5.06, "vade": 48, "miktar": 5000},
    {"ad": "Maas Musterisine Ozel",  "faiz": 3.99, "vade": 36, "miktar": 10000},
    {"ad": "Mutlu Emekli Kredisi",   "faiz": 4.25, "vade": 24, "miktar": 3000},
    {"ad": "Kampanyali Ihtiyac",     "faiz": 6.75, "vade": 60, "miktar": 2000},
]


# VERITABANI (JSON dosyasi)
# ============================================
def veritabani_yukle():
    """musteriler.json dosyasini okur."""
    if not os.path.exists(DB_DOSYA):
        return {}
    try:
        with open(DB_DOSYA, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def veritabani_kaydet(musteriler):
    """musteriler.json dosyasina yazar."""
    with open(DB_DOSYA, "w", encoding="utf-8") as f:
        json.dump(musteriler, f, ensure_ascii=False, indent=2)

# YARDIMCI FONKSIYONLAR
# ============================================
def temizle():
    """Terminali temizler (Windows/Linux/Mac)."""
    os.system("cls" if os.name == "nt" else "clear")

def baslik(yazi, ikon=""):
    """Ortalanmis baslik yazar."""
    print()
    print("=" * 60)
    print(f"        {ikon} {yazi}")
    print("=" * 60)

def cizgi():
    print("-" * 60)

def bekle():
    input("\nDevam etmek icin Enter'a bas...")

# SAYFA 1: HOME (Hero)
# ============================================
def home():
    temizle()
    print()
    print("=" * 60)
    print(f"        {SITE_ADI}")
    print(f"        {SLOGAN}")
    print("=" * 60)
    print()
    print("        Hedeflerinize Daha Hizli Ulasin")
    print("        Tum ihtiyaclariniz icin hesaplama araclarimiz")
    print("        ve size ozel kredi secenekleri.")
    print()
    print("=" * 60)

def home_menu():
    while True:
        home()
        print("  [1] Kayit Ol")
        print("  [2] Giris Yap")
        print("  [3] Cikis")
        print("=" * 60)

        secim = input("Secim (1-3): ").strip()

        if secim == "1":
            register()
        elif secim == "2":
            musteri = login()
            if musteri:
                panel(musteri)
        elif secim == "3":
            print(f"\nGule gule!")
            break
        else:
            print("\nGecersiz secim!")
            bekle()

# SAYFA 2: REGISTER (Kayit)
# ============================================
def register():
    temizle()
    baslik("LudoBank - Hesap Ac")

    musteriler = veritabani_yukle()

    # Form
    ad      = input("Ad Soyad: ").strip()
    yas     = input("Yas: ").strip()
    tc      = input("TC Kimlik No (11 hane): ").strip()
    telefon = input("Telefon: ").strip()

    print("\nCalisma Durumu:")
    print("  [1] Calisiyorum")
    print("  [2] Calismiyorum")
    print("  [3] Ogrenciyim")
    print("  [4] Emekliyim")
    calisma_secim = input("Secim (1-4): ").strip()

    maas  = input("Aylik Maas (TL): ").strip()
    sifre = input("Sifre (en az 4 karakter): ").strip()

    # KONTROLLER
    # ============================================
    if not yas.isdigit():
        print("\nHATA: Yas sayi olmalidir!")
        bekle()
        return

    yas = int(yas)

    if len(tc) != 11 or not tc.isdigit():
        print("\nHATA: TC Kimlik No 11 haneli sayi olmalidir!")
        bekle()
        return

    if tc in musteriler:
        print("\nHATA: Bu TC ile zaten kayit var!")
        bekle()
        return

    if len(sifre) < 4:
        print("\nHATA: Sifre en az 4 karakter olmalidir!")
        bekle()
        return

    try:
        maas = float(maas)
    except ValueError:
        print("\nHATA: Maas sayi olmalidir!")
        bekle()
        return

    # Calisma map
    calisma_map = {
        "1": "evet",
        "2": "hayir",
        "3": "ogrenci",
        "4": "emekli"
    }
    calisma = calisma_map.get(calisma_secim, "hayir")

    # KAYIT
    # ============================================
    musteriler[tc] = {
        "ad": ad,
        "yas": yas,
        "tc": tc,
        "telefon": telefon,
        "calisma": calisma,
        "maas": maas,
        "sifre": sifre,
        "bakiye": 0.0,
        "krediler": []
    }

    veritabani_kaydet(musteriler)

    print()
    print("=" * 60)
    print("        KAYIT BASARILI")
    print("=" * 60)
    print(f"  Sayin {ad},")
    print(f"  Hesabiniz olusturuldu.")
    print(f"  TC: {tc}")
    print(f"  Simdi giris yapabilirsiniz.")
    print("=" * 60)
    bekle()

# SAYFA 3: LOGIN (Giris)
# ============================================
def login():
    temizle()
    baslik("LudoBank - Giris")

    musteriler = veritabani_yukle()

    if not musteriler:
        print("\nSistemde kayitli musteri yok.")
        print("Once kayit olmalisiniz.")
        bekle()
        return None

    tc    = input("TC Kimlik No: ").strip()
    sifre = input("Sifre: ").strip()

    print()

    # Kontrol zinciri
    if tc not in musteriler:
        print("HATA: Bu TC ile kayit bulunamadi.")
        bekle()
        return None

    if musteriler[tc]["sifre"] != sifre:
        print("HATA: Sifre hatali.")
        bekle()
        return None

    # Basarili
    print(f"Hos geldin, {musteriler[tc]['ad']}!")
    print("Panele yonlendiriliyorsunuz...")
    bekle()
    return musteriler[tc]

# SAYFA 4: PANEL
# ============================================
def panel(musteri):
    while True:
        temizle()
        musteriler = veritabani_yukle()
        musteri = musteriler[musteri["tc"]]  # guncel veri

        baslik("LudoBank Musteri Paneli")

        # Avatar (ismin bas harfi)
        avatar = musteri["ad"][0].upper()

        calisma_metin = {
            "evet": "Calisiyor",
            "hayir": "Calismiyor",
            "ogrenci": "Ogrenci",
            "emekli": "Emekli"
        }.get(musteri["calisma"], musteri["calisma"])

        print()
        print(f"  [{avatar}] {musteri['ad']}")
        print(f"      TC       : {musteri['tc']}")
        print(f"      Durum    : {calisma_metin}")
        print(f"      Maas     : {musteri['maas']} TL")
        print()
        cizgi()
        print("        MEVCUT BAKIYE")
        cizgi()
        print(f"        {musteri['bakiye']:.2f} TL")
        cizgi()
        print()

        print("Islemler:")
        print("  [1] Kredi Basvurusu")
        print("  [2] Faiz Hesapla")
        print("  [3] Kredilerim")
        print("  [4] Cikis Yap")
        print("=" * 60)

        secim = input("Secim (1-4): ").strip()

        if secim == "1":
            krediler(musteri)
        elif secim == "2":
            faiz()
        elif secim == "3":
            kredilerim(musteri)
        elif secim == "4":
            print(f"\nGule gule, {musteri['ad']}!")
            bekle()
            return
        else:
            print("\nGecersiz secim!")
            bekle()


# SAYFA 5: KREDILER (Liste)
# ============================================
def krediler(musteri):
    temizle()
    baslik("LudoBank - Kredi Turleri")

    print()
    for i, k in enumerate(KREDILER, start=1):
        print(f"  [{i}] {k['ad']}")
        print(f"      Faiz  : %{k['faiz']}")
        print(f"      Vade  : {k['vade']} ay")
        print(f"      Tutar : {k['miktar']} TL")
        print()

    cizgi()
    print("  [0] Panele Don")
    cizgi()

    secim = input("Basvurulacak kredi (1-4, 0=Don): ").strip()

    if secim == "0":
        return

    if secim in ["1", "2", "3", "4"]:
        index = int(secim) - 1
        kredionay(musteri, KREDILER[index])
    else:
        print("\nGecersiz secim!")
        bekle()

# SAYFA 6: KREDI ONAY (Basvuru)
# ============================================
def kredionay(musteri, kredi):
    temizle()
    baslik("KREDI BASVURUSU")

    print()
    print(f"  Kredi : {kredi['ad']}")
    print(f"  Tutar : {kredi['miktar']} TL")
    print(f"  Faiz  : %{kredi['faiz']}")
    print(f"  Vade  : {kredi['vade']} ay")
    print()

    # KONTROL 1: YAS
    # ============================================
    if musteri["yas"] < 18:
        print("=" * 60)
        print("        REDDEDILDI")
        print("=" * 60)
        print(f"  Kredi icin 18 yas ve uzeri olmalisiniz.")
        print(f"  Mevcut yasiniz: {musteri['yas']}")
        print("=" * 60)
        bekle()
        return

    # KONTROL 2: CALISMA DURUMU
    # ============================================
    calisiyor = musteri["calisma"] == "evet" or musteri["calisma"] == "emekli"

    if not calisiyor and "Emekli" not in kredi["ad"]:
        print("=" * 60)
        print("        REDDEDILDI")
        print("=" * 60)
        print(f"  Kredi icin calisiyor veya emekli olmaniz gerekiyor.")
        print(f"  Durumunuz: {musteri['calisma']}")
        print("=" * 60)
        bekle()
        return

    # KONTROL 3: MAAS
    # ============================================
    min_maas = kredi["miktar"] * 0.3

    if musteri["maas"] < min_maas:
        print("=" * 60)
        print("        REDDEDILDI")
        print("=" * 60)
        print(f"  Bu kredi icin min {min_maas:.0f} TL maas gerekiyor.")
        print(f"  Mevcut maasiniz: {musteri['maas']} TL")
        print("=" * 60)
        bekle()
        return

    # 
    # ONAYLANDI
    # ============================================
    toplam = kredi["miktar"] * (1 + (kredi["faiz"] / 100) * (kredi["vade"] / 12))
    taksit = toplam / kredi["vade"]

    # Bakiye guncelle
    musteriler = veritabani_yukle()
    musteriler[musteri["tc"]]["bakiye"] += kredi["miktar"]
    musteriler[musteri["tc"]]["krediler"].append({
        "ad": kredi["ad"],
        "tutar": kredi["miktar"],
        "faiz": kredi["faiz"],
        "vade": kredi["vade"],
        "taksit": round(taksit, 2),
        "toplam": round(toplam, 2)
    })
    veritabani_kaydet(musteriler)

    # Ekrani guncelle
    musteri["bakiye"] = musteriler[musteri["tc"]]["bakiye"]

    print("=" * 60)
    print("        ONAYLANDI")
    print("=" * 60)
    print(f"  Kredi Tutari  : {kredi['miktar']} TL")
    print(f"  Aylik Taksit  : {taksit:.2f} TL")
    print(f"  Toplam Odeme  : {toplam:.2f} TL")
    print(f"  Yeni Bakiye   : {musteri['bakiye']:.2f} TL")
    print("=" * 60)
    bekle()

# SAYFA 7: KREDILERIM (Aktif krediler)
# ============================================
def kredilerim(musteri):
    temizle()
    baslik("Kredilerim")

    musteriler = veritabani_yukle()
    aktif = musteriler[musteri["tc"]].get("krediler", [])

    if not aktif:
        print("\n  Henuz aktif krediniz yok.")
        bekle()
        return

    for i, k in enumerate(aktif, start=1):
        print(f"\n  [{i}] {k['ad']}")
        print(f"      Tutar  : {k['tutar']} TL")
        print(f"      Faiz   : %{k['faiz']}")
        print(f"      Vade   : {k['vade']} ay")
        print(f"      Taksit : {k['taksit']} TL")
        print(f"      Toplam : {k['toplam']} TL")

    bekle()

# SAYFA 8: FAIZ (Hesaplama)
# ============================================
def faiz_hesapla(anapara, oran, vade):
    """Basit faiz hesaplar. (toplam, taksit) dondurur."""
    toplam = anapara * (1 + (oran / 100) * (vade / 12))
    taksit = toplam / vade
    return toplam, taksit

def faiz():
    temizle()
    baslik("FAIZ HESAPLAMA")

    print()
    for i, k in enumerate(KREDILER, start=1):
        print(f"  [{i}] {k['ad']} - %{k['faiz']}")
    print()

    secim = input("Kredi turu (1-4): ").strip()

    if secim not in ["1", "2", "3", "4"]:
        print("\nGecersiz secim!")
        bekle()
        return

    kredi = KREDILER[int(secim) - 1]

    try:
        anapara = float(input("Anapara (TL): ").strip())
        vade = int(input("Vade (ay): ").strip())
    except ValueError:
        print("\nHATA: Gecerli sayi girin!")
        bekle()
        return

    toplam, taksit = faiz_hesapla(anapara, kredi["faiz"], vade)

    print()
    print("=" * 60)
    print("        HESAPLAMA SONUCU")
    print("=" * 60)
    print(f"  Kredi         : {kredi['ad']}")
    print(f"  Anapara       : {anapara:.2f} TL")
    print(f"  Faiz Orani    : %{kredi['faiz']}")
    print(f"  Vade          : {vade} ay")
    print(f"  Aylik Taksit  : {taksit:.2f} TL")
    print(f"  Toplam Odeme  : {toplam:.2f} TL")
    print("=" * 60)
    bekle()


# ANA PROGRAM
# ============================================
def main():
    home_menu()

if __name__ == "__main__":
    main()