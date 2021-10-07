from models.access_point import AccessPoint


class AccessPointsParser:
    def __init__(self, devices):
        self.raw_string = devices
        self.access_points = self.parse_access_points_strings()

    def parse_access_points_strings(self):
        return self.split_to_strings_of_points(self.raw_string)

    def split_to_strings_of_points(self, main_string):
        points_strings = main_string.split("SSID")
        return self.parse_points_strings(points_strings[1:])

    def parse_points_strings(self, points_strings):
        access_points = []
        for point_string in points_strings:
            ssid, signal, security = self.parse_point_string(point_string)
            access_points.append(AccessPoint(ssid, signal, security))
        return access_points

    def parse_point_string(self, point_string):
        ssid = self.parse_ssid(point_string)
        signal = self.parse_signal(point_string)
        security = self.parse_security(point_string)
        return ssid, signal, security

    def parse_signal(self, line):
        signal_start_index = self.find_index_after_target(line, "SIGNAL:")
        signal_end_index = self.find_end_index(line, signal_start_index)
        return line[signal_start_index:signal_end_index]

    def parse_ssid(self, line):
        ssid_start_index = self.find_index_after_target(line, ":")
        ssid_end_index = self.find_end_index(line, ssid_start_index)
        return line[ssid_start_index:ssid_end_index]

    def parse_security(self, line):
        security_start_index = self.find_index_after_target(line, "SECURITY:")
        security_end_index = self.find_end_index(line, security_start_index)
        return line[security_start_index:security_end_index]

    def find_end_index(self, line, start_index):
        return line.find("\n", start_index)

    def find_index_after_target(self, line, target):
        return line.find(target) + len(target)
