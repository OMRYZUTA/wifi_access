from unittest import TestCase

from controllers.access_points_parser import AccessPointsParser
from controllers.os_utils import get_available_devices


class Test(TestCase):
    def setUp(self):
        self.access_points_parser = AccessPointsParser(get_available_devices())

    def test_get_available_networks(self):
        self.assertTrue(len(get_available_devices()) > 1)

    def test_decode_devices_to_str(self):
        self.assertTrue(isinstance(self.access_points_parser.raw_string, str))

    def test_access_points_parser_returns_list_of_points(self):
        self.assertTrue(isinstance(self.access_points_parser.access_points, list))
