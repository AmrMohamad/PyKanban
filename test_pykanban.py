from tabulate import tabulate
from colored import fg, bg, attr
import inflect
import csv
import os
import shutil
import sys
import re
import time
from datetime import datetime
import pytest
from pykanban import *


DESTINATION = "./data/_test_data"
TABLE = {
    "\x1b[38;5;15m\x1b[48;5;0m    column1    \x1b[0m": [
        " #################################################\n"
        + "|                     Card_1                      #\n"
        + "|                                                 #\n"
        + "| Description :                                   #\n"
        + "|       This task involves creating wireframes    #\n"
        + "| and mockups for the different pages and         #\n"
        + "| screens of the software application. This may   #\n"
        + "| include designing the layout, buttons, input    #\n"
        + "| fields, and other visual elements of the user   #\n"
        + "| interface.                                      #\n"
        + "| Task Type :                                     #\n"
        + "|     Feature Implementation                      #\n"
        + "| Status :                                        #\n"
        + "|    In Progress                                  #\n"
        + "| Estimated Time :                                #\n"
        + "|        8 hours                                  #\n"
        + "| Notes :                                         #\n"
        + "|   This task should be completed before the      #\n"
        + "| code for the user interface is written, as it   #\n"
        + "| will provide a clear visual guide for the       #\n"
        + "| developers.                                     #\n"
        + " ------------------------------------------------",
        "",
        "",
    ],
    "\x1b[38;5;9m\x1b[48;5;12m    column2    \x1b[0m": [
        " #################################################\n"
        + "|                     Card_2                      #\n"
        + "|                                                 #\n"
        + "| Description :                                   #\n"
        + "|       This task involves writing the code       #\n"
        + "| that will handle user authentication in the     #\n"
        + "| software application.                           #\n"
        + "| Task Type :                                     #\n"
        + "|     Bug Fix                                     #\n"
        + "| Status :                                        #\n"
        + "|    Completed                                    #\n"
        + "| Estimated Time :                                #\n"
        + "|        16 hours                                 #\n"
        + "| Notes :                                         #\n"
        + "|   This task should be completed before the      #\n"
        + "| login functionality is implemented, as it       #\n"
        + "| will provide the necessary code for handling    #\n"
        + "| user authentication.                            #\n"
        + " ------------------------------------------------",
        " #################################################\n"
        + "|                     Card_3                      #\n"
        + "|                                                 #\n"
        + "| Description :                                   #\n"
        + "|       This task involves writing tests that     #\n"
        + "| will verify that the authentication module is   #\n"
        + "| working correctly. This may include testing     #\n"
        + "| different scenarios.                            #\n"
        + "| Task Type :                                     #\n"
        + "|     Refactoring                                 #\n"
        + "| Status :                                        #\n"
        + "|    In Progress                                  #\n"
        + "| Estimated Time :                                #\n"
        + "|        4 hours                                  #\n"
        + "| Notes :                                         #\n"
        + "|   This task should be completed after the       #\n"
        + "| code for the authentication module has been     #\n"
        + "| written, and should be run regularly to         #\n"
        + "| ensure the module is functioning properly.      #\n"
        + " ------------------------------------------------",
        "",
    ],
    "\x1b[38;5;10m\x1b[48;5;13m    column3    \x1b[0m": [
        " #################################################\n"
        + "|                     Card_4                      #\n"
        + "|                                                 #\n"
        + "| Description :                                   #\n"
        + "|       This task involves integrating the        #\n"
        + "| authentication module into the software         #\n"
        + "| application, and implementing the               #\n"
        + "| functionality for logging in and out.           #\n"
        + "| Task Type :                                     #\n"
        + "|     Testing                                     #\n"
        + "| Status :                                        #\n"
        + "|    In Progress                                  #\n"
        + "| Estimated Time :                                #\n"
        + "|        12 hours                                 #\n"
        + "| Notes :                                         #\n"
        + "|   This task should be completed after the       #\n"
        + "| code for the authentication module and the      #\n"
        + "| user interface have been written, and should    #\n"
        + "| be tested thoroughly to ensure the login        #\n"
        + "| process is working correctly.                   #\n"
        + " ------------------------------------------------",
        " #################################################\n"
        + "|                     Card_5                      #\n"
        + "|                                                 #\n"
        + "| Description :                                   #\n"
        + "|       This task involves writing the code       #\n"
        + "| that will handle the connection to the          #\n"
        + "| database used by the software application.      #\n"
        + "| This may include implementing functions for     #\n"
        + "| executing SQL queries                           #\n"
        + "| Task Type :                                     #\n"
        + "|     Documentation                               #\n"
        + "| Status :                                        #\n"
        + "|    Completed                                    #\n"
        + "| Estimated Time :                                #\n"
        + "|        6 hours                                  #\n"
        + "| Notes :                                         #\n"
        + "|   This task should be completed before the      #\n"
        + "| code for accessing the database is written,     #\n"
        + "| as it will provide the necessary functions      #\n"
        + "| for connecting to the database.                 #\n"
        + " ------------------------------------------------",
        " #################################################\n"
        + "|                     Card_6                      #\n"
        + "|                                                 #\n"
        + "| Description :                                   #\n"
        + "|       This task involves writing the code for   #\n"
        + "| the user profile page, which will display       #\n"
        + "| information about the logged-in user, such as   #\n"
        + "| their username, email address, and other        #\n"
        + "| profile details.                                #\n"
        + "| Task Type :                                     #\n"
        + "|     Deployment                                  #\n"
        + "| Status :                                        #\n"
        + "|    Blocked                                      #\n"
        + "| Estimated Time :                                #\n"
        + "|        2 hours                                  #\n"
        + "| Notes :                                         #\n"
        + "|   This task should be completed after the       #\n"
        + "| code for the authentication module and the      #\n"
        + "| database connection have been written, as it    #\n"
        + "| will require accessing the user's data from     #\n"
        + "| the database.                                   #\n"
        + " ------------------------------------------------",
    ],
}


def generate_table():
    os.mkdir(DESTINATION)
    with open(f"{DESTINATION}/latest.csv", "w") as test_table:
        writer = csv.DictWriter(test_table, fieldnames=list(TABLE.keys()))
        writer.writeheader()
        longest_header_in_cards = 0
        for h in list(TABLE.keys()):
            if longest_header_in_cards < len(TABLE[h]):
                longest_header_in_cards = len(TABLE[h])
            else:
                continue
        for row in range(longest_header_in_cards):
            temp_ = {}
            for h_pointer in TABLE:
                if row in range(len(TABLE[h_pointer])):
                    temp_[h_pointer] = TABLE[h_pointer][row]
                else:
                    continue
            writer.writerow(temp_)
    ...


def test_card():
    title = "Card_1"
    sub_titles = ["Description", "Task Type", "Status", "Estimated Time", "Notes"]
    lines_under_sub_titles = (
        "This task involves creating wireframes and mockups for the different pages and screens of the software application. This may include designing the layout, buttons, input fields, and other visual elements of the user interface.",
        "Feature Implementation",
        "In Progress",
        "8 hours",
        "This task should be completed before the code for the user interface is written, as it will provide a clear visual guide for the developers.",
    )
    card = (
        Card.add_title(title)
        .add_sub_titles(sub_titles)
        .add_lines(*lines_under_sub_titles)
        .print_here()
    )
    assert (
        card
        == " #################################################\n"
        + "|                     Card_1                      #\n"
        + "|                                                 #\n"
        + "| Description :                                   #\n"
        + "|       This task involves creating wireframes    #\n"
        + "| and mockups for the different pages and         #\n"
        + "| screens of the software application. This may   #\n"
        + "| include designing the layout, buttons, input    #\n"
        + "| fields, and other visual elements of the user   #\n"
        + "| interface.                                      #\n"
        + "| Task Type :                                     #\n"
        + "|     Feature Implementation                      #\n"
        + "| Status :                                        #\n"
        + "|    In Progress                                  #\n"
        + "| Estimated Time :                                #\n"
        + "|        8 hours                                  #\n"
        + "| Notes :                                         #\n"
        + "|   This task should be completed before the      #\n"
        + "| code for the user interface is written, as it   #\n"
        + "| will provide a clear visual guide for the       #\n"
        + "| developers.                                     #\n"
        + " ------------------------------------------------"
    )
    ...


def test_create_header_without_set_color():
    # Test with set header name
    header = "Test Header"
    header_without_color = init_header(header)
    result = (
        fg("#ffffff") + bg("#000000") + "    " + "Test Header" + "    " + attr("reset")
    )
    assert header_without_color == result
    # Test without set header name
    with pytest.raises(ValueError):
        init_header("")
    with pytest.raises(TypeError):
        init_header()


def test_create_header_with_set_colors():
    # Test without Foreground color
    header = "Test Header with colors"
    header_with_bg = init_header(header, back_color="#00ff00")
    result = (
        fg("#ffffff")
        + bg("#00ff00")
        + "    "
        + "Test Header with colors"
        + "    "
        + attr("reset")
    )
    assert header_with_bg == result
    # Test without Background color
    header = "Test Header with colors"
    header_with_bg = init_header(header, fore_color="#ff0000")
    result = (
        fg("#ff0000")
        + bg("#000000")
        + "    "
        + "Test Header with colors"
        + "    "
        + attr("reset")
    )
    assert header_with_bg == result
    # Test with Foreground color and Background color
    header = "Test Header with colors"
    header_with_bg = init_header(header, fore_color="#ff0000", back_color="#00ff00")
    result = (
        fg("#ff0000")
        + bg("#00ff00")
        + "    "
        + "Test Header with colors"
        + "    "
        + attr("reset")
    )
    assert header_with_bg == result
    # Test colors with invaild Hex value
    with pytest.raises(TypeError):
        init_header(header, fore_color="000000", back_color="#9gffff")


def test_init_table():
    assert init_table("_test_data") == "_test_data"
    shutil.rmtree(DESTINATION)
    with pytest.raises(TypeError):
        init_table()
    ...


def test_view_tables():
    destination = "./test_data"
    os.mkdir(destination)
    # shutil.rmtree(f'{destination}/.DS_Store')
    for f in os.listdir("./data"):
        shutil.move(f"./data/{f}", destination)
    assert view_tables() == "No Tables Exist"
    for f in os.listdir(destination):
        shutil.move(f"{destination}/{f}", "./data")
    name_tables = []
    for nt in os.listdir("./data"):
        if nt == ".DS_Store":
            continue
        name_tables.append(nt)
    assert view_tables() == name_tables
    os.rmdir(destination)
    ...


def test_open_table():
    # Test open table with only table name to open latest.csv
    generate_table()
    assert open_table(table_name="_test_data") == TABLE
    shutil.rmtree(DESTINATION)
    # Test open table without any parameters
    with pytest.raises(TypeError):
        open_table()
    # Test open table to open table history
    os.mkdir(DESTINATION)
    table_e = {
        "\x1b[38;5;15m\x1b[48;5;0m    column1    \x1b[0m": [
            " #################################################\n"
            + "|                     Card_1                      #\n"
            + "|                                                 #\n"
            + "| descriptoin :                                   #\n"
            + "|            qwertyqwertyqwerty                   #\n"
            + "|                                                 #\n"
            + "|                                                 #\n"
            + "| Commnet :                                       #\n"
            + "|        qwertyqwertyqwertyqwertyqwertyqwerty     #\n"
            + "|                                                 #\n"
            + "|                                                 #\n"
            + "| Notes :                                         #\n"
            + "|      qwertyqwertyqwertyqwertyqwertyqwerty       #\n"
            + "|                                                 #\n"
            + "|                                                 #\n"
            + " ------------------------------------------------",
            " #################################################\n"
            + "|                     Card_2                      #\n"
            + "|                                                 #\n"
            + "| Title :                                         #\n"
            + "|      qwertyqwertyqwertyqwertyqwertyqwerty       #\n"
            + "|                                                 #\n"
            + "|                                                 #\n"
            + "| Description :                                   #\n"
            + "|            qwertyqwertyqwertyqwertyqwertyqwer   #\n"
            + "| ty                                              #\n"
            + "|                                                 #\n"
            + "| Comment :                                       #\n"
            + "|        qwertyqwertyqwertyqwertyqwertyqwertyqw   #\n"
            + "| ertyqwertyqwerty                                #\n"
            + "|                                                 #\n"
            + " ------------------------------------------------",
            "",
        ],
        "\x1b[38;5;9m\x1b[48;5;12m    column2    \x1b[0m": [
            " #################################################\n"
            + "|                     Card_3                      #\n"
            + "|                                                 #\n"
            + "| Description :                                   #\n"
            + "|            qwertyqwertyqwertyqwertyqwertyqwer   #\n"
            + "| ty                                              #\n"
            + "|                                                 #\n"
            + "| Comment :                                       #\n"
            + "|        qwertyqwertyqwertyqwertyqwertyqwerty     #\n"
            + "|                                                 #\n"
            + "|                                                 #\n"
            + "| Notes :                                         #\n"
            + "|      qwertyqwertyqwertyqwertyqwertyqwerty       #\n"
            + "|                                                 #\n"
            + "|                                                 #\n"
            + " ------------------------------------------------",
            "",
            "",
        ],
        "\x1b[38;5;10m\x1b[48;5;13m    column3    \x1b[0m": [
            " #################################################\n"
            + "|                     Card_4                      #\n"
            + "|                                                 #\n"
            + "| des :                                           #\n"
            + "|    qwertyqwertyqwerty                           #\n"
            + "|                                                 #\n"
            + "| comment :                                       #\n"
            + "|        qwertyqwertyqwertyqwertyqwertyqwerty     #\n"
            + "|                                                 #\n"
            + "|                                                 #\n"
            + "| notes :                                         #\n"
            + "|      qwertyqwertyqwerty                         #\n"
            + "|                                                 #\n"
            + "|                                                 #\n"
            + " ------------------------------------------------",
            " #################################################\n"
            + "|                     Card_5                      #\n"
            + "|                                                 #\n"
            + "| des :                                           #\n"
            + "|    qwertyqwertyqwerty                           #\n"
            + "|                                                 #\n"
            + "| comment :                                       #\n"
            + "|        qwertyqwertyqwertyqwertyqwertyqwerty     #\n"
            + "|                                                 #\n"
            + "|                                                 #\n"
            + "| notes :                                         #\n"
            + "|      qwertyqwertyqwerty                         #\n"
            + "|                                                 #\n"
            + "|                                                 #\n"
            + " ------------------------------------------------",
            " #################################################\n"
            + "|                     Card_6                      #\n"
            + "|                                                 #\n"
            + "| tit :                                           #\n"
            + "|    qwertyqwertyqwerty                           #\n"
            + "|                                                 #\n"
            + "| des :                                           #\n"
            + "|    qwertyqwertyqwerty                           #\n"
            + "|                                                 #\n"
            + "| com :                                           #\n"
            + "|    qwertyqwertyqwerty                           #\n"
            + "|                                                 #\n"
            + " ------------------------------------------------",
        ],
    }
    with open(f"{DESTINATION}/_ 28-11-2022 03.44.42 PM.csv", "w") as test_table:
        writer = csv.DictWriter(test_table, fieldnames=list(table_e.keys()))
        writer.writeheader()
        longest_header_in_cards = 0
        for h in list(table_e.keys()):
            if longest_header_in_cards < len(table_e[h]):
                longest_header_in_cards = len(table_e[h])
            else:
                continue
        for row in range(longest_header_in_cards):
            temp_ = {}
            for h_pointer in table_e:
                if row in range(len(table_e[h_pointer])):
                    temp_[h_pointer] = table_e[h_pointer][row]
                else:
                    continue
            writer.writerow(temp_)
    assert (
        open_table(
            table_name="_test_data", table_version="_ 28-11-2022 03.44.42 PM.csv"
        )
        == table_e
    )
    shutil.rmtree(DESTINATION)
    # Test open table with wrong table name or is not exist
    with pytest.raises(FileNotFoundError):
        open_table(table_name="_test_data_")


def test_add_card():
    generate_table()
    # Test adding a card
    assert (
        add_card(
            "_test_data",
            "Card_7",
            "column1",
            ["Description", "Task Type", "Status", "Estimated Time", "Notes"],
            [
                "Implement the user profile page, which will display information about the logged-in user.",
                "Feature Implementation",
                "In Progress",
                "4 hours",
                "This task may involve using a template engine such as Jinja or Mustache to create the user profile page.",
            ],
        )
        == "Added"
    )
    table_e = {
        "\x1b[38;5;15m\x1b[48;5;0m    column1    \x1b[0m": [
            " #################################################\n"
            + "|                     Card_1                      #\n"
            + "|                                                 #\n"
            + "| Description :                                   #\n"
            + "|       This task involves creating wireframes    #\n"
            + "| and mockups for the different pages and         #\n"
            + "| screens of the software application. This may   #\n"
            + "| include designing the layout, buttons, input    #\n"
            + "| fields, and other visual elements of the user   #\n"
            + "| interface.                                      #\n"
            + "| Task Type :                                     #\n"
            + "|     Feature Implementation                      #\n"
            + "| Status :                                        #\n"
            + "|    In Progress                                  #\n"
            + "| Estimated Time :                                #\n"
            + "|        8 hours                                  #\n"
            + "| Notes :                                         #\n"
            + "|   This task should be completed before the      #\n"
            + "| code for the user interface is written, as it   #\n"
            + "| will provide a clear visual guide for the       #\n"
            + "| developers.                                     #\n"
            + " ------------------------------------------------",
            " #################################################\n"
            + "|                     Card_7                      #\n"
            + "|                                                 #\n"
            + "| Description :                                   #\n"
            + "|       Implement the user profile page, which    #\n"
            + "| will display information about the logged-in    #\n"
            + "| user.                                           #\n"
            + "| Task Type :                                     #\n"
            + "|     Feature Implementation                      #\n"
            + "| Status :                                        #\n"
            + "|    In Progress                                  #\n"
            + "| Estimated Time :                                #\n"
            + "|        4 hours                                  #\n"
            + "| Notes :                                         #\n"
            + "|   This task may involve using a template        #\n"
            + "| engine such as Jinja or Mustache to create      #\n"
            + "| the user profile page.                          #\n"
            + " ------------------------------------------------",
            "",
        ],
        "\x1b[38;5;9m\x1b[48;5;12m    column2    \x1b[0m": [
            " #################################################\n"
            + "|                     Card_2                      #\n"
            + "|                                                 #\n"
            + "| Description :                                   #\n"
            + "|       This task involves writing the code       #\n"
            + "| that will handle user authentication in the     #\n"
            + "| software application.                           #\n"
            + "| Task Type :                                     #\n"
            + "|     Bug Fix                                     #\n"
            + "| Status :                                        #\n"
            + "|    Completed                                    #\n"
            + "| Estimated Time :                                #\n"
            + "|        16 hours                                 #\n"
            + "| Notes :                                         #\n"
            + "|   This task should be completed before the      #\n"
            + "| login functionality is implemented, as it       #\n"
            + "| will provide the necessary code for handling    #\n"
            + "| user authentication.                            #\n"
            + " ------------------------------------------------",
            " #################################################\n"
            + "|                     Card_3                      #\n"
            + "|                                                 #\n"
            + "| Description :                                   #\n"
            + "|       This task involves writing tests that     #\n"
            + "| will verify that the authentication module is   #\n"
            + "| working correctly. This may include testing     #\n"
            + "| different scenarios.                            #\n"
            + "| Task Type :                                     #\n"
            + "|     Refactoring                                 #\n"
            + "| Status :                                        #\n"
            + "|    In Progress                                  #\n"
            + "| Estimated Time :                                #\n"
            + "|        4 hours                                  #\n"
            + "| Notes :                                         #\n"
            + "|   This task should be completed after the       #\n"
            + "| code for the authentication module has been     #\n"
            + "| written, and should be run regularly to         #\n"
            + "| ensure the module is functioning properly.      #\n"
            + " ------------------------------------------------",
            "",
        ],
        "\x1b[38;5;10m\x1b[48;5;13m    column3    \x1b[0m": [
            " #################################################\n"
            + "|                     Card_4                      #\n"
            + "|                                                 #\n"
            + "| Description :                                   #\n"
            + "|       This task involves integrating the        #\n"
            + "| authentication module into the software         #\n"
            + "| application, and implementing the               #\n"
            + "| functionality for logging in and out.           #\n"
            + "| Task Type :                                     #\n"
            + "|     Testing                                     #\n"
            + "| Status :                                        #\n"
            + "|    In Progress                                  #\n"
            + "| Estimated Time :                                #\n"
            + "|        12 hours                                 #\n"
            + "| Notes :                                         #\n"
            + "|   This task should be completed after the       #\n"
            + "| code for the authentication module and the      #\n"
            + "| user interface have been written, and should    #\n"
            + "| be tested thoroughly to ensure the login        #\n"
            + "| process is working correctly.                   #\n"
            + " ------------------------------------------------",
            " #################################################\n"
            + "|                     Card_5                      #\n"
            + "|                                                 #\n"
            + "| Description :                                   #\n"
            + "|       This task involves writing the code       #\n"
            + "| that will handle the connection to the          #\n"
            + "| database used by the software application.      #\n"
            + "| This may include implementing functions for     #\n"
            + "| executing SQL queries                           #\n"
            + "| Task Type :                                     #\n"
            + "|     Documentation                               #\n"
            + "| Status :                                        #\n"
            + "|    Completed                                    #\n"
            + "| Estimated Time :                                #\n"
            + "|        6 hours                                  #\n"
            + "| Notes :                                         #\n"
            + "|   This task should be completed before the      #\n"
            + "| code for accessing the database is written,     #\n"
            + "| as it will provide the necessary functions      #\n"
            + "| for connecting to the database.                 #\n"
            + " ------------------------------------------------",
            " #################################################\n"
            + "|                     Card_6                      #\n"
            + "|                                                 #\n"
            + "| Description :                                   #\n"
            + "|       This task involves writing the code for   #\n"
            + "| the user profile page, which will display       #\n"
            + "| information about the logged-in user, such as   #\n"
            + "| their username, email address, and other        #\n"
            + "| profile details.                                #\n"
            + "| Task Type :                                     #\n"
            + "|     Deployment                                  #\n"
            + "| Status :                                        #\n"
            + "|    Blocked                                      #\n"
            + "| Estimated Time :                                #\n"
            + "|        2 hours                                  #\n"
            + "| Notes :                                         #\n"
            + "|   This task should be completed after the       #\n"
            + "| code for the authentication module and the      #\n"
            + "| database connection have been written, as it    #\n"
            + "| will require accessing the user's data from     #\n"
            + "| the database.                                   #\n"
            + " ------------------------------------------------",
        ],
    }
    # Checking of the Card is added
    assert open_table(table_name="_test_data") == table_e
    # Test if the column name not exist
    with pytest.raises(ValueError):
        add_card(
            "_test_data",
            "Card_7",
            "column4",
            ["Description", "Task Type", "Status", "Estimated Time", "Notes"],
            [
                "Implement the user profile page, which will display information about the logged-in user.",
                "Feature Implementation",
                "In Progress",
                "4 hours",
                "This task may involve using a template engine such as Jinja or Mustache to create the user profile page.",
            ],
        )
    # Test if the table name not exist
    with pytest.raises(TypeError):
        add_card(
            "_test_data_",
            "Card_7",
            "column1",
            ["Description", "Task Type", "Status", "Estimated Time", "Notes"],
            [
                "Implement the user profile page, which will display information about the logged-in user.",
                "Feature Implementation",
                "In Progress",
                "4 hours",
                "This task may involve using a template engine such as Jinja or Mustache to create the user profile page.",
            ],
        )
    shutil.rmtree(DESTINATION)
    ...


def test_move_card():
    generate_table()
    # Test moving card
    assert (
        move_card(
            table_name_to_edit="_test_data", card_name="Card_2", move_to="column1"
        )
        == "Moved"
    )
    table_e = {
        "\x1b[38;5;15m\x1b[48;5;0m    column1    \x1b[0m": [
            " #################################################\n"
            + "|                     Card_1                      #\n"
            + "|                                                 #\n"
            + "| Description :                                   #\n"
            + "|       This task involves creating wireframes    #\n"
            + "| and mockups for the different pages and         #\n"
            + "| screens of the software application. This may   #\n"
            + "| include designing the layout, buttons, input    #\n"
            + "| fields, and other visual elements of the user   #\n"
            + "| interface.                                      #\n"
            + "| Task Type :                                     #\n"
            + "|     Feature Implementation                      #\n"
            + "| Status :                                        #\n"
            + "|    In Progress                                  #\n"
            + "| Estimated Time :                                #\n"
            + "|        8 hours                                  #\n"
            + "| Notes :                                         #\n"
            + "|   This task should be completed before the      #\n"
            + "| code for the user interface is written, as it   #\n"
            + "| will provide a clear visual guide for the       #\n"
            + "| developers.                                     #\n"
            + " ------------------------------------------------",
            " #################################################\n"
            + "|                     Card_2                      #\n"
            + "|                                                 #\n"
            + "| Description :                                   #\n"
            + "|       This task involves writing the code       #\n"
            + "| that will handle user authentication in the     #\n"
            + "| software application.                           #\n"
            + "| Task Type :                                     #\n"
            + "|     Bug Fix                                     #\n"
            + "| Status :                                        #\n"
            + "|    Completed                                    #\n"
            + "| Estimated Time :                                #\n"
            + "|        16 hours                                 #\n"
            + "| Notes :                                         #\n"
            + "|   This task should be completed before the      #\n"
            + "| login functionality is implemented, as it       #\n"
            + "| will provide the necessary code for handling    #\n"
            + "| user authentication.                            #\n"
            + " ------------------------------------------------",
            "",
        ],
        "\x1b[38;5;9m\x1b[48;5;12m    column2    \x1b[0m": [
            " #################################################\n"
            + "|                     Card_3                      #\n"
            + "|                                                 #\n"
            + "| Description :                                   #\n"
            + "|       This task involves writing tests that     #\n"
            + "| will verify that the authentication module is   #\n"
            + "| working correctly. This may include testing     #\n"
            + "| different scenarios.                            #\n"
            + "| Task Type :                                     #\n"
            + "|     Refactoring                                 #\n"
            + "| Status :                                        #\n"
            + "|    In Progress                                  #\n"
            + "| Estimated Time :                                #\n"
            + "|        4 hours                                  #\n"
            + "| Notes :                                         #\n"
            + "|   This task should be completed after the       #\n"
            + "| code for the authentication module has been     #\n"
            + "| written, and should be run regularly to         #\n"
            + "| ensure the module is functioning properly.      #\n"
            + " ------------------------------------------------",
            "",
            "",
        ],
        "\x1b[38;5;10m\x1b[48;5;13m    column3    \x1b[0m": [
            " #################################################\n"
            + "|                     Card_4                      #\n"
            + "|                                                 #\n"
            + "| Description :                                   #\n"
            + "|       This task involves integrating the        #\n"
            + "| authentication module into the software         #\n"
            + "| application, and implementing the               #\n"
            + "| functionality for logging in and out.           #\n"
            + "| Task Type :                                     #\n"
            + "|     Testing                                     #\n"
            + "| Status :                                        #\n"
            + "|    In Progress                                  #\n"
            + "| Estimated Time :                                #\n"
            + "|        12 hours                                 #\n"
            + "| Notes :                                         #\n"
            + "|   This task should be completed after the       #\n"
            + "| code for the authentication module and the      #\n"
            + "| user interface have been written, and should    #\n"
            + "| be tested thoroughly to ensure the login        #\n"
            + "| process is working correctly.                   #\n"
            + " ------------------------------------------------",
            " #################################################\n"
            + "|                     Card_5                      #\n"
            + "|                                                 #\n"
            + "| Description :                                   #\n"
            + "|       This task involves writing the code       #\n"
            + "| that will handle the connection to the          #\n"
            + "| database used by the software application.      #\n"
            + "| This may include implementing functions for     #\n"
            + "| executing SQL queries                           #\n"
            + "| Task Type :                                     #\n"
            + "|     Documentation                               #\n"
            + "| Status :                                        #\n"
            + "|    Completed                                    #\n"
            + "| Estimated Time :                                #\n"
            + "|        6 hours                                  #\n"
            + "| Notes :                                         #\n"
            + "|   This task should be completed before the      #\n"
            + "| code for accessing the database is written,     #\n"
            + "| as it will provide the necessary functions      #\n"
            + "| for connecting to the database.                 #\n"
            + " ------------------------------------------------",
            " #################################################\n"
            + "|                     Card_6                      #\n"
            + "|                                                 #\n"
            + "| Description :                                   #\n"
            + "|       This task involves writing the code for   #\n"
            + "| the user profile page, which will display       #\n"
            + "| information about the logged-in user, such as   #\n"
            + "| their username, email address, and other        #\n"
            + "| profile details.                                #\n"
            + "| Task Type :                                     #\n"
            + "|     Deployment                                  #\n"
            + "| Status :                                        #\n"
            + "|    Blocked                                      #\n"
            + "| Estimated Time :                                #\n"
            + "|        2 hours                                  #\n"
            + "| Notes :                                         #\n"
            + "|   This task should be completed after the       #\n"
            + "| code for the authentication module and the      #\n"
            + "| database connection have been written, as it    #\n"
            + "| will require accessing the user's data from     #\n"
            + "| the database.                                   #\n"
            + " ------------------------------------------------",
        ],
    }
    # Checking of the Card is moved
    assert open_table(table_name="_test_data") == table_e
    # Test if the table name not exist
    with pytest.raises(TypeError):
        move_card(
            table_name_to_edit="_test_data_", card_name="Card_6", move_to="column1"
        )
    # Test if the card name not exist
    with pytest.raises(ValueError):
        move_card(
            table_name_to_edit="_test_data", card_name="Card_7", move_to="column1"
        )
    # Test if the column name not exist
    with pytest.raises(ValueError):
        move_card(
            table_name_to_edit="_test_data", card_name="Card_6", move_to="column4"
        )
    shutil.rmtree(DESTINATION)


def test_delete_card():
    generate_table()
    # Test deleting a card
    assert delete_card(table_name_to_edit="_test_data", card_name="Card_2") == "Deleted"
    table_e = {
        "\x1b[38;5;15m\x1b[48;5;0m    column1    \x1b[0m": [
            " #################################################\n"
            + "|                     Card_1                      #\n"
            + "|                                                 #\n"
            + "| Description :                                   #\n"
            + "|       This task involves creating wireframes    #\n"
            + "| and mockups for the different pages and         #\n"
            + "| screens of the software application. This may   #\n"
            + "| include designing the layout, buttons, input    #\n"
            + "| fields, and other visual elements of the user   #\n"
            + "| interface.                                      #\n"
            + "| Task Type :                                     #\n"
            + "|     Feature Implementation                      #\n"
            + "| Status :                                        #\n"
            + "|    In Progress                                  #\n"
            + "| Estimated Time :                                #\n"
            + "|        8 hours                                  #\n"
            + "| Notes :                                         #\n"
            + "|   This task should be completed before the      #\n"
            + "| code for the user interface is written, as it   #\n"
            + "| will provide a clear visual guide for the       #\n"
            + "| developers.                                     #\n"
            + " ------------------------------------------------",
            "",
            "",
        ],
        "\x1b[38;5;9m\x1b[48;5;12m    column2    \x1b[0m": [
            " #################################################\n"
            + "|                     Card_3                      #\n"
            + "|                                                 #\n"
            + "| Description :                                   #\n"
            + "|       This task involves writing tests that     #\n"
            + "| will verify that the authentication module is   #\n"
            + "| working correctly. This may include testing     #\n"
            + "| different scenarios.                            #\n"
            + "| Task Type :                                     #\n"
            + "|     Refactoring                                 #\n"
            + "| Status :                                        #\n"
            + "|    In Progress                                  #\n"
            + "| Estimated Time :                                #\n"
            + "|        4 hours                                  #\n"
            + "| Notes :                                         #\n"
            + "|   This task should be completed after the       #\n"
            + "| code for the authentication module has been     #\n"
            + "| written, and should be run regularly to         #\n"
            + "| ensure the module is functioning properly.      #\n"
            + " ------------------------------------------------",
            "",
            "",
        ],
        "\x1b[38;5;10m\x1b[48;5;13m    column3    \x1b[0m": [
            " #################################################\n"
            + "|                     Card_4                      #\n"
            + "|                                                 #\n"
            + "| Description :                                   #\n"
            + "|       This task involves integrating the        #\n"
            + "| authentication module into the software         #\n"
            + "| application, and implementing the               #\n"
            + "| functionality for logging in and out.           #\n"
            + "| Task Type :                                     #\n"
            + "|     Testing                                     #\n"
            + "| Status :                                        #\n"
            + "|    In Progress                                  #\n"
            + "| Estimated Time :                                #\n"
            + "|        12 hours                                 #\n"
            + "| Notes :                                         #\n"
            + "|   This task should be completed after the       #\n"
            + "| code for the authentication module and the      #\n"
            + "| user interface have been written, and should    #\n"
            + "| be tested thoroughly to ensure the login        #\n"
            + "| process is working correctly.                   #\n"
            + " ------------------------------------------------",
            " #################################################\n"
            + "|                     Card_5                      #\n"
            + "|                                                 #\n"
            + "| Description :                                   #\n"
            + "|       This task involves writing the code       #\n"
            + "| that will handle the connection to the          #\n"
            + "| database used by the software application.      #\n"
            + "| This may include implementing functions for     #\n"
            + "| executing SQL queries                           #\n"
            + "| Task Type :                                     #\n"
            + "|     Documentation                               #\n"
            + "| Status :                                        #\n"
            + "|    Completed                                    #\n"
            + "| Estimated Time :                                #\n"
            + "|        6 hours                                  #\n"
            + "| Notes :                                         #\n"
            + "|   This task should be completed before the      #\n"
            + "| code for accessing the database is written,     #\n"
            + "| as it will provide the necessary functions      #\n"
            + "| for connecting to the database.                 #\n"
            + " ------------------------------------------------",
            " #################################################\n"
            + "|                     Card_6                      #\n"
            + "|                                                 #\n"
            + "| Description :                                   #\n"
            + "|       This task involves writing the code for   #\n"
            + "| the user profile page, which will display       #\n"
            + "| information about the logged-in user, such as   #\n"
            + "| their username, email address, and other        #\n"
            + "| profile details.                                #\n"
            + "| Task Type :                                     #\n"
            + "|     Deployment                                  #\n"
            + "| Status :                                        #\n"
            + "|    Blocked                                      #\n"
            + "| Estimated Time :                                #\n"
            + "|        2 hours                                  #\n"
            + "| Notes :                                         #\n"
            + "|   This task should be completed after the       #\n"
            + "| code for the authentication module and the      #\n"
            + "| database connection have been written, as it    #\n"
            + "| will require accessing the user's data from     #\n"
            + "| the database.                                   #\n"
            + " ------------------------------------------------",
        ],
    }
    # Checking of the Card is deleted
    assert open_table(table_name="_test_data") == table_e
    # Test if the table name not exist
    with pytest.raises(TypeError):
        delete_card(table_name_to_edit="", card_name="Card_6")
    # Test if the card name not exist
    with pytest.raises(ValueError):
        delete_card(table_name_to_edit="_test_data", card_name="Card_10")
    shutil.rmtree(DESTINATION)
    ...


def main():
    test_card()
    test_create_header_without_set_color()
    test_create_header_with_set_colors()
    test_init_table()
    test_view_tables()
    test_open_table()
    test_add_card()
    test_move_card()
    test_delete_card()


if __name__ == "__main__":
    main()
