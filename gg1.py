from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11.0'
desired_caps['deviceName'] = 'p'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

el1 = driver.find_element_by_accessibility_id('9')
el1.click()

el2 = driver.find_element_by_accessibility_id('plus')
el2.click()

el3 = driver.find_element_by_accessibility_id('3')
el3.click()

el4 = driver.find_element_by_accessibility_id('equals')
el4.click()

driver.quit()