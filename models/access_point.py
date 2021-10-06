class AccessPoint:
    def __init__(self, point_bssid, name, signal):
        self.point_bssid = point_bssid
        self.name = name
        self.signal = signal

    def __repr__(self):
        return f"name: {self.name}\nid:{self.point_bssid}\nsignal: {self.signal}"

    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        return str(self) + other

    def __radd__(self, other):
        return other + str(self)