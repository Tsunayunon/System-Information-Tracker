---

# Sistem Bilgi İzleyici

"Sistem Bilgi İzleyici" (System Information Tracker), sistem bilgilerinizi toplayıp bir grafik kullanıcı arayüzü (GUI) üzerinden gösteren bir Python uygulamasıdır. Bu uygulama, işletim sistemi, işlemci, bellek ve disk kullanımı gibi önemli bilgileri görsel olarak sunar.

## Başlangıç

Bu projeyi lokal makinenizde çalıştırmak için aşağıdaki adımları izleyin.

### Gereksinimler

Bu projeyi çalıştırabilmeniz için Python'un yüklü olması gerekmektedir. Ayrıca, sistem bilgilerini sorgulamak için `psutil` kütüphanesine ihtiyacınız olacak.

Python'ı [buradan](https://www.python.org/downloads/) indirebilirsiniz.

### Kurulum

Projeyi çalıştırmadan önce gerekli kütüphaneleri yüklemelisiniz. Terminal veya komut istemcisine aşağıdaki komutu girerek `psutil` kütüphanesini yükleyin:

```bash
pip install psutil
```

### Çalıştırma

Projeyi klonladıktan veya indirdikten sonra, projenin bulunduğu dizinde terminal veya komut istemcisini açın ve aşağıdaki komutu çalıştırın:

```bash
python sistem_bilgi_izleyici.py
```

Bu komut, sistem bilgilerinizi toplayan ve bunları bir GUI aracılığıyla gösteren "Sistem Bilgi İzleyici" uygulamasını başlatacaktır.

## Kullanım

Uygulama çalıştırıldığında, sistem bilgileriniz otomatik olarak yüklenir. Bilgileri yenilemek için GUI'deki "Refresh Info" butonuna tıklayabilirsiniz.

## Katkıda Bulunma

Projeye katkıda bulunmak isteyenler, GitHub üzerinden pull request gönderebilir veya yeni özellikler/iyileştirmeler için issue açabilirler.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakınız.

---
