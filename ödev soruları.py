'''  SORU 1)kullanıcıdan aldığın 3 tane sayıyı çarptır ekrana yazdır yazdıma işlemini formatla yap.'''
'''print("sayıları giriniz:")
a = int(input("birinci sayıyı giriniz:"))
b = int(input("ikinci sayıyı giriniz:"))
c = int(input("üçüncü sayıyı giriniz:"))

islem = (a*b*c)
print("birinci sayı: {}\nikinci sayi: {}\nücüncü sayi: {}\nislem: {}".format(a,b,c,islem))'''



''' SORU 2)kullanıcıdan aldığınız boy ve kilo oranına göre vücut kitle endeksini buldurun.'''
'''print("lütfen bilgilerinizi giriniz...")
boy = int(input("boyunuzu giriniz:"))
kilo = int(input("kilonuzu giriniz:"))
print("bilgiler işleniyor...")
print("vücut kitle endeksiniz hesaplanıyor...")

endeks = (boy/kilo)
print(endeks)'''



''' SORU 3) bir aracın kilometrede ne kadar yaktığını ve ka. kilometre yol yaptığını bilgilerini al ve sürücünün toplam ne
kadar ödemesi gerektiğini hesapla'''

'''print("lütfen istenilen bilgileri giriniz...")
yakilan_yakit = int(input("yakilan yakit bilgisini giriniz:"))
km = int(input("aracın kac km gittigini giriniz:"))

print("sürücünün toplam ne kadar ödemesi gerektiği hesaplanıyor lütfen bekleyiniz...")

hesap = yakilan_yakit/km
benzin = 5
ödenek = hesap*benzin
print(ödenek)'''




'''SORU 4) kullanıcıdan ad,soyad ve telefon numarasını alarak bunları alt alta yazdırın'''

'''print("lütfen bilgilerinizi giriniz...")
ad = input("adınızı giriniz:")
soyad = input("soyadınızı giriniz:")
telefon_no = int(input("telefon numarasını giriniz:"))

print("ad: {}\nsoyad: {}\ntelefon numarası: {}".format(ad,soyad,telefon_no))'''




'''SORU 5) kullanıcadan iki sayı isteyin ve bu sayıları birbiriyle değiştirin'''
'''print("istenilen bilgileri lütfen giriniz...")
sayi1 = int(input("birinci sayıyı giriniz:"))
sayi2 = int(input("ikinci sayiyi giriniz:"))

a = sayi1
b = sayi2

sayi1 = b
print(sayi1)

sayi2 = a
print(sayi2)'''



'''SORU 6) kullanıcıdan bir dik üçgenin dik olan iki kenarının (a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın '''
''' hipotenüs formülü : a^2 + b^2 = c^2 '''

'''print("üçgenin bilgilerini giriniz...")
a = int(input("a kenarını uzunluğunu giriniz:"))
b = int(input("b kenarının uzunluğunu giriniz:"))

hip = a**2 + b**2
c = hip**0.5
print(c)'''



'''harf notu hesaplama sistemi'''
'''print("lütfen notunuzu giriniz...")
puan = float(input("notunuzu giriniz:"))
if 0<puan<49:
    print("FF")
elif 50<puan<54:
    print("FD")
elif 55<puan<59:
    print("DD")
elif 60<puan<64:
    print("DC")
elif 65<puan<74:
    print("CC")
elif 75<puan<79:
    print("CB")
elif 80<puan<84:
    print("BB")
elif 85<puan<89:
    print("BA")
else:
    print("AA")'''






