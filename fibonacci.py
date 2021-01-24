""" fibonacci serisi yeni bir sayıyı önceki iki sayının toplamıyla olusturur

1 1 2 3 5 8 13 21 34
"""
a,b = 1,1

fibonacci = [a,b]

for i in range(20):
    a,b = b,a+b
    fibonacci.append(b)
print(fibonacci)


