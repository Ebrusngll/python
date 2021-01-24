'''Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi ,
 dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı ,
 eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın.
 Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.'''

print("üçgen tipi mi yoksa dikdörgen tipi mi bulmak istiyorsunuz.")

cevap = input("ne istediğinizi girin:")

if cevap == "dörtgen":
    print("dört tane kenar değeri giriniz")
    kenar1 = int(input("kenar1:"))
    kenar2 = int(input("kenar2:"))
    kenar3 = int(input("kenar3:"))
    kenar4 = int(input("kenar4:"))

    if (kenar1==kenar2==kenar3==kenar4):
        print("şekil karedir")
    elif (kenar1==kenar3 and kenar2==kenar4):
        print("şekil dikdörtgendir")
    else:
        print("şekil normal dörtgendir")
elif cevap == "üçgen":
    print("üç tane kenar giriniz.")
    ken1 = int(input("kenar1:"))
    ken2 = int(input("kenar2:"))
    ken3 = int(input("kenar3:"))
    if (ken1==ken2==ken3):
        print("üçgen eşkenardır")
    elif (ken1==ken2):
        print("üçgen ikizkenar üçgendir")
    else:
        if not (abs(ken1-ken2) < ken3 < ken1+ken2 and abs(ken1-ken3) < ken2 < ken1+ken3 and abs(ken2-ken3) < ken1 < ken2+ken3):
            print("üçgen belirtmez")
else:
    print("geçersiz şekil")

