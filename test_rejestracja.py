from selenium.webdriver.support.select import Select
from data_tools import *
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By


class RegisterNewUserTest(unittest.TestCase):
    def setUp(self):
        # Preconditions
        # 1. Open main page
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://automationpractice.techwithjatin.com/')
        self.driver.implicitly_wait(10)
        # 2. User is unlogged - there is no need any action


    def test_positive_registration(self):
        # Steps
        # 1. Click on "Sign in"
        self.driver.find_element(By.XPATH, '//a[@title="Log in to your customer account"]').click()

        # 2. Type the email address
        generated_email = TestData.DATA_EMAIL
        self.driver.find_element(By.XPATH, '//*[@id="email_create"]').send_keys(generated_email)

        # 3. Click "Create an account" button
        self.driver.find_element(By.XPATH, '//*[@id="SubmitCreate"]').click()

        # 4. Choose the gender
        if TestData.DATA_GENDER == Gender.MALE:
            self.driver.find_element(By.XPATH,
                                '/html/body/div/div[2]/div/div[3]/div/div/form/div[1]/div[1]/div[1]/label').click()
        elif TestData.DATA_GENDER == Gender.FEMALE:
            self.driver.find_element(By.XPATH,
                                '/html/body/div/div[2]/div/div[3]/div/div/form/div[1]/div[1]/div[2]/label').click()

        # 5. Type the first name
        self.driver.find_element(By.XPATH, '//*[@id="customer_firstname"]').send_keys(TestData.DATA_FIRST_NAME)

        # 6. Type the last name
        self.driver.find_element(By.XPATH, '//*[@id="customer_lastname"]').send_keys(TestData.DATA_LAST_NAME)

        # 7. Check if the email are the same as typed earlier
        existed_email =  self.driver.find_element(By.XPATH, '//*[@id="email"]').get_attribute('value')
        self.assertEqual(generated_email, existed_email)

        # 8. Leave the same email
        self.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("")

        # 9. Type the password
        self.driver.find_element(By.XPATH, '//*[@id="passwd"]').send_keys(TestData.DATA_PASSWORD)

        # 10. Chose the day of birth
        Select(self.driver.find_element(By.XPATH, '//*[@id="days"]')).select_by_index(TestData.DATA_DAY_OF_BIRTH)

        # 11. Chose the month of birth
        Select(self.driver.find_element(By.XPATH, '//*[@id="months"]')).select_by_index(TestData.DATA_DAY_OF_MONTH)

        # 12. Chose the year of birth
        Select(self.driver.find_element(By.XPATH, '//*[@id="years"]')).select_by_value(str(TestData.DATA_DAY_OF_YEAR))

        # 13. Click "Submit" button
        self.driver.find_element(By.XPATH, '//*[@id="submitAccount"]').click()

        # 14. "My account" page shown
        self.assertEqual("https://automationpractice.techwithjatin.com/my-account", self.driver.current_url)


    def tearDown(self):
        # Close
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()