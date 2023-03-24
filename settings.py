from appium import webdriver
import subprocess
import time


def settings():

    # Set the package name and activity name
    # package_name = 'com.android.settings'
    # activity_name = 'com.android.settings.Settings$NotificationAppListActivity'
    #
    # # Construct the command
    # cmd = ['adb', 'shell', 'am', 'start', '-n', f'{package_name}/{activity_name}']
    #
    # # Run the command
    # subprocess.run(cmd, check=True)
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '12',
        'deviceName': 'Android Emulator',
        'appPackage': 'com.android.settings',
        'appActivity': '.Settings',
        'noReset': True
    }

    # package_name = 'com.android.settings'
    # activity_name = '.Settings$NotificationAppListActivity'
    #
    # # Construct the adb command to open the app
    # open_cmd = ['adb', 'shell', 'am', 'start', '-n', f'{package_name}/{activity_name}']
    #
    # subprocess.Popen(open_cmd)
    #
    # time.sleep(5)
    #
    #
    #
    # stop_cmd = ['adb', 'shell', 'am', 'force-stop', package_name]
    # subprocess.Popen(stop_cmd)

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # Navigate to the Notifications settings
    # driver.start_activity('com.android.settings', '.Settings$ConfigureNotificationSettingsActivity')
    driver.start_activity('com.android.settings', '.Settings$NotificationAppListActivity')

    

# Close the driver session

settings()
