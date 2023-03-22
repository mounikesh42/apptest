import subprocess
from appium import webdriver
from PIL import Image
import pytesseract
from PIL import Image
import time
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'Android Emulator',
    'appPackage': 'com.qihoo.security',
    'appActivity': 'com.qihoo.security.ui.main.HomeActivity',
    'autoGrantPermissions': False,
    'noReset':True
}

def safe():

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(5)
    perms = driver.get_screenshot_as_file('safe.png')
    driver.quit()

    # Load the image
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Load the screenshot image
    img = Image.open('safe.png')
    # Convert the image to grayscale
    img = img.convert('L')

    # Use pytesseract to recognize the text in the image
    text = pytesseract.image_to_string(img)

    # Check if the recognized text contains "AGREE AND CONTINUE"
    if "Boost Clean" in text:
        print("Permissions Granted  for SAFE ")
    else:
        print("Permissions failed for SAFE APP")

# safe()
