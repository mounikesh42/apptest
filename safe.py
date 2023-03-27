import subprocess
from appium import webdriver
from PIL import Image
import pytesseract
from PIL import Image
import time

import subprocess
import time
from appium import webdriver

def safe():


# Set the package name and activity name for the Chrome app
    package_name = 'com.qihoo.security'
    activity_name = 'com.qihoo.security.ui.main.HomeActivity'

    # Construct the adb command to open the app
    open_cmd = ['adb', 'shell', 'am', 'start', '-n', f'{package_name}/{activity_name}']

    subprocess.Popen(open_cmd)

    time.sleep(2)



    stop_cmd = ['adb', 'shell', 'am', 'force-stop', package_name]
    subprocess.Popen(stop_cmd)
    print("Permissions Granted  for SAFE ")





# safe()
