from selenium import webdriver

PATH = "assets/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")

print(driver.title)

driver.close()