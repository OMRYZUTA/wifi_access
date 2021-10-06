import subprocess


def get_available_devices():
    result = subprocess.getoutput(" sudo nmcli -f  SSID,BSSID,SIGNAL -m tabular -t dev wifi list")
    return result
