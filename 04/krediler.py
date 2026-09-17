# ============================================
# 05 - KREDI TURLERI


# Kredi verileri
krediler = [
    "Hizli Kredi",
    "Maas Musterisine Ozel",
    "Mutlu Emekli Kredisi",
    "Kampanyali Ihtiyac"
]

faizler = [5.06, 3.99, 4.25, 6.75]
vadeler = [48, 36, 24, 60]
miktarlar = [5000, 10000, 3000, 2000]

# Baslik
print("=" * 60)
print("        LudoBank Kredi Turleri")
print("=" * 60)

# Numarali liste
for i, (kredi, faiz, vade, miktar) in enumerate(
    zip(krediler, faizler, vadeler, miktarlar), start=1
):
    print(f"\n{i}. {kredi}")
    print(f"   Faiz : %{faiz}")
    print(f"   Vade : {vade} ay")
    print(f"   Tutar: {miktar} TL")

print("\n" + "=" * 60)