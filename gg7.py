from appium import webdriver
import subprocess
# Define desired capabilities for the app
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'device',
    'appPackage': 'com.estrongs.android.pop',
    'appActivity': 'com.estrongs.android.pop.view.FileExplorerActivity',
    'noReset': True,

}
cmd = 'adb shell pm grant com.estrongs.android.pop android.permission.WRITE_EXTERNAL_STORAGE android.permission.READ_EXTERNAL_STORAGE'

# Run the command and wait for it to finish
subprocess.run(cmd, shell=True, check=True)     
# Start the Appium session
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Get the list of permissions granted to the app
#granted_permissions = driver.execute_script('mobile: getPermissions', {'targetPackage': 'com.estrongs.android.pop'})

# Print the list of granted permissions
#print('Granted permissions:', granted_permissions)

# Close the Appium session
driver.quit()
