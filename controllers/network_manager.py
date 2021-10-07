import subprocess
from shlex import join


class NetworkManager:
    def get_available_devices(self):
        result = subprocess.getoutput(" nmcli -f  SSID,SIGNAL,SECURITY -m multiline -t dev wifi list")
        result = subprocess.getoutput(
            join(['nmcli', '-f', 'SSID,SIGNAL,SECURITY', '-m', 'multiline', '-t', 'dev', 'wifi', 'list']))
        return result

    def connect_access_point(self, access_point, password=None):
        if password is not None:
            result = subprocess.getoutput(
                join(['nmcli', 'dev', 'wifi', 'connect', access_point.ssid, 'password', password]))
        else:
            result = subprocess.getoutput(join(['nmcli', 'dev', 'wifi', 'connect', access_point.ssid]))
        return result

    def open_default_browser(self):
        subprocess.getoutput(
            join(['xdg-open', 'https://www.google.com']))
