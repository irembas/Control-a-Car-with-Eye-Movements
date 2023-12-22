
Proje Adı: Göz Hareketleri ile Araba Kontrolü
Proje Özeti
Bu proje, göz hareketlerini algılayarak bir aracı kontrol etmeyi amaçlar. Özellikle omurilik felci gibi hareket kabiliyeti kısıtlı bireyler için tasarlanmıştır. Proje, yüz ve göz tespiti, göz hareketlerinin analizi ve bu bilgilerin bir aracı yönlendirmek için kullanılmasını içerir. Sistem, göz hareketlerini takip eden bir kamera ve bu verileri işleyerek aracı kontrol eden bir mikrodenetleyici üzerine kuruludur.

Kurulum ve Gereksinimler
Yazılım Gereksinimleri:

Python 3.x
OpenCV (cv2)
dlib
numpy
math
serial
Donanım Gereksinimleri:

Kamera (Göz hareketlerini takip etmek için)
Mikrodenetleyici (Arduino veya benzeri)
Bluetooth modülü (Arduino ile bilgisayar arasında haberleşme için)
Uygun bir araba modeli (Kontrol edilecek)
Kurulum Adımları
Gerekli Kütüphanelerin Kurulumu: Yukarıda listelenen Python kütüphanelerini sisteminize kurun.
Arduino Ayarları: Arduino'yu bilgisayarınıza bağlayın ve gerekli Bluetooth ayarlarını yapın.
Kamera Ayarı: Kameranızı bilgisayara bağlayın ve doğru çalıştığından emin olun.
Kullanım Talimatları
Proje Dosyaları: module.py, main.py ve test.py dosyalarını projenin ana dizinine yerleştirin.
main.py dosyasını çalıştırın. Bu, kamera üzerinden göz hareketlerini takip edip, bu verileri Arduino'ya iletecektir.
Göz hareketlerinize göre aracın kontrolünü sağlayın. Örneğin, gözlerinizi sağa çevirerek aracı sağa yönlendirebilirsiniz.
Sistem Mimarisi
Yüz ve Göz Tespiti: dlib ve OpenCV kütüphaneleri kullanılarak yüz ve göz tespiti yapılır.
Göz Takibi ve Komut Oluşturma: Gözlerin açık ya da kapalı olduğu ve bakış yönü module.py içindeki fonksiyonlarla tespit edilir. Bu bilgiler Arduino'ya Bluetooth üzerinden iletilir.
Araba Kontrolü: Arduino, alınan komutlara göre aracı hareket ettirir.
Güvenlik ve Performans Önerileri
Güvenlik: Deney yaparken güvenli bir alanda olun ve ani hareketlere karşı dikkatli olun.
Performans: Aydınlatma ve kamera kalitesi, sistemin doğruluğunu etkileyebilir. Optimal sonuçlar için iyi aydınlatılmış bir ortamda test yapın.
Sorun Giderme
Eğer sistem düzgün çalışmıyorsa, kamera ve Bluetooth bağlantılarınızı kontrol edin.
Göz tespiti doğru çalışmıyorsa, aydınlatmayı ayarlayın veya kameranın konumunu değiştirin.
