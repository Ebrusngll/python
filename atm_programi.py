print('''
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
bu bir atm programıdır.
1. bakiye sorgulama
2. para çekme
3. para yatırma
programdan çıkmak için 'q' ya basın.
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
''')

bakiye = 1000

while True:
    işlem = input("lütfen yapmak istediğiniz işlemi tuşlayınız:")

    if (işlem == "q"):
        print("çıkış yapılıyor...")
        break
    elif (işlem == 1):
        print("bakiyeniz :  {} TL dir.".format(bakiye))
    elif (işlem ==2):
        miktar = int(input("çekiceğiniz miktarı giriniz:"))
        if (miktar>bakiye):
            print("bu işlemi gerçekleştiremezsiniz.hesabınızda yeterli miktar da para yok.")
            continue
        bakiye_yeni = bakiye-miktar
        print("yeni bakiyeniz:  {}".format(bakiye_yeni))
    elif (işlem==3):
        miktar = int(input("yatırıcağınız miktarı giriniz:"))
        bakiye = bakiye+miktar
        print("yeni bakiyeniz:  {}".format(bakiye))
    else:
        print("geçersiz işlem")









