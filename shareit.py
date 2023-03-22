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
    activity_name = 'com.lenovo.anyshare.ApMainActivity'

    # Construct the adb command to open the app
    open_cmd = ['adb', 'shell', 'am', 'start', '-n', f'{package_name}/{activity_name}']
    stop_cmd = ['adb', 'shell', 'am', 'force-stop', package_name]

    # Construct the adb command to take a screenshot

    # Open the app using the subprocess module
    # Wait for 10 seconds
    subprocess.Popen(open_cmd)

    time.sleep(5)
    subprocess.run(['adb', 'shell', 'screencap', '/sdcard/shareit.png'])

    subprocess.run(['adb', 'pull', '/sdcard/shareit.png', 'shareit.png'])


    subprocess.Popen(stop_cmd)


    # Load the image
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Load the screenshot image
    img = Image.open('shareit.png')

    # Convert the image to grayscale
    img = img.convert('L')

    # Use pytesseract to recognize the text in the image
    text = pytesseract.image_to_string(img)

    # Check if the recognized text contains "AGREE AND CONTINUE"
    if "AGREE AND CONTINUE" in text:
        print("Permissions failed  for Share IT")
    else:
        print("All Permissions granted for Share It")

# shareit()
