from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

#from android.support.v4.app import NotificationManagerCompat
import subprocess
import time
import os

# Set up desired capabilities for the device and ES File Explorer app

es_file_explorer_caps = {}
es_file_explorer_caps['platformName'] = 'Android'
es_file_explorer_caps['platformVersion'] = '12'
es_file_explorer_caps['deviceName'] = 'p'
es_file_explorer_caps['appPackage'] = 'com.estrongs.android.pop'
es_file_explorer_caps['appActivity'] = 'com.estrongs.android.pop.view.FileExplorerActivity'

    
# Initialize the driver for ES File Explorer
es_file_explorer_driver = webdriver.Remote('http://localhost:4723/wd/hub', es_file_explorer_caps)

# Wait for the app to launch
time.sleep(1)
cmd = 'adb shell pm grant com.estrongs.android.pop android.permission.WRITE_EXTERNAL_STORAGE'

# Run the command and wait for it to finish
subprocess.run(cmd, shell=True, check=True)
# Confirm the presence of ES File Explorer app
assert es_file_explorer_driver.is_app_installed('com.estrongs.android.pop')

es_file_explorer_driver.quit()




# Set up desired capabilities for the device and ShareIt app
shareit_caps = {}
shareit_caps['platformName'] = 'Android'
shareit_caps['platformVersion'] = '12'
shareit_caps['deviceName'] = 'p'
shareit_caps['appPackage'] = 'com.lenovo.anyshare.gps'
shareit_caps['appActivity'] = 'com.lenovo.anyshare.ApMainActivity'
shareit_caps['autoGrantPermissions'] = True

# Initialize the driver for ShareIt
shareit_driver = webdriver.Remote('http://localhost:4723/wd/hub', shareit_caps)

# Wait for the app to launch
time.sleep(1)

# Confirm the presence of ShareIt app
assert shareit_driver.is_app_installed('com.lenovo.anyshare.gps')

# Quit the ShareIt driver
shareit_driver.quit()



desired_caps = {
    'platformName': 'Android',
    'platformVersion': '12',
    'deviceName': 'Android Emulator',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
    'noReset': True
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Navigate to the Notifications settings
driver.start_activity('com.android.settings', '.Settings$ConfigureNotificationSettingsActivity')
time.sleep(1)

# Close the driver session
#driver.quit()

