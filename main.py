from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.onet.pl')
sleep(15)