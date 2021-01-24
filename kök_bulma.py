'''ikinci dereceden bir bilinmeyenli denklemin köklerini bulma
Denklem = ax^2 + bx + c
Deltayı hesaplama = b**2 - 4*a*c
Birinci Kök = (-b-Delta**0.5)/(2*a*c)
İkinci kök =(-b+Delta**0.5)/(2*a*c) '''

a = int(input("a sayısını giriniz:"))
b = int(input("b sayısını giriniz:"))
c = int(input("c sayısını giriniz:"))

Delta = b**2-4*a*c

# delta ** 0.5 demek deltanın karekökü anlamında sonradan kafan karışmasın

x1 = ((-b-Delta**0.5)/(2*a*c))
x2 = ((-b+Delta**0.5)/(2*a*c))

print("a sayısı: {}\nb sayısı: {}\nc sayısı: {}\nbirinci kök: {}\nikinci kök: {}".format(a, b, c, x1, x2))

