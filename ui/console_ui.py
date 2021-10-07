from collections import defaultdict

from controllers.access_points_parser import AccessPointsParser
from controllers.network_manager import NetworkManager


class ConsoleUI:
    def __init__(self):
        self.network_manager = NetworkManager()
        self.main_menu_choices_operator = None
        self.access_points = self.set_access_points()
        self.user_continue = True
        self.set_main_menu_operator()

    opening_message = "Hi there, please select_one of the options"
    quit_message = "If you want to quit, please insert q"
    main_menu_options = ["Show available access points", "Connect to access point", "Open google in browser "]
    the_best_network = "The Best Network: "
    choose_wifi_message = "Please enter the name of the network you want to connect or q to quit"

    def print_access_points(self):
        self.print_best_option()
        for index, access_point in enumerate(list(self.access_points.values())[1:], 2):
            print(f"{index}. {access_point}\n")
        print()

    def print_best_option(self):
        print('*' * 8)
        print(ConsoleUI.the_best_network)
        print(f"1. {list(self.access_points.values())[0]}")
        print('*' * 8)

    def operate_connect_to_access_point(self):
        print(ConsoleUI.choose_wifi_message)
        network_exist = False
        while not network_exist:
            result = input()
            if result.lower() == 'q':
                return
            if self.check_network_exist(result):
                self.connect_to_existing_access_point(result)
                network_exist = True

    def operate_open_google_in_browser(self):
        self.network_manager.open_default_browser()

    def operate_quit(self):
        print("shutting down app..")
        self.user_continue = False

    def operate_invalid_choice(self):
        print("Invalid choice, please insert input as instructed")

    def operate_user_choice(self, user_choice):
        normalized_choice = user_choice.strip().lower()
        option = self.main_menu_choices_operator[normalized_choice]
        if option is not None:
            option()

    def run_main_menu(self):
        while self.user_continue:
            print(ConsoleUI.opening_message)
            for index, option in enumerate(ConsoleUI.main_menu_options, 1):
                print(f"{index}. {option}")
            print(ConsoleUI.quit_message)
            user_choice = input()
            self.operate_user_choice(user_choice.strip())

    def set_main_menu_operator(self):
        valid_options = {'1': self.print_access_points,
                         '2': self.operate_connect_to_access_point,
                         '3': self.operate_open_google_in_browser,
                         'q': self.operate_quit}
        self.main_menu_choices_operator = defaultdict(self.operate_invalid_choice, valid_options)

    def check_network_exist(self, result):
        return self.access_points[result] is not None

    def set_access_points(self):
        access_points = AccessPointsParser(self.network_manager.get_available_devices()).access_points
        access_point_dict = {x.ssid: x for x in access_points}
        return defaultdict(self.operate_invalid_choice, access_point_dict)

    def connect_to_existing_access_point(self, result):
        access_point = self.access_points[result]
        if access_point:
            if access_point.security:
                password = input("please insert password")
                result = self.network_manager.connect_access_point(access_point, password)
            else:
                result = self.network_manager.connect_access_point(access_point)
            self.handle_result(result)

    def handle_result(self, result):
        if result.find("successfully") != -1:
            print("successfully connected")
        else:
            print("something went wrong, please try again")
