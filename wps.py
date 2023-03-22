# Import the Appium Python Client
from appium import webdriver
from PIL import Image
import pytesseract
from PIL import Image
import time
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'Android Emulator',
    'appPackage': 'cn.wps.moffice_eng',
    'appActivity': 'cn.wps.moffice.documentmanager.PreStartActivity2',
    'autoGrantPermissions': False,
    'noReset':True
}

def wps():

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(5)
    perms = driver.get_screenshot_as_file('wps.png')
    driver.quit()

    # Load the image
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
