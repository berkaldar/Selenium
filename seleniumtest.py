# bir kütüphaneden dosya import etmek
# kalıp => from {kütüphane -ismi} import {nesne-ismi}
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
#sitenin açılmasını bekle!
sleep(1) #defensive programming
input = driver.find_element(By.NAME, "q") # inputu bul
input.send_keys("Deneme")
sleep(5)
searchBtn = driver.find_element(By.NAME, "btnK")
searchBtn.click()
sleep(5)

