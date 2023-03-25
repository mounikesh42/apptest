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

time.sleep(1)


subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:com.camerasideas.instashot'])
time.sleep(1)
subprocess.run(['adb', 'shell', 'input', 'tap', '550', '650'])
time.sleep(1)
subprocess.run(['adb', 'shell', 'input', 'tap', '500', '550'])

time.sleep(1)

subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:com.kotobee.readerapp'])
time.sleep(1)
subprocess.run(['adb', 'shell', 'input', 'tap', '550', '650'])
time.sleep(1)
subprocess.run(['adb', 'shell', 'input', 'tap', '500', '550'])


time.sleep(1)

subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:com.qihoo.security'])
time.sleep(1)
subprocess.run(['adb', 'shell', 'input', 'tap', '550', '650'])
time.sleep(1)
subprocess.run(['adb', 'shell', 'input', 'tap', '500', '550'])

time.sleep(1)

subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:org.scratchjr.android'])
time.sleep(1)
subprocess.run(['adb', 'shell', 'input', 'tap', '550', '650'])
time.sleep(1)
subprocess.run(['adb', 'shell', 'input', 'tap', '500', '550'])


time.sleep(1)

subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:com.lenovo.anyshare.gps'])
time.sleep(1)
subprocess.run(['adb', 'shell', 'input', 'tap', '550', '650'])
time.sleep(1)
subprocess.run(['adb', 'shell', 'input', 'tap', '500', '550'])


time.sleep(1)

subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:com.sonymobile.sketch'])
time.sleep(1)
subprocess.run(['adb', 'shell', 'input', 'tap', '550', '650'])
time.sleep(1)
subprocess.run(['adb', 'shell', 'input', 'tap', '500', '550'])


time.sleep(1)

subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:air.fourdWhiteboard.debug'])
time.sleep(1)
subprocess.run(['adb', 'shell', 'input', 'tap', '550', '650'])
time.sleep(1)
subprocess.run(['adb', 'shell', 'input', 'tap', '500', '550'])

time.sleep(1)

subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.APPLICATION_DETAILS_SETTINGS', '-d', 'package:cn.wps.moffice_eng'])
time.sleep(1)
subprocess.run(['adb', 'shell', 'input', 'tap', '550', '650'])
time.sleep(1)
subprocess.run(['adb', 'shell', 'input', 'tap', '500', '550'])
