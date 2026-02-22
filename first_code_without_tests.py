from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://automationpractice.techwithjatin.com/')
driver.implicitly_wait(10)

class Gender:
    MALE = 0
    FEMALE = 1

DATA_EMAIL = "tester1@gmail.com"
DATA_GENDER = Gender.MALE
DATA_FIRST_NAME = "Janusz"
DATA_LAST_NAME = "Kowalski"
DATA_PASSWORD = "12345678!"
DATA_DAY_OF_BIRTH = 7
DATA_DAY_OF_MONTH = 2
DATA_DAY_OF_YEAR = 1990

driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
signup_button = driver.find_element(By.XPATH , '//a[@title="Log in to your customer account"]')
signup_button.click()
print(driver.current_url)

email_registration_field = driver.find_element(By.XPATH , '//*[@id="email_create"]')
email_registration_field.send_keys(DATA_EMAIL)

register_button = driver.find_element(By.XPATH , '//*[@id="SubmitCreate"]')
register_button.click()

sleep(3)
if DATA_GENDER == Gender.MALE:
    driver.find_element(By.XPATH , '/html/body/div/div[2]/div/div[3]/div/div/form/div[1]/div[1]/div[1]/label').click()
elif DATA_GENDER == Gender.FEMALE:
    driver.find_element(By.XPATH , '/html/body/div/div[2]/div/div[3]/div/div/form/div[1]/div[1]/div[2]/label').click()

first_name_field = driver.find_element(By.XPATH , '//*[@id="customer_firstname"]')
first_name_field.send_keys(DATA_FIRST_NAME)

last_name_field = driver.find_element(By.XPATH , '//*[@id="customer_lastname"]')
last_name_field.send_keys(DATA_LAST_NAME)

email_field = driver.find_element(By.XPATH , '//*[@id="email"]')
email_field.send_keys("")

password_field = driver.find_element(By.XPATH , '//*[@id="passwd"]')
password_field.send_keys(DATA_PASSWORD)

dropdown_day_of_birth = driver.find_element(By.XPATH, '//*[@id="days"]')
select = Select(dropdown_day_of_birth)
select.select_by_index(DATA_DAY_OF_BIRTH)

dropdown_month_of_birth = driver.find_element(By.XPATH, '//*[@id="months"]')
select = Select(dropdown_month_of_birth)
select.select_by_index(DATA_DAY_OF_MONTH)

dropdown_month_of_year = driver.find_element(By.XPATH, '//*[@id="years"]')
select = Select(dropdown_month_of_year)
select.select_by_value(str(DATA_DAY_OF_YEAR))

submit_button = driver.find_element(By.XPATH , '//*[@id="submitAccount"]')
submit_button.click()

# sleep(50)

# shadow_host = driver.find_element(By.ID, "usercentrics-root")
# shadow_root = shadow_host.shadow_root
# accept_button = shadow_root.find_element(By.CSS_SELECTOR, 'button[data-testid="uc-accept-all-button"]')