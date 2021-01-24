'''print(
*******************************
sistem giriş ekranı

*******************************
)'''

sys_kullanici_adi = ("ebrusngl")
sys_parola = ("247948")

print("lütfen sistem bilgilerinizi giriniz...")

kullanici_adi = input("kullanıcı adı:")
parola = input("şifre:")

if (sys_kullanici_adi == kullanici_adi and sys_parola != parola):
    print("parolanızı hatalı girdiniz")
elif (sys_kullanici_adi != kullanici_adi and sys_parola == parola):
    print("kullanıcı adınız hatalı")
elif (sys_kullanici_adi != kullanici_adi and sys_parola != parola):
    print("hatalı giriş bilgileri girdiniz.")
else:
    print("sisteme başarılı bir şekilde girdiniz.")