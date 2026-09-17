# ============================================
# 07 - FAIZ HESAPLAMA (Fonksiyon)


def faiz_hesapla(anapara, oran, vade):
    """
    Basit faiz hesaplar.
    anapara: kredi tutari (TL)
    oran: yillik faiz orani (%)
    vade: ay cinsinden vade
    return: (toplam_odeme, aylik_taksit)
    """
    toplam = anapara * (1 + (oran / 100) * (vade / 12))
    taksit = toplam / vade
    return toplam, taksit


# Kullanim
print("=" * 40)
print("        FAIZ HESAPLAMA")
print("=" * 40)

anapara = float(input("Anapara (TL): "))
oran = float(input("Faiz Orani (%): "))
vade = int(input("Vade (ay): "))

toplam, taksit = faiz_hesapla(anapara, oran, vade)

print()
print("=" * 40)
print(f"Anapara       : {anapara:.2f} TL")
print(f"Faiz Orani    : %{oran}")
print(f"Vade          : {vade} ay")
print(f"Aylik Taksit  : {taksit:.2f} TL")
print(f"Toplam Odeme  : {toplam:.2f} TL")
print("=" * 40)
