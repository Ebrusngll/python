print('''
xxxxxxxxxxxxxxxxxxxxxxxxx
faktöriyel hesaplama programı

programdan çıkmak için lütfen 'q' ya basınız.
xxxxxxxxxxxxxxxxxxxxxxxxx
''')

while True:
    sayı = input("sayı:")
    if (sayı == "q"):
        print("programdan çıkılıyor")
        break
    else:
        sayı = int(sayı)
        faktöriyel = 1

        for i in range(2,i+1):
            faktöriyel *= i
        print("faktöriyel",faktöriyel)

