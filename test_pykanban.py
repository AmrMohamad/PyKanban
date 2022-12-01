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


def test_card():
    title = "Test Card"
    sub_titles = ["Test Sub-Title 1", "Test Sub-Title 2", "Test Sub-Title 3"]
    lines_under_sub_titles = (
        "Lorem ipsum dolor sit amet,",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
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
        + "|                   Test Card                    #\n"
        + "|                                                 #\n"
        + "| Test Sub-Title 1 :                              #\n"
        + "|                 Lorem ipsum dolor sit amet,     #\n"
        + "|                                                 #\n"
        + "|                                                 #\n"
        + "| Test Sub-Title 2 :                              #\n"
        + "|                 Lorem ipsum dolor sit amet, c   #\n"
        + "| onsectetur adipiscing elit                      #\n"
        + "|                                                 #\n"
        + "|                                                 #\n"
        + "| Test Sub-Title 3 :                              #\n"
        + "|                 Lorem ipsum dolor sit amet, c   #\n"
        + "| onsectetur adipiscing elit, sed do eiusmod te   #\n"
        + "| mpor incididunt ut labore et dolore magna ali   #\n"
        + "| qua.                                            #\n"
        + "|                                                 #\n "
        + "------------------------------------------------"
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
    assert init_table("test_table") == "test_table"
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
    table = {
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
            "",
            "",
        ],
        "\x1b[38;5;9m\x1b[48;5;12m    column2    \x1b[0m": [
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
    destination = "./data/_test_data"
    os.mkdir(destination)
    with open(f"{destination}/latest.csv", "w") as test_table:
        writer = csv.DictWriter(test_table, fieldnames=list(table.keys()))
        writer.writeheader()
        longest_header_in_cards = 0
        for h in list(table.keys()):
            if longest_header_in_cards < len(table[h]):
                longest_header_in_cards = len(table[h])
            else:
                continue
        for row in range(longest_header_in_cards):
            temp_ = {}
            for h_pointer in table:
                if row in range(len(table[h_pointer])):
                    temp_[h_pointer] = table[h_pointer][row]
                else:
                    continue
            writer.writerow(temp_)
    assert open_table(table_name="_test_data") == table
    shutil.rmtree(destination)
    # Test open table without any parameters
    with pytest.raises(TypeError):
        open_table()
    # Test open table to open table history
    os.mkdir(destination)
    table = {
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
    with open(f"{destination}/_ 28-11-2022 03.44.42 PM.csv", "w") as test_table:
        writer = csv.DictWriter(test_table, fieldnames=list(table.keys()))
        writer.writeheader()
        longest_header_in_cards = 0
        for h in list(table.keys()):
            if longest_header_in_cards < len(table[h]):
                longest_header_in_cards = len(table[h])
            else:
                continue
        for row in range(longest_header_in_cards):
            temp_ = {}
            for h_pointer in table:
                if row in range(len(table[h_pointer])):
                    temp_[h_pointer] = table[h_pointer][row]
                else:
                    continue
            writer.writerow(temp_)
    assert (
        open_table(
            table_name="_test_data", table_version="_ 28-11-2022 03.44.42 PM.csv"
        )
        == table
    )
    shutil.rmtree(destination)


def test_add_card():
    destination = "./data/_test_data"
    os.mkdir(destination)
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
            "",
            "",
        ],
        "\x1b[38;5;9m\x1b[48;5;12m    column2    \x1b[0m": [
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
    with open(f"{destination}/latest.csv", "w") as test_table:
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
    # Test adding a card
    assert (
        add_card(
            "_test_data",
            "Card_7",
            "column1",
            ["Title", "Description", "Comment"],
            [
                "qwertyqwertyqwertyqwertyqwertyqwerty",
                "qwertyqwertyqwertyqwertyqwertyqwerty",
                "qwertyqwertyqwertyqwertyqwertyqwertyqwertyqwertyqwerty",
            ],
        )
        == "Added"
    )
    table = {
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
            + "|                     Card_7                      #\n"
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
    # Checking of the Card is added
    assert open_table(table_name="_test_data") == table
    shutil.rmtree(destination)
    ...


def main():
    test_card()
    test_create_header_without_set_color()
    test_create_header_with_set_colors()
    test_init_table()
    test_view_tables()
    test_open_table()
    test_add_card()


if __name__ == "__main__":
    main()
