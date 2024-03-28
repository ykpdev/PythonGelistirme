def toplama(x, y):               #def ile fonk oluşturuldu 
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y == 0:
        return "Bir sayı sıfıra bölünemez!"
    else:
        return x / y

print("Hesap Makinesi Programı")          # ekranda hangi sayı hangi işleme karşılık geldiğini gösterir
print("1. Toplama")                       # print ile yapılacak işlemler ekrana alt alta yazılır
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

secim = input("Yapmak istediğiniz işlemi seçin (1/2/3/4): ") # secim adında değişken  oluşturulur

sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

if secim == '1':
    print("Sonuç:", toplama(sayi1, sayi2))
elif secim == '2':
    print("Sonuç:", cikarma(sayi1, sayi2))
elif secim == '3':
    print("Sonuç:", carpma(sayi1, sayi2))            # if ve elif ifadeleri, koşullu durumları kontrol etmek için Python'da kullanılan yapısal öğelerdir. 
                                                     #Bu ifadeler, belirli koşulların doğru olup olmadığını kontrol eder ve bu koşullara göre farklı blokların çalışmasını sağlar.
elif secim == '4':
    print("Sonuç:", bolme(sayi1, sayi2))
else:
    print("Geçersiz seçim. Lütfen tekrar deneyin.")