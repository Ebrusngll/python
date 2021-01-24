'''Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez'''

'''print("lütfen boy ve kilo bilgilerinizi giriniz.")
boy = float(input("boy:"))
kilo = int(input("kilo:"))

BKİ = kilo/(boy * boy)
if BKİ < 18.5:
    print("zayıfsınız")
elif 18.5<BKİ<25:
    print("normal kilodasınız")
elif 25<BKİ<30:
    print("fazla kilolusunuz")
else:
    print("obezsin yeme")'''




'''Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.'''
'''print("lütfen istenilen bilgileri giriniz...")
say1 = int(input("birinci sayi:"))
say2 = int(input("ikinci sayi:"))
say3 = int(input("üçüncü sayi:"))

if (say1 > say2 and say1 >say3):
    print(say1)
elif (say2 > say1 and say2 > say3):
    print(say2)
elif (say3 > say1 and say3 > say2):
    print (say3)
elif (say1 == say2 and say1 > say3):
    print(say1)
elif (say1 == say3 and say1 > say2):
    print(say1)
elif (say2 == say3 and say2 > say1):
    print(say2)
else:
    print("tüm sayılar eşit büyük olan yok...")'''


''' Vize1 toplam notun %30'una etki edecek.
    Vize2 toplam notun %30'una etki edecek.
    Final toplam notun %40'ına etki edecek.

    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF'''

print("öğrencilerin vize ve final notlarını giriniz.")
vize1 = int(input("vize1"))
vize2 = int(input("vize2"))
final = int(input("final"))

toplam_not = ((vize1*30)/100 + (vize2*30)/100 + (final*40)/100)
'''toplam notu kotrol amaçlı yazdım'''
print(toplam_not)

if toplam_not < 55:
    print("FF")
elif 55<=toplam_not<59:
    print("FD")
elif 59<=toplam_not<65:
    print("DD")
elif 65<=toplam_not<70:
    print("DC")
elif 70<=toplam_not<75:
    print("CC")
elif 75<=toplam_not<80:
    print("CB")
elif 80<=toplam_not<85:
    print("BB")
elif 85<=toplam_not<90:
    print("BA")
else:
    print("AA")