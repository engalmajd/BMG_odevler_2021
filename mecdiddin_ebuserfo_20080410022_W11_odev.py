from types import DynamicClassAttribute
# Matrisi tanımlarız ve elemanları içine koyarız.
kisilar = ['mohamad','ahmad','murat','ali']
# liste ekrana yazdir
print(kisilar)
# kulancidan 4 isim iste
kulancilist = input("enter the first name")
#kulanc girdiği isim listeye ekleyiniz ve ekrana yazdir
kisilar.append(kulancilist)
print(kisilar)
# liste uzunlugu
print(len(kisilar)) #(len) işlevi dizinin uzunluğunu yazdırmak için kullanılır

#listenin 2. elemanini ekrana yazdiriniz
print('kisilar[1]=',kisilar[1]) #Dizideki herhangi bir öğeye erişmek için, değerini almak veya değiştirmek için, öğenin dizin numarasını kullanırız.
#son elemanini sil
kisilar.pop(-1)   # Sentence(pop), bir diziyi bellekten olduğu gibi silmek veya diziden belirli öğeleri çıkarmak için kullanılır.
print(kisilar)  # Öğeyi sildikten sonra diziyi yazdırmayı tekrarlıyoruz