import numpy as np

print(np.__version__)

dizi=np.random.rand(1,25,5) # burada 1 başlangıç değeri,25 son değer, 5 ise artış miktarını verir
print("örnek dizi")
print(dizi)

print("-------------------")

#a= np.arange(0,10) # 10 dahil değil ...
#print("Dizi oluşturma")
#print(a)

b=np.array([1,2,3,4,5,6,7,8,9]) # Başlangıç dizisi: [1, 2, 3, 4, 5, 6, 7, 8, 9]
                                #[5, 6] parametresi ile bölme: Diziyi 5. ve 6. indekslerde (6. ve 7. elemanlar) böleceğiz.
c= np.split(b,[5,6])            # 
print("Diziyi bölme")
print(c)                               #İlk bölme:

                                #[1, 2, 3, 4, 5]: Bu, dizinin 0'dan 4. indeksine (5. elemana) kadar olan kısmıdır.
                                #[6, 7, 8, 9]: Bu ise dizinin 5. indeksinden sonuna kadar olan kısmıdır.

                                #kinci bölme (5. indeks ve 6. indeks arasında):

                                #[1, 2, 3, 4, 5]: Bu, dizinin 0'dan 4. indeksine (5. elemana) kadar olan kısmıdır.
                                #[6]: Bu, dizinin 5. indeksi (6. elemanı) olarak sadece tek bir elemandan oluşan bir dizi parçasıdır.
                                #[7, 8, 9]: Bu, dizinin 6. indeksinden sonuna kadar olan kısmıdır.
                                #numpy.array(): Dizi oluşturma.
                                #numpy.zeros(): Sıfırlardan oluşan bir dizi oluşturma.
                                #numpy.ones(): Birlerden oluşan bir dizi oluşturma.
                                #numpy.arange(): Belirli bir aralıktaki sayıları içeren bir dizi oluşturma.
                                #numpy.linspace(): Belirli bir aralıktaki sayıları eşit aralıklarla içeren bir dizi oluşturma.
                                #umpy.reshape(): Dizinin şeklini değiştirme.
                               # numpy.concatenate(): Dizileri birleştirme.
                                #numpy.sum(): Dizideki elemanların toplamını hesaplama.
                               # numpy.mean(): Dizideki elemanların ortalamasını hesaplama.
                               # numpy.max(): Dizideki en büyük elemanı bulma.
                               # numpy.min(): Dizideki en küçük elemanı bulma.
                               # numpy.dot(): İki dizinin iç çarpımını hesaplama.