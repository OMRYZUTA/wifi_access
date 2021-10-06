class AccessPoint:
    def __init__(self, point_bssid, name, signal):
        self.point_bssid = point_bssid
        self.name = name
        self.signal = signal

    def __repr__(self):
        return f" id:{self.id}\n name: {self.name}\n signal: {self.signal}"
