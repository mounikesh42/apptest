from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

# Set up desired capabilities for the device and app
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'p'
desired_caps['appPackage'] = 'com.estrongs.android.pop'
desired_caps['appActivity'] = 'com.estrongs.android.pop.view.FileExplorerActivity'

# Initialize the driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Wait for the app to launch
time.sleep(5)

# Confirm the presence of the app
assert driver.is_app_installed('com.estrongs.android.pop')

# Quit the driver
driver.quit()
