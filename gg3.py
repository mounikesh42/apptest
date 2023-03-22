from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import subprocess
import time

# Set up desired capabilities for the device and app
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '12'
desired_caps['deviceName'] = 'p'
desired_caps['appPackage'] = 'com.estrongs.android.pop'
desired_caps['appActivity'] = 'com.estrongs.android.pop.view.FileExplorerActivity'
desired_caps['autoGrantPermissions'] = True

# Initialize the driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Wait for the app to launch
time.sleep(5)

# Get the package name of the app
app_package = desired_caps['appPackage']

# Use subprocess to execute the dumpsys command and get the output
output = subprocess.check_output(f"adb shell dumpsys package {app_package}", shell=True).decode()

# Parse the output to find the permissions required by the app
permissions = [line.strip() for line in output.split("\n") if "android.permission" in line]

# Print the permissions required by the app
print("Permissions required by the app:")
for permission in permissions:
    print(permission)

# Quit the driver
driver.quit()
