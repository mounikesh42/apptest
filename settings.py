from appium import webdriver



def settings():

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

# Close the driver session
