sinav_sonuc = {'isimler': ['ayse K.', 'Ahmet M.', 'Nuri C.', 'Nawar T.', 'Suzan T.', 'Ala B.'],
               'cinsiyet': ['K', 'E', 'E', 'E', 'K', 'K'], 'matematik': [60, 40, 97, 45, 56, 95],
               'turkce': [70, 30, 23, 80, 78, 46]}

def yeni_kayit():
    y_ismi = []
    y_cinsiyet = []
    y_mat_not = []
    y_turkce_not = []
    for i in range(2):
        isim = input("isim giriniz :")
        cinsiyet = input("cinsiyet giriniz :")
        mat_notu = input("matematik notu giriniz:")
        turkce_notu = input("turkce notu giriniz :")
        y_ismi.append(isim)
        y_cinsiyet.append(cinsiyet)
        y_mat_not.append(mat_notu)
        y_turkce_not.append(turkce_notu)
        print(y_ismi)
        print(y_cinsiyet)
        print(y_mat_not)
        print(y_turkce_not)
    for k in range(2):
        sinav_sonuc['isimler'].append(y_ismi[k])
        sinav_sonuc['cinsiyet'].append(y_cinsiyet[k])
        sinav_sonuc['matematik'].append(y_mat_not[k])
        sinav_sonuc['turkce'].append(y_turkce_not[k])

        print(sinav_sonuc["isimler"],'\n')
        print(sinav_sonuc["cinsiyet"], '\n')
        print(sinav_sonuc["matematik"],'\n')
        print(sinav_sonuc["turkce"])

yeni_kayit()
