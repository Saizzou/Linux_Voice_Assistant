# Linux Ses Assistanı

Sisteminizde kolayca çalışabilir bir Ses Assistanı. Linux üzerinde birçok ses Modulü ile sorun çıkmasından dolayı yapılmış bir projedir. Eğitim amaçlıdır. 

## Yükleme

Sox kurulumu yapmanız gerekir böylece Terminal üstü ses dosyalarını çalıştırmanız mümkün olur. Ek Python kütüphanelerine gerek duymazsınız. Ayrıca [pip](https://pip.pypa.io/en/stable/) ile kurulumlar gerektirir:

```bash
pip install gtts
pip install speechrecognition
$ sudo apt install sox
```

## Kullanım

```python
def fkomut_alma():
....
komut = fkomut_alma() # komutları algılayan kısım
fkonusma('Bu fonksiyon ile ses çıktıları alırsınız')
```

## Katılım
Tamamen eğitim amaçlıdır. Aklınıza takılan ek konular olursa [koddunyam](http://forum.koddunyam.net) üzerinden sorularınızı yöneltebilirsiniz!
