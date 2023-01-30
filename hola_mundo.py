import imp
from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;

driver = webdriver.Chrome(executable_path="C:\drivers_selenium\chromedriver_win32\chromedriver.exe")

driver.get("https://demoqa.com/text-box")
print("Hola")
print(driver.title)
driver.close()