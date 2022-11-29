from tabulate import tabulate
from colored import fg, bg, attr
import inflect
import csv
import os
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
    header = 'Test Header'
    header_without_color = init_header(header)
    result  = fg('#ffffff') + bg('#000000') + "    " + 'Test Header' + "    " + attr("reset")
    assert header_without_color == result

def test_create_header_with_set_colors():
    #Test without Foreground color
    header = 'Test Header with colors'
    header_with_bg = init_header(header,back_color='#00ff00')
    result  = fg('#ffffff') + bg('#00ff00') + "    " + 'Test Header with colors' + "    " + attr("reset")
    assert header_with_bg == result
    #Test without Background color
    header = 'Test Header with colors'
    header_with_bg = init_header(header,fore_color='#ff0000')
    result  = fg('#ff0000') + bg('#000000') + "    " + 'Test Header with colors' + "    " + attr("reset")
    assert header_with_bg == result
    #Test with Foreground color and Background color
    header = 'Test Header with colors'
    header_with_bg = init_header(header,fore_color='#ff0000',back_color='#00ff00')
    result  = fg('#ff0000') + bg('#00ff00') + "    " + 'Test Header with colors' + "    " + attr("reset")
    assert header_with_bg == result

def test_init_table():
    assert init_table("test_table") == 'test_table'
    ...

def main():
    test_card()
    test_create_header_without_set_color()
    test_create_header_with_set_colors()
    ...


if __name__ == "__main__":
    main()
