import pandas as pd

df = pd.read_excel("C:/Users/Ebru/PycharmProjects/Kodlama Egzersizleri/venv/data.xlsx")

df = pd.DataFrame(df, columns=['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course', 'math score', 'reading score', 'writing score'])
#df.head()     # ilk beş satırı döndürüyor içine ne kadar dönmesini isteğiini yaz o satıra kadar döndürür.
#df.tail()     # tam tersi sondan beş döndürür.
#print(df.isnull().sum().sort_values(ascending=False))   #df ‘deki eksik değerlerin sayısını öğrenelim ve azalan şekilde sıralama.


#print(df)
#print(df.shape)     #dataframe satır ve sütun sayısını öğreniyoruz şuan
#print(df.columns)   # df nin stüunlarını
#print(df.dtypes)    #veri tiplerini öğreniyoruz.
#print(df.describe())   #sütunların istatistiksel özeti
#print(df["gender"].describe())  #istenilen kolondaki tanım analiz
#df.describe(include=['O'])   #Sayısal olmayan tüm sütunların istatiksel özetini görmek istiyorsak include=[‘O’] parametresini kullanmalıyız.
#df["gender"].value_counts()  #Her bir değerin sütunda bulunma sayısına bakalım.
#print(df[df["lunch"]=="standard"])  # belirli sütındaki verileri koşula bastırdık
#print(df.sort_values(by='reading score', ascending=False).head(10))  # sıralama
'''df.drop(6)
df.sort_values(by='reading score', ascending=False).head(10)
print(df.sort_values(by='reading score', ascending=False).head(10))'''

print(df.groupby("gender")["reading score"].mean().head(10))








