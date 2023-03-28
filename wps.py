import subprocess


def wps():
    package_name = "cn.wps.moffice_eng"
    output = subprocess.check_output(["adb", "shell", "appops", "get", package_name, "MANAGE_EXTERNAL_STORAGE"]).decode("utf-8")

    if "allow" in output:
        print("WPS:Granted")
    else:
        print("WPS:Failed")
