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


def main():
    test_card()
    ...


if __name__ == "__main__":
    main()
