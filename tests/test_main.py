from unittest import TestCase

from controllers.access_points_parser import AccessPointsParser
from controllers.network_manager import NetworkManager


class Test(TestCase):
    def setUp(self):
        self.network_manager = NetworkManager()
        self.access_points_parser = AccessPointsParser(self.network_manager.get_available_devices())

    def test_get_available_networks(self):
        self.assertTrue(len(self.network_manager.get_available_devices()) > 1)

    def test_access_points_parser_returns_list_of_points(self):
        self.assertTrue(isinstance(self.access_points_parser.access_points, list))
