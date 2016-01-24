from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://www.packtpub.com/packt/offers/free-learning")

assert "Free Learning" in driver.title

driver.find_elements_by_class_name("float-left")[2].click()
emailElement = driver.find_elements_by_name("email")[1]
emailElement.send_keys("Enter Your Email")
passwordElement = driver.find_elements_by_name("password")[1]
passwordElement.send_keys("Enter your Password")
driver.find_elements_by_name("op")[2].click()

assert "display: block;" in driver.find_element_by_id("account-bar-logged-in").get_attribute("style")

button = driver.find_element_by_class_name("twelve-days-claim")
driver.execute_script("arguments[0].click()", button)