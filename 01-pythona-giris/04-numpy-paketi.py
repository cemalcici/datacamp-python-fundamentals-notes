# region NumPy Giris

# Listeleri Hatırlayalım
# Güçlüler
# Verileri koleksiyon halinde tutarlar
# Farklı veri tipleri barındırabilirler
# Elemanları değiştirilebilir, eklenebilir ve çıkarılabilir

# Peki, Veri Bilimi için bize neler lazım?
# Veri koleksiyonları üzerinde matematiksel işlem
# Hız

# Aşağıda liste halinde verilen boy ve kilo değerlerine sahip kişilerin
# Beden kütle endekslerini hesaplayalım.

boy = [1.73, 1.68, 1.71, 1.89, 1.79]
kilo = [65.4, 59.2, 63.6, 88.4, 68.7]
bke = kilo / boy ** 2

print(bke) # Hata verir

# Çözüm: NumPy
# Numeric Python isminin kısaltmasıdır.
# Listelere alternatif olarak NumPy dizileri vardır.
# Dizi içerisindeki her bir değer üzeride matematiksel işlem yapabiliriz.
# Kullanımı kolay ve hızlıdır.

import numpy as np

np_boy = np.array(boy)
np_kilo = np.array(kilo)
np_bke = np_kilo / np_boy ** 2

print(np_bke) # array([21.85171573, 20.97505669, 21.75028214, 24.7473475 , 21.44127836])

# NumPy dizileri sabit tipte veri tutar.

print(np.array([1.0, "is", True])) # array(['1.0', 'is', 'True'], dtype='<U32'

# Listelerde + operatörü eleman eklerken, NumPy dizilerinde + operatörü dizideki her bir elemanı karşılıklı toplar.

python_liste = [1, 2, 3]
numpy_dizi = np.array([1, 2, 3])

print(python_liste + python_liste) # [1, 2, 3, 1, 2, 3]
print(numpy_dizi + numpy_dizi) # array([2, 4, 6])

# NumPy dizilerinde listelere ilave olarak şarta bağlı eleman seçilebilir

print(np_bke[1]) # 20.97505669
print(np_bke[np_bke > 23]) # array([24.7473475])

# endregion

# region 2 Boyutlu NumPy Dizileri

# NumPy Dizilerin Tipleri

print(type(np_bke)) # numpy.ndarray

np_2_boyut = np.array([np_boy,
                       np_kilo])

print(np_2_boyut.shape) # (2, 5) -> 2 satır, 5 sütun

# 2 boyutta da sabit tiplidir

print(np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                [65.4, 59.2, 63.6, 88.4, "68.7"]]))

# array([['1.73', '1.68', '1.71', '1.89', '1.79'], ['65.4', '59.2', '63.6', '88.4', '68.7']], dtype='<U32')

# Eleman Seçimi

print(np_2_boyut)

#          0     1     2     3     4 
#          |     |     |     |     |
# array([[1.73, 1.68, 1.71, 1.89, 1.79],  -- 0
#        [65.4, 59.2, 63.6, 88.4, 68.7]]) -- 1

print(np_2_boyut[0]) # [1.73, 1.68, 1.71, 1.89, 1.79]
print(np_2_boyut[0, 2]) # 1.71
print(np_2_boyut[0][2]) # 1.71
print(np_2_boyut[:, 1:3]) # array([[1.68, 1.71], [59.2, 63.6]])
print(np_2_boyut[1, :]) # array([65.4, 59.2, 63.6, 88.4, 68.7])

# endregion

# region NumPy ile Basit İstatistikler

# Veri Üretme

# np.random.normal() nesnesi ile veri üretebiliriz.
# Bu fonksiyon 3 önemli değer alır:
# Dağılımın ortalaması, dağılımın standart sapması, örnek sayısı

boy = np.round(np.random.normal(1.75, 0.20, 5000), 2)
kilo = np.round(np.random.normal(60.32, 15, 5000), 2)
np_sehir = np.column_stack((boy, kilo))

print(np.mean(np_sehir[:, 0])) # 1.7477839999999996
print(np.median(np_sehir[:, 0])) # 1.75
print(np.corrcoef(np_sehir[:, 0], np_sehir[:, 1])) # array([[1., 0.01970579] [0.01970579, 1.]])
print(np.std(np_sehir[:, 0])) # 0.19851632009484763

# endregion
