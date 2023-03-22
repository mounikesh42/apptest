# Import the Appium Python Client
from appium import webdriver
from PIL import Image
import pytesseract
from PIL import Image
# Set up the Appium desired capabilities
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'Android Emulator',
    'appPackage': 'com.lenovo.anyshare.gps',
    'appActivity': 'com.lenovo.anyshare.ApMainActivity',
    'autoGrantPermissions': False,
    'noReset':True

}

def shareit():
# Connect to the Appium server
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # Get the list of permissions granted to the app
    # perms = driver.get_permissions('com.lenovo.anyshare.gps')
    perms = driver.get_screenshot_as_file('shareit.png')

    # Print the list of permissions
    # print(perms)

    # Quit the driver
    driver.quit()




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
