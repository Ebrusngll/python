print("""*************************************
bu bir basit hesap makinesi programıdır...

1. işlem toplama işlemi
2. işlem çıkarma işlemi
3. işlem çarpma işlemi
4. işlem bölme işlemi
*************************************
""")

print("lütfen işlem yaptırmak istediğiniz sayıları giriniz...")
a = int(input("birinci sayı:"))
b = int(input("ikinci sayı:"))

işlem = input("işlemi giriniz")

if işlem == "1":
    print("{} ile {} in toplamı {}".format(a,b,a+b))
elif işlem == "2":
    print("{} ile {} in farkı {}".format(a, b, a - b))
elif işlem =="3":
    print("{} ile {} in çarpımı {}".format(a, b, a * b))
elif işlem =="4":
    print("{} ile {} in bölümü {}".format(a, b, a / b))
else:
    print("geçersiz işlem")