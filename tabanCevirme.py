#21100011042 / Nadire Nur / Sağlam

while True:
    print("----------------------------------------------")
    print("----------------------------------------------")
    print("(1) : Onluk tabandan ikilik tabana çavirme")
    print("(2) : İkilik tabandan onluk tabana çevirme")
    print("(3) : Çıkış")
    print("----------------------------------------------")

    islem = int(input("İşlem numarası seçiniz: "))
    print("----------------------------------------------")

    if islem == 1:
        temp = ""  # sayıyı sitring içine yazdırmak için
        sayi = int(input("Tabanı on olan bir sayı giriniz: "))

        while sayi != 0:
            temp = str(sayi % 2) + temp  # integer olan sayıyıyı string e dönüştürdük ki yan yana string halde yazabilelim.
            sayi = sayi // 2
        print("Sayının ikilik tabandaki karşılığı: ", temp)

    elif islem == 2:
        while True:
            sayilar = "23456789"  # Geçersiz sayılan sayılar string içinde tanımlandı
            sayi = input("Tabanı iki olan bir sayı giriniz: ")
            for i in sayi:
                if i in sayilar :
                    print("Geçersiz biçim kullanıldı!")
                    while sayi not in sayilar:
                        sayi = input("Tekrardan tabanı iki olan bir sayı giriniz: ")
                        break

            for i in sayi:
                if i == '1' or i == '0':
                    bas_sayisi = 0
                    n = 0
                    for i in sayi:
                        bas_sayisi = bas_sayisi + 1  # basamak saysı bulundu
                    bas_sayisi = bas_sayisi - 1  # sayıyla çarpılacak olan 2'nin üssünü sayının basamak sayısının 1 eksiği ile çarpmak için yazıldı
                    while bas_sayisi >= 0:
                        for i in sayi:
                            if i == '1':
                                n = n + 2 ** bas_sayisi  # sayıda 1 içeren basamaklar karşılığına gelen 2'nin üssü ile çarpıldı
                            bas_sayisi = bas_sayisi - 1  # basamak sayısı her seferinde azaltılarak en sondaki basamak 2 üzeri 0 ile çarpıldı
                    print("Sayının onluk tabandaki karşılığı: ", n)
                    break
            break
    else:
        print("Programdan çıkış yapılıyor... \n")
        break