import subprocess
import time
scratch = "org.scratchjr.android"

# Define the permissions to grant
scratchpermissions = ["android.permission.READ_EXTERNAL_STORAGE", "android.permission.RECORD_AUDIO", "android.permission.CAMERA"]

# Loop through the permissions and execute the 'pm grant' command for each one
for scratchpermission in scratchpermissions:
    cmd = f"adb shell pm grant {scratch} {scratchpermission}"
    subprocess.run(cmd, shell=True)



sketch ="com.sonymobile.sketch"

sketchpermissions = ["android.permission.READ_EXTERNAL_STORAGE", "android.permission.WRITE_EXTERNAL_STORAGE"]

for sketchpermission in sketchpermissions:
    cmd = f"adb shell pm grant {sketch} {sketchpermission}"
    subprocess.run(cmd, shell=True)


edlp = 'com.erudex.eduapp.mauritius'

edlppermissions = ["android.permission.READ_EXTERNAL_STORAGE", "android.permission.WRITE_EXTERNAL_STORAGE"]

for edlppermission in edlppermissions:
    cmd = f"adb shell pm grant {edlp} {edlppermission}"
    subprocess.run(cmd, shell=True)



esfile = 'com.estrongs.android.pop'

esfilepermissions = ["android.permission.READ_EXTERNAL_STORAGE", "android.permission.WRITE_EXTERNAL_STORAGE","android.permission.ACCESS_MEDIA_LOCATION"]

for esfilepermission in esfilepermissions:
    cmd = f"adb shell pm grant {esfile} {esfilepermission}"
    subprocess.run(cmd, shell=True)


inshot = 'com.camerasideas.instashot'

inshotpermissions = ["android.permission.READ_EXTERNAL_STORAGE", "android.permission.WRITE_EXTERNAL_STORAGE"]

for inshotpermission in inshotpermissions:
    cmd = f"adb shell pm grant {inshot} {inshotpermission}"
    subprocess.run(cmd, shell=True)



koto = 'com.kotobee.readerapp'

kotopermissions = ["android.permission.READ_EXTERNAL_STORAGE", "android.permission.WRITE_EXTERNAL_STORAGE"]

for kotopermission in kotopermissions:
    cmd = f"adb shell pm grant {koto} {kotopermission}"
    subprocess.run(cmd, shell=True)



safe = 'com.qihoo.security'

safepermissions = ["android.permission.READ_EXTERNAL_STORAGE", "android.permission.WRITE_EXTERNAL_STORAGE"]

for safepermission in safepermissions:
    cmd = f"adb shell pm grant {safe} {safepermission}"
    subprocess.run(cmd, shell=True)


whiteboard = 'air.fourdWhiteboard.debug'

whiteboardpermissions = ["android.permission.READ_EXTERNAL_STORAGE", "android.permission.WRITE_EXTERNAL_STORAGE"]

for whiteboardpermission in whiteboardpermissions:
    cmd = f"adb shell pm grant {whiteboard} {whiteboardpermission}"
    subprocess.run(cmd, shell=True)




subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.MANAGE_APP_ALL_FILES_ACCESS_PERMISSION', '-d', 'package:cn.wps.moffice_eng'])

# Wait for 2 seconds
time.sleep(2)

subprocess.run(['adb', 'shell', 'input', 'tap', '500', '550'])



# Tap on Allow button

time.sleep(1)

wps = 'cn.wps.moffice_eng'
wpsactivity = 'cn.wps.moffice.documentmanager.PreStartActivity2'
subprocess.run( ['adb', 'shell', 'am', 'start', '-n', f'{wps}/{wpsactivity}'])

time.sleep(5)
subprocess.run(['adb', 'shell', 'input', 'tap', '46', '956'])
time.sleep(3)

subprocess.run(['adb', 'shell', 'input', 'tap', '603', '1770'])





subprocess.run(['adb', 'shell', 'am', 'start', '-a', 'android.settings.MANAGE_APP_ALL_FILES_ACCESS_PERMISSION', '-d', 'package:com.lenovo.anyshare.gps'])

# Wait for 2 seconds
time.sleep(2)



# Tap on Allow button
subprocess.run(['adb', 'shell', 'input', 'tap', '500', '550'])

time.sleep(2)
shareit = 'com.lenovo.anyshare.gps'
shareitactivity = 'com.lenovo.anyshare.ApMainActivity'
subprocess.run( ['adb', 'shell', 'am', 'start', '-n', f'{shareit}/{shareitactivity}'])

time.sleep(4)

subprocess.run(['adb', 'shell', 'input', 'tap', '561', '1660'])
