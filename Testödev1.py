from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.kodlama.io/")
sleep(2)

kurslar = driver.find_elements(By.CLASS_NAME, ("course-listing-extra-info"))
#kursları sayar
kursSayisi = len(kurslar)

if kursSayisi == 6:
    print("Kurs sayısı 6'ya denk 😁"), " Toplam Kurs adeti:" + str(kursSayisi)
else:
    print("Kurs sayısı testi başarısız ❌")

driver.save_screenshot(str(date.today) + '(1).png')

sleep(5)

searchBtn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[3]/form/div/input")
searchBtn.click()
searchBtn.send_keys("Senior")
x = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[3]/div/div[1]/a/div/div[2]")
driver.save_screenshot(str(date.today()) + '(1).png')
sleep(5)
x = x.text
if x == "Senior Yazılım Geliştirici Yetiştirme Kampı (.NET)":
    print("Doğru Çalıştı")
else:
    print("Yanlış Cevap")

input()