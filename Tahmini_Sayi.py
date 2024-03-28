import random       # rastegele sayı üretmek için random modülü kullanılır
                    # import ile projeye dahil ederiz 
def tahmin_oyunu():
    hedef_sayi = random.randint(1, 100)  # 1 ile 100 arasında rastgele bir sayı seç 
                                         # randint ile rasgele tam sayı üretilir  
    while True:                         #while True:: Bu satır, sonsuz bir döngü başlatır. 
        tahmin = int(input("Bir sayı tahmin edin (1-100 arası): "))      #Kullanıcı doğru tahmini yapana kadar veya program tarafından kesilene kadar bu döngü devam eder.

        if tahmin == hedef_sayi:                           # projede yer alan  "hedef_sayi , tahmin , devam " değişkendir
            print("Tebrikler! Doğru tahmin ettiniz.")
            break
        elif tahmin < hedef_sayi:
            print("Daha büyük bir sayı girin.")
        else:
            print("Daha küçük bir sayı girin.")

while True:   # sonsuz döngü oluşturur 
    tahmin_oyunu()     # oluşturulan fonksiyonu çağırır
    devam = input("Yeniden oynamak istiyor musunuz? (Evet/Hayır): ") 
    if devam.lower() != 'evet': # lower girdiği küçük harfe dönüştürür  evet dışında  başka bir şey yazarsa döngü sonlanır 
        break                    # evet yazmaz ise döngü sonlanır 
