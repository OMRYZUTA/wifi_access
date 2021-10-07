# wifi_access
console app for accessing wifi

 This project is a command line application that manipulates the network.


Usage:
From inside of wifi_access directory hit python3 ./main.py
Insert input as requested

Technologies:
Python 3.9,
Pipenv,
ubuntu,
Git,
Pycharm.

Project structure:
Folders:
Controllers:
Access_points_parser - parse from linux output to access_point object
Network manager - gets access points, connect to them, open chrome
Models: 
Access_point - holds the ssid, the signal and security info as strings
Tests: 
Check functionality for parser - incomplete
Ui :
ConsoleUI only class that prints to the screen, runs the menus, and invoke the controllers





Decisions:
The app should handle user typos and re prompt if necessary
The app can connect to access points with or without passwords
The app is running on a machine that doesn’t need sudo permissions for nmbli
The app doesn’t show detailed network errors - only success or failure
The packages required on ubuntu to run this app are detailed in ubuntu_packages.txt
