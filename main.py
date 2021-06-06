'''
Linux Ses Assistanıdır! Birçok ses kütüphanesi ile
çakışma yaşayan yada ALSA ayarları gerektiren eklemeler olmadan
terminal'den "$sudo apt install sox" ile sistemsel sesleri
kullanır. "sox" terminalden sesli çıktı vermenizi sağlayacaktır!
'''
import os
from gtts import gTTS
import speech_recognition as sr
import webbrowser
from time import ctime
import random
import ccxt
kraken = ccxt.kraken()

r = sr.Recognizer() #ses algilama fonksiyonu
cagri = False

class Kisi:
    name = 'Sai' # Kendi isminizi girin!!

# Seslenmeyi yaziya ceviren tanim
def audio_girisi(giris=False):
    with sr.Microphone() as mic:
        if giris:
            konus(giris)
        audio = r.listen(mic)
        konusma_verisi = ''
        try:
            konusma_verisi = r.recognize_google(audio, language='TR-tr')
        except sr.UnknownValueError:
            print("Tanimlanamadi")
        except sr.RequestError:
            print("Sisteme ulasilamiyor")
        print(f">> {konusma_verisi.lower()}")
    return konusma_verisi.lower()

def konus(audio_string):
    tts = gTTS(text=audio_string, lang='tr')
    audio_verisi = 'audio.mp3'
    tts.save(audio_verisi)
    os.system('play ' + audio_verisi + ' tempo 1.3') #sox paketi ile konusmayi saglar
    os.remove(audio_verisi) #audio.mp3 silme komutu

def kripto_mana():
    for trade in kraken.fetch_trades('MANA/EUR'):
        mana = float(f'{trade["price"]}')
        return mana


def kripto_btc():
    for trade in kraken.fetch_trades('BTC/EUR'):
        btc = float(f'{trade["price"]}')
        return btc


def there_exists(terms):
    for term in terms:
        if term in konusma_verisi:
            return True


def cevaplama(konusma_verisi):
    import time
    global cagri
    def check_uhr():
        time = ctime().split(" ")[3].split(":")[0:2]
        dakika = time[1]
        return dakika


    if there_exists(['sen kimsin', 'adın ne', 'sana nasıl hitap edeyim']):
        ich_bin = ["Adım Katya", "Ben senin çılgın ses asistanın Katyayım", "Katya"]
        ich = ich_bin[random.randint(0, len(ich_bin) - 1)]
        konus(ich)
        cagri = False


    if there_exists(['katya bana karşı ne hissediyorsun', 'benden hoşlanıyor musun', 'katya beni seviyor musun']):
        sevgi_sorusu = [f"Neden böyle birşey sordun {Kisi.name}", "Tabiiki, sonuçta sen benim yaratıcımsın",
                   "Seni gayet sevecen buluyorum aslında, tabii arada sırada bana iki güncelleme yapsan fena olmaz", f"Kendini yalnız mı hissediyorsun {Kisi.name}? Bana birkaç güncelleme yazsan daha çok vakit geçirebiliriz aslında"]
        ant = sevgi_sorusu[random.randint(0, len(sevgi_sorusu) - 1)]
        konus(ant)


    if there_exists(['hayatın amacı ne', 'neden dünyadayız', 'yaşamanın amacı nedir']):
        yasama_amaci = [f"o kadarını bilemem ama senin amacın kod yazmak! Bunu sakın unutma ve hazır bana böyle sorular sormuşken bana yeni şeyler öğretmelisin"]
        ant = yasama_amaci[random.randint(0, len(yasama_amaci) - 1)]
        konus(ant)


    #Uhr
    elif there_exists(["saat kaç","saati söyle"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            saat = '12'
        else:
            saat = time[0]
        dakika = time[1]
        zaman = f'Saat {saat} {dakika}'
        konus(zaman)

    elif there_exists(["alarm kur", "alarm oluştur"]):
        alarm = konusma_verisi.split("alarm")[-1]
        os.system("sleep {}h && play alarm.mp3".format(alarm))


    # Youtube
    elif there_exists(['youtube de ara']):
        suche = konusma_verisi.split('youtube de ara')[-1]
        url = f"https://www.youtube.com/results?search_query={suche}"
        konus('Bakalım Youtubede neler bulabilirim')
        webbrowser.get().open(url)


    # Duckduckgo
    elif there_exists(['internette ara']):
        suche_net = konusma_verisi.split('internette ara')[-1]
        url_net = f"https://duckduckgo.com/?q={suche_net}&t=ffab&atb=v256-1&ia=web"
        konus('Bakalım internette senin için neler bulabilirim')
        webbrowser.get().open(url_net)


    # Github
    elif there_exists(['github sayfamı aç']):
        url_github = f"https://github.com/Saizzou"
        konus('Yeni Projelerin mi var? Çok heyecanlıyım')
        webbrowser.get().open(url_github)


    # Netflix
    elif there_exists(['netflixi aç']):
        url_netflix = f"https://www.netflix.com"
        konus('Yine canın sıkıldı değil mi?')
        webbrowser.get().open(url_netflix)


    # Amazon
    elif there_exists(['gitti gidiyor aç']):
        url_amazon = f"https://www.gittigidiyor.com.tr"
        konus('Çok para harcamamalısın dikkat et')
        webbrowser.get().open(url_amazon)


    #Screenshot
    elif there_exists(['ekran görüntüsü al']):
        konus("Alınacak alanı seçebilirsin")
        os.system('gnome-screenshot -a')


    # Programme
    elif there_exists(['sanal serverleri aç']):
        konus("VM Player hemen açılıyor")
        os.system('vmplayer &')

    elif there_exists(['pythonu aç']):
        konus("PyCharm programını açıyorum")
        os.system('charm &')

    elif there_exists(['javayı aç']):
        konus("Java hemen açılıyor")
        os.system('~/Programms/eclipse-java-2021-03-R-linux-gtk-x86_64/eclipse/eclipse &')

    elif there_exists(['proje tablosu hazırlamalıyım']):
        konus("draw io yu açıyorum o zaman")
        os.system('drawio &')

    elif there_exists(['tablet çizimi yapmam gerek']):
        konus("bileğine kuvvet o zaman hemen açıyorum")
        os.system('xournalpp &')

    elif there_exists(['notlarımı açar mısın']):
        konus("notlar nerdeydi hah şurda notların")
        os.system('cherrytree &')

    elif there_exists(['video kayıt programını aç']):
        konus("Yeni videolar mı yolda? Hemen hazırlıklara başlıyorum")
        os.system('obs &')


    # System befehle
    elif there_exists(['katja bilgisayarı yeniden başlatır mısın']):
        konus('Bilgisayarı yeniden başlatıyorum tekrar onaylar mısın')
        sicher = audio_girisi()
        time.sleep(2)
        if 'onaylıyorum' in sicher:
            os.system('reboot')

    elif there_exists(['katja bilgisayarı kapatır mısın']):
        konus('Bilgisayarı kapatırsan bende kapanırım. Emin misin?')
        sicher = audio_girisi()
        time.sleep(2)
        if 'evet' in sicher:
            os.system('shutdown')

    elif there_exists(['güncelleme yap','bilgisayarı güncelle']):
        konus("Güncelleme başlamak üzere. Bakalım ne gibi yenilikler var. Şifre girmen gerekebilir bakar mısın?")
        os.system('sudo apt update')
        konus("Güncelleme işlemi bitti. Hazır yeni paketleri okumuşken yükseltelim")
        os.system('sudo apt upgrade')
        konus("Yükseltme işlemi bitti. Kendimi taptaze hissediyorum")



while True:

    konusma_verisi = audio_girisi()
    cevaplama(konusma_verisi)
