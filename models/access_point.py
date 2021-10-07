class AccessPoint:
    def __init__(self, ssid, signal, security):
        self.ssid = ssid
        self.signal = signal
        self.security = security

    def __repr__(self):
        return f"name: {self.ssid}\nsignal: {self.signal}\nsecurity:{self.security}"

    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        return str(self) + other

    def __radd__(self, other):
        return other + str(self)
