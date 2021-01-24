'''1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.
İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.
sayılar = range(1,11)
for i in sayılar:
    for j in sayılar:
        print("i : {}  j :  {}  ixj :  {}".format(i,j,i*j))'''



'''Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. 
Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.
İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.
toplam = 0
while True:
    sayı =input("lütfen bir sayı giriniz:")
    if (sayı == 'q'):
        break
    sayı= int(sayı)
    toplam += sayı
print(toplam) '''













