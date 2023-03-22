from appium import webdriver

# Set desired capabilities for the appium server
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'device',
    'appPackage': 'com.estrongs.android.pop',
    'appActivity': '.view.FileExplorerActivity'
}

# Start the appium server
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Get the app permissions
app_info = driver.execute_script('mobile: getNotifications', {'packageName': 'com.estrongs.android.pop'})
permissions = app_info['permissions']
print(permissions)
# Check if the app has the RECEIVE_NOTIFICATIONS permission
for permission in permissions:
    if permission['permission'] == 'android.permission.RECEIVE_NOTIFICATIONS':
        print('The app has RECEIVE_NOTIFICATIONS permission')
        break
else:
    print('The app does not have RECEIVE_NOTIFICATIONS permission')

# Quit the driver
driver.quit()
