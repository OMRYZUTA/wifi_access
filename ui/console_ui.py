opening_message = "Hi there, please select_one of the options"
quit_message = "If you want to quit, please insert q"
main_menu_options = ["Show available access points", "Connect to access point", "Open google in browser "]

choices_operator = {}


def print_access_points(access_points):
    print('*' * 8 + access_points[0] + '*' * 8)
    for access_point in access_points[1:]:
        print(access_point)


def operate_user_choice(user_choice):
    pass


def run_mainMenu():
    user_continue = True
    while user_continue:
        for index, option in enumerate(main_menu_options):
            print(f"{index}. {option}")
        print(quit_message)
        user_choice = input()
        user_continue = operate_user_choice(user_choice.strip())
