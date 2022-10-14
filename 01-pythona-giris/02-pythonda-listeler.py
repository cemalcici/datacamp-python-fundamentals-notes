# region Python Veri Tipleri

# float - ondalık sayı
# int - tamsayı
# str - karakter dizisi, metin
# bool - Doğru ve Yanlış

# Her bir değişken bir değeri temsil eder.

# Problem, Veri Biliminin çok fazla veri gerektirdiğidir. 
# Örneğin bir aileye ait boy uzunluklarını girelim

uzunluk1 = 1.73
uzunluk2 = 1.68
uzunluk3 = 1.71
uzunluk4 = 1.89

# Bu şekilde yazmak zahmetli. Peki, ne yapmalı?

# endregion

# region Python Listeler

# [a, b, c] şeklinde oluşturulan nesnelerdir.

# Yukarıdaki uzunluk değerlerini bir listede toplayabiliriz

aile = [1.73, 1.68, 1.71, 1.89]
print(aile)

# Bir değerler koleksionuna isim verebiliriz.
# Bu değerler herhangi bir tipte olabilir. 
aile = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
print(aile)

# Veya bu şekilde de oluşturabiliriz.
aile2 = [["liz", 1.73],
         ["emma", 1.68],
         ["mom", 1.71],
         ["dad", 1.89]]

print(aile2)

# Listeler, belirli davranışlara ve fonksiyonlara sahiptir.

# endregion

# region Listeden Eleman Seçmek

# Tek eleman seçmek

aile = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]

print(aile[3]) # 1.68
print(aile[6]) # dad
print(aile[-1]) # 1.89 <-
print(aile[7]) # 1.89 <-

# Birden fazla eleman seçmek

print(aile[3:5]) # [1.68, "mom"]
print(aile[1:4]) # [1.73, "emma", 1.68]

# Liste dilimlemenin yapısı:
# liste_adi[başlangıç(dahil):bitiş(hariç)]

print(aile[:4]) # ["liz", 1.73, "emma", 1.68]
print(aile[5:]) # [1.71, "dad", 1.89]

# endregion

# region Liste Üzerinde İşlemler

aile = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]

# region Liste elemanını değiştirmek

aile[7] = 1.86
print(aile) # ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.86]

aile[0:2] = ["lisa", "1.74"]
print(aile) # ['lisa', '1.74', 'emma', 1.68, 'mom', 1.71, 'dad', 1.86]

# endregion

# region Listeye eleman eklemek

print(aile + ["me", 1.79]) # ['lisa', '1.74', 'emma', 1.68, 'mom', 1.71, 'dad', 1.86, 'me', 1.79]

# endregion

# region Listeden eleman çıkarmak

del(aile[2])
print(aile) # ['lisa', '1.74', 1.68, 'mom', 1.71, 'dad', 1.86]

# endregion

# endregion

# region Listeyi Kopyalamak

x = ["a", "b", "c"]
y = x
y[1] = "z"

print(y) # ['a', 'z', 'c']
print(x) # ['a', 'z', 'c']

# Bunu önlemek için aşağıdaki yolu izlemek gerekir:

x = ["a", "b", "c"]
y = list(x)
y[1] = "z"

print(y) # ['a', 'z', 'c']
print(x) # ['a', 'b', 'c']

# endregion
