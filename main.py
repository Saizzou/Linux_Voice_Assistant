'''
Linux Ses Assistanıdır! Birçok ses kütüphanesi ile
çakışma yaşayan yada ALSA ayarları gerektiren eklemeler olmadan
terminal'den "$sudo apt install sox" ile sistemsel sesleri
kullanır. "sox" terminalden sesli çıktı vermenizi sağlayacaktır!
'''
import os
from gtts import gTTS
import speech_recognition as sr


def fkomut_alma():
    algilama = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Komut bekleniyor")
        algilama.pause_threshold = 0.7
        kayit = algilama.listen(mic)
        '''Speech Recognition kütüphanesindeki dinleme fonksiyonu
        baglanti saglanan mikrofon girisi ile kayit yapacaktir.'''
        try:
            print("Algilama basladi...")
            ses_paketi = algilama.recognize_google(kayit,language="TR-tr")
            print("Paket icerigi: ",ses_paketi)
        except Exception as e:
            print(e)
            print("Algilama basarisiz...")
            return "None"
    return ses_paketi

def fkonusma(kayit):
    tts = gTTS(text=kayit,lang='tr')
    ses_dosyasi = 'ses' + '.mp3'
    tts.save(ses_dosyasi)
    os.system('play ' + ses_dosyasi + ' tempo 1.5')

if __name__=='__main__':
    while True:
        komut = fkomut_alma()
        if "selam" in komut:
            fkonusma("merhabalar!")
