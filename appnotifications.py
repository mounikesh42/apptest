import subprocess

# List of package names for the apps to disable notifications for
package_names = [
    'com.estrongs.android.pop',
    'com.camerasideas.instashot',
    'com.kotobee.readerapp',
    'com.qihoo.security',
    'org.scratchjr.android',
    'com.lenovo.anyshare.gps',
    'com.sonymobile.sketch',
    'air.fourdWhiteboard.debug',
    'cn.wps.moffice_eng'
]

# Loop through the list of package names and execute the command for each app
for package_name in package_names:
    command = ['adb', 'shell', 'pm', 'disable-user', '--user', '0', package_name]
    subprocess.run(command)
