# Import the Appium Python Client
from appium import webdriver
from PIL import Image
import pytesseract
from PIL import Image
import time
import subprocess
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'Android Emulator',
    'appPackage': 'cn.wps.moffice_eng',
    'appActivity': 'cn.wps.moffice.documentmanager.PreStartActivity2',
    'autoGrantPermissions': False,
    'noReset':True
}

def wps():

    package_name = 'cn.wps.moffice_eng'
    activity_name = 'cn.wps.moffice.documentmanager.PreStartActivity2'

    # Construct the adb command to open the app
    open_cmd = ['adb', 'shell', 'am', 'start', '-n', f'{package_name}/{activity_name}']
    stop_cmd = ['adb', 'shell', 'am', 'force-stop', package_name]

    # Construct the adb command to take a screenshot

    # Open the app using the subprocess module
    # Wait for 10 seconds
    subprocess.Popen(open_cmd)

    time.sleep(5)
    subprocess.run(['adb', 'shell', 'screencap', '/sdcard/wps.png'])

    subprocess.run(['adb', 'pull', '/sdcard/wps.png', 'wps.png'])


    # Load the image
    subprocess.Popen(stop_cmd)

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Load the screenshot image
    img = Image.open('wps.png')

    # Convert the image to grayscale
    img = img.convert('L')

    # Use pytesseract to recognize the text in the image
    text = pytesseract.image_to_string(img)

    # Check if the recognized text contains "AGREE AND CONTINUE"
    if "START" in text:
        print("Permissions failed for WPS APP")
    else:
        print("Permissions granted for wps APP")
