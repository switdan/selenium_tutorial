from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://automationpractice.techwithjatin.com/')

driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
signup_button = driver.find_element(By.XPATH , '//a[@title="Log in to your customer account"]')
signup_button.click()

email_registration_field = driver.find_element(By.XPATH , '//*[@id="email_create"]')
email_registration_field.send_keys("tester@gmail.com")

register_button = driver.find_element(By.XPATH , '//*[@id="SubmitCreate"]')
register_button.click()
sleep(5)

# shadow_host = driver.find_element(By.ID, "usercentrics-root")
# shadow_root = shadow_host.shadow_root
# accept_button = shadow_root.find_element(By.CSS_SELECTOR, 'button[data-testid="uc-accept-all-button"]')