import subprocess


def get_available_devices():
    return subprocess.check_output(["netsh", "wlan", "show", "network", "mode=Bssid"])
