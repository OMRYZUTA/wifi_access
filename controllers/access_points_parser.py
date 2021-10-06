from models.access_point import AccessPoint


class AccessPointsParser:
    def __init__(self, devices):
        self.raw_string = self.parse_raw_string(devices)
        self.access_points = self.parse_access_points_strings()

    def parse_raw_string(self, devices):
        decoded_devices = devices.decode('ascii')
        decoded_devices = decoded_devices.replace("\r", "")
        return decoded_devices

    def parse_access_points_strings(self):
        main_string = self.parse_main_string(self.raw_string)
        return self.split_to_strings_of_points(main_string)

    def parse_main_string(self, decoded_string):
        main_string_parts = decoded_string.split("visible.")
        return main_string_parts[1].strip()

    def split_to_strings_of_points(self, main_string):
        points_strings = main_string.split("\n\n")
        return self.parse_points_strings(points_strings)

    def parse_points_strings(self, points_strings):
        access_points = []
        for point_string in points_strings:
            point_id, point_name, point_signal = self.parse_point_string(point_string)
            access_points.append(AccessPoint(point_id, point_name, point_signal))
        return access_points

    def parse_point_string(self, point_string):
        lines = point_string.splitlines()
        point_id = self.parse_point_id_from_line(lines[0])
        name = self.parse_name_from_line(lines[0])
        signal = self.parse_signal_from_line(lines[5])
        return point_id, name, signal

    def parse_name_from_line(self, line):
        name_index = line.find(":") + 2
        return line[name_index:].strip()

    def parse_signal_from_line(self, line):
        signal_index = line.find(":") + 2
        return line[signal_index:-3].strip()

    def parse_point_id_from_line(self, line):
        lines_parts = line.split(" ")
        return lines_parts[1]
