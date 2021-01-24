print('''
********************
gelişmiş kullancı giriş programı
********************
''')

sys_kullancı_adı = ("ebrusngl")
sys_parola = ("247948")

giris_hakki = 3

while True:
    kullanıcı_adı = input("kullanıcı adı:")
    parola = input("parola:")
    if (sys_kullancı_adı == kullanıcı_adı and sys_parola != parola):
        print("parola hatalı tekrar deneyiniz...")
        giris_hakki -= 1
    elif (sys_kullancı_adı != kullanıcı_adı and sys_parola == parola):
        print("kullanıcı adınız hatalı lütfen tekrar deneyiniz...")
        giris_hakki -= 1
    elif (sys_kullancı_adı != kullanıcı_adı and sys_parola != parola):
        print("hem kullanıcı adı hemde parolanız hatalı lütfen terar deneyin.")
        giris_hakki -= 1
    else:
        print("sisteme başarılı bir şekilde girdiniz.")
        break
    if (giris_hakki == 0):
        print("giriş hakkınız kalmamıştır.")
        break



