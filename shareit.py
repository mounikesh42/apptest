# Import the Appium Python Client
from appium import webdriver
from PIL import Image
import pytesseract
from PIL import Image
import subprocess
import time
# Set up the Appium desired capabilities

def shareit():

    package_name = 'com.lenovo.anyshare.gps'
    output = subprocess.check_output(["adb", "shell", "appops", "get", package_name, "MANAGE_EXTERNAL_STORAGE"]).decode("utf-8")

    if "allow" in output:
        print("All Permissions granted  For shareit app")
    else:
        print("Permissions not granted")


# shareit()
