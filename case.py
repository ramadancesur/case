from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import webbrowser

driver=webdriver.Chrome()

driver.get("https://testcase.myideasoft.com/")

time.sleep(5)

#arama kısmına ürün yazılması ve listelenmesi
search= driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/div/form/input")

search.send_keys("ürün")

search.send_keys(Keys.RETURN)

time.sleep(5)

#listelenen ürünün detayına tıklanması
driver.find_element(By.CLASS_NAME, "lazyload").click()

time.sleep(3)

#detay ürününün 5 adet olarak seçilmesi
select_element=driver.find_element(By.ID, "qty-input")

select = Select(select_element)

select.select_by_value("5")

time.sleep(5)

#sepete eklenmesi
driver.find_element(By.CLASS_NAME, "add-to-cart-button").click()

time.sleep(5)

#sepet başlığına tıklanması
driver.find_element(By.CLASS_NAME, "cart-amount").click()

time.sleep(5)

#ürün miktarının kontrolü
quantity_input = driver.find_element(By.CLASS_NAME, "form-control")

quantity_value = quantity_input.get_attribute("value")

if quantity_value == "5":
    print("Ürün miktarı 5 olarak ayarlanmış.")
else:
    print("Ürün miktarı yanlış.")

#Tarayıcıyı kapat
driver.quit()