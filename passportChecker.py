from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import smtplib

# Girilecek bilgileri giriniz.
tcNumarasi = "***"
sifre = "***"

# driverımızı tanıtıyorum.
driver = webdriver.Chrome()

class E_Devlet():
    # class üzerindeki değişkenlerimizi giriyoruz.
    def __init__(self,tcNumarasi,sifre):
        self.browser = driver
        self.tcNumarasi = tcNumarasi
        self.sifre = sifre
    def signIn(self):
        # sayfamızı tam ekran yapıyoruz.
        self.browser.maximize_window()
        # giriş sayfamız.
        self.browser.get("https://giris.turkiye.gov.tr/Giris/gir")

        # 1 sn bekletiyoruz.
        time.sleep(1)

        # gerekli bilgileri giriyoruz.
        username = self.browser.find_element(By.XPATH, "//*[@id='tridField']")
        password = self.browser.find_element(By.XPATH,"//*[@id='egpField']")

        # girilen bilgileri gerekli yerlere gönderiyoruz.
        username.send_keys(self.tcNumarasi)
        password.send_keys(self.sifre)

        time.sleep(1)

        # giriş yap butonuna tıklıyoruz.
        self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div[2]/input[4]").click()
        

        time.sleep(1)
        # pasaport durum sorgulama linkine gidiyoruz.
        self.browser.get("https://www.turkiye.gov.tr/nvi-pasaport-basvuru-durum-sorgu")
        time.sleep(1)
        # gerekli butonlara tıklıyoruz.
        self.browser.find_element(By.XPATH,"//*[@id='kendi']").click()
        time.sleep(1)
        self.browser.find_element(By.XPATH,"//*[@id='mainForm']/fieldset/div[3]/input[1]").click()

        # sonucumuzu alıp karşılaştırıyoruz. Buna göre bir sonuç döndürüyoruz.
        result = self.browser.find_element(By.XPATH,"//*[@id='contentStart']/div/dl/dd[7]").text
        time.sleep(5)
        if(result == 'Başvurunuz basım öncesi kontrol aşamasındadır.'):
            self.browser.get("https://giphy.com/gifs/spongebob-squarepants-sad-crying-BEob5qwFkSJ7G/fullscreen")
            time.sleep(2)
        else:
            self.browser.get("https://giphy.com/gifs/season-17-the-simpsons-17x10-xT5LMHxhOfscxPfIfm/fullscreen")
            time.sleep(2)
        self.browser.close()

              

a = E_Devlet(tcNumarasi,sifre)
a.signIn()
