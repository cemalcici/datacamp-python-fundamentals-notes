# region Fonksiyonlar

# Tekrar kullanılabilir kod yapılarıdır.
# Belirli problemleri çözerler.
# Hazır yapılardan çağrılabilirler (type() gibi) veya geliştirici tarafından oluşturulabilirler

# max(): Bir listenin maksimum değerini verir.

aile = [1.73, 1.68, 1.71, 1.89]

en_uzun = max(aile)
print(en_uzun) # 1.89

# round(): Bir değeri belirlenen ondalık kısma göre yuvarlar

print(round(1.68, 1)) # 1.7
print(round(1.68)) # 2

# help(): Bir nesne hakkında bilgi almamızı sağlar.

help(round) # round() fonksiyonu hakkında bilgi verir.

# Basit bir Google araması ile amacınıza yönelik, muhtemelen daha önce yazılmış, fonksiyonu bulabilirsiniz.

# endregion

# region Metotlar

# Bir listedeki maksimum değeri bulmak için max() fonksiyonu kullanabiliriz
# Bir listenin toplam kaç elemana sahip olduğunu bulmak için len() fonksiyonunu kullanabiliriz
# Peki, listedeki bir elemanın indeksini bulmak veya bir listeyi tersten sıralamak için ne yapabiliriz?
# İşte bize burada metotlar yardımcı oluyor.
# Metotlar, bir nesneye bağlı fonksiyonlardır.

# region Liste Metotları

aile = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]

# aile listesi üzerinde index() metodu kullanıldı.
print(aile.index("mom")) # 4
# aile listesi üzerinde count() metodu kullanıldı.
print(aile.count(1.73)) # 1

# endregion

# region Karakter Dizisi Metotları

kiz_kardes = "liz"

# kiz_kardes karakter dizisi üzerinde capitalize() metodu kullanıldı.
print(kiz_kardes.capitalize()) # Liz
# kiz_kardes karakter dizisi üzerinde replace() metodu kullanıldı.
print(kiz_kardes.replace("z", "sa")) # lisa

# endregion

# Python'da her şey nesnedir ve bu nesnelerin kendi tiplerine yönelik metotları vardır.

print(kiz_kardes.replace("z", "sa")) # lisa
print(aile.replace("z", "sa")) # Hata verir!

# Bazı metotlar ortak olabilir.

print(kiz_kardes.index("z")) # 2
print(aile.index("mom")) # 4

# Listeye eleman eklemek için append() metodu kullanılır.

aile.append("me")
aile.append(1.79)
print(aile) # ['lisa', '1.74', 'emma', 1.68, 'mom', 1.71, 'dad', 1.86, 'me', 1.79]

# endregion

# region Paketler

# Paketler, Python dosyalarından oluşan klasörlerdir.
# Her bir Python dosyası bir modüldür.
# Python'da binlerce paket mevcuttur.

# Python'da bir paket yüklemek için pip aracı kullanılabilir.
# Örneğin Windows'ta NumPy paketini yüklemek için python çalıştıran bir terminale 
# `pip install numpy` komutu yazılabilir.

# Python'da bir paketi çalışma ortamına almak için aşağıdaki yöntemler kullanılabilir.

import numpy # Paket direkt çağrıldı
print(numpy.array([1, 2, 3])) # array([1, 2, 3])

import numpy as np # Pakete takma isim verilerek çağrıldı
print(np.array([1, 2, 3])) # array([1, 2, 3])

from numpy import array # Paketten sadece bir nesne çağrıldı
print(array([1, 2, 3])) # array([1, 2, 3])

# Sonuncu yöntem pek tavsiye edilmez, çünkü mevcut modül içerisinde isim benzerliği oluşabilir
# ve kod okuma sırasında nesnenin nereden geldiği görülemeyebilir

# endregion
