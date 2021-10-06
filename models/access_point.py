class AccessPoint:
    def __init__(self, point_id, name, signal):
        self.point_id = point_id
        self.name = name
        self.signal = signal

    def __repr__(self):
        return f" id:{self.id}\n name: {self.name}\n signal: {self.signal}"
