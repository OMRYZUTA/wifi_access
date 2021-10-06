from models.access_point import AccessPoint


class AccessPointsParser:
    def __init__(self, devices):
        self.raw_string = devices
        self.access_points = self.parse_access_points_strings()

    def parse_access_points_strings(self):
        return self.split_to_strings_of_points(self.raw_string)

    def split_to_strings_of_points(self, main_string):
        points_strings = main_string.split("\n")
        return self.parse_points_strings(points_strings)

    def parse_points_strings(self, points_strings):
        access_points = []
        for point_string in points_strings:
            point_id, point_name, point_signal = self.parse_point_string(point_string)
            access_points.append(AccessPoint(point_id, point_name, point_signal))
        return access_points

    def parse_point_string(self, point_string):
        point_id = self.parse_point_id_from_line(point_string)
        name = self.parse_name_from_line(point_string)
        signal = self.parse_signal_from_line(point_string)
        return point_id, name, signal

    def parse_name_from_line(self, line):
        name_end_index = line.find(":")
        return line[:name_end_index].strip()

    def parse_signal_from_line(self, line):
        signal_index = line.rfind(":") + 1
        return line[signal_index:].strip()

    def parse_point_id_from_line(self, line):
        name_end_index = line.find(":") + 1
        signal_index = line.rfind(":")
        return line[name_end_index:signal_index]
