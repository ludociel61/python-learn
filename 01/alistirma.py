site_adi = "LudoBank"
isim = input("Ismin ne?: ")
yas = int(input("Kac yasindasin?: "))
calisiyor_musun = True

if yas >= 18:
    print(f"{site_adi} hosgeldin! Kayit olmak icin {yas} yasiniz yeterlidir.")
else:
    print(f"{site_adi} hosgeldin! Maalesef ki {yas} kayit olmak icin yasiniz yetmiyor.")
