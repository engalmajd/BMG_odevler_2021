sinav_sonuc = {'isimler': ['ayse K.', 'Ahmet M.', 'Nuri C.', 'Nawar T.', 'Suzan T.', 'Ala B.'],
               'cinsiyet': ['K', 'E', 'E', 'E', 'K', 'K'], 'matematik': [60, 40, 97, 45, 56, 95],
               'turkce': [70, 30, 23, 80, 78, 46]}

def yeni_kayit():
    yeni_ismi = []
    yeni_cinsiyet = []
    yeni_math_not = []
    yeni_turkce_not = []
    yeni_isim1 = []
    for i in range(2):
        isim = input("isim giriniz :")
        cinsiyet = input("cinsiyet giriniz :")
        math_notu = input("matematik notu giriniz:")
        turkce_notu = input("turkce notu giriniz :")
        yeni_ismi.append(isim)
        yeni_cinsiyet.append(cinsiyet)
        yeni_math_not.append(math_notu)
        yeni_turkce_not.append(turkce_notu)
        print(yeni_ismi)
        print(yeni_cinsiyet)
        print(yeni_math_not)
        print(yeni_turkce_not)
    for k in range(2):
        sinav_sonuc['isimler'].append(yeni_ismi[k])
        sinav_sonuc['cinsiyet'].append(yeni_cinsiyet[k])
        sinav_sonuc['matematik'].append(yeni_math_not[k])
        sinav_sonuc['turkce'].append(yeni_turkce_not[k])
       
        print(sinav_sonuc["isimler"],'\n')
        print(sinav_sonuc["cinsiyet"], '\n')
        print(sinav_sonuc["matematik"],'\n')
        print(sinav_sonuc["turkce"])

yeni_kayit()
