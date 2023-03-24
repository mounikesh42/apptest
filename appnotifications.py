import subprocess
import time

# Launch app details settings for a package
subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:com.qihoo.security'])

# Wait for a few seconds to ensure that the settings activity is launched
time.sleep(1)

# Simulate screen tap at (500, 650)
subprocess.run(['adb', 'shell', 'input', 'tap', '500', '650'])

# Wait for a few seconds before simulating the second tap
time.sleep(1)

# Simulate screen tap at (500, 550)
subprocess.run(['adb', 'shell', 'input', 'tap', '500', '550'])

time.sleep(1)

subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:com.estrongs.android.pop'])
time.sleep(1)
subprocess.run(['adb', 'shell', 'input', 'tap', '550', '650'])
time.sleep(1)
subprocess.run(['adb', 'shell', 'input', 'tap', '500', '550'])
