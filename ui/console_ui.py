from collections import defaultdict

from controllers.access_points_parser import AccessPointsParser
from controllers.os_utils import get_available_devices


class ConsoleUI:
    def __init__(self):
        self.main_menu_choices_operator = None
        self.access_points = AccessPointsParser(get_available_devices()).access_points
        self.user_continue = True
        self.set_main_menu_operator()

    opening_message = "Hi there, please select_one of the options"
    quit_message = "If you want to quit, please insert q"
    main_menu_options = ["Show available access points", "Connect to access point", "Open google in browser "]
    the_best_network = "The Best Network: "

    def print_access_points(self):
        print('*' * 8 + ConsoleUI.the_best_network + self.access_points[0] + '*' * 8)
        for access_point in self.access_points[1:]:
            print(access_point)
            print()
        print()

    def operate_connect_to_access_point(self):
        self.print_access_points()

    def operate_open_google_in_browser(self):
        pass

    def operate_quit(self):
        print("shutting down..")
        self.user_continue = False

    def operate_invalid_choice(self):
        print("Invalid choice, please choose a number of one of the options")

    def operate_user_choice(self, user_choice):
        normalized_choice = user_choice.strip().lower()
        self.main_menu_choices_operator[normalized_choice]()

    def run_main_menu(self):
        while self.user_continue:
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
        self.main_menu_choices_operator = defaultdict(self.operate_invalid_choice(), valid_options)
