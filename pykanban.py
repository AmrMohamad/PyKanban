from tabulate import tabulate
from colored import fg, bg, attr, stylize
import csv
import os
import sys
import time


DATA_DIR = "./data/"


class Card:
    def __init__(self, width_of_card: int = 38) -> None:
        self.width_of_card: int = width_of_card
        self._top_line: str = " " + ("#" * (width_of_card + 2)) + "#" + "\n"
        self._blank_line: str = "| " + (" " * (width_of_card + 2)) + "#" + "\n"
        self._buttom_line: str = " " + ("-" * (width_of_card + 2))
        self.text_line: str = ""

    @property
    def width_of_card(self):
        """Getter of width_of_card"""
        return self._width_of_card

    @width_of_card.setter
    def width_of_card(self, width_of_card):
        """Setter of width_of_card
        Args:
            width_of_card (_int_): _setting the value of width_of_card_
        Raises:
            ValueError: _The value of card width is out of range,The range is between 28 and 44_
        """
        if 28 <= width_of_card <= 44:
            self._width_of_card = width_of_card
        else:
            raise ValueError(
                "The value of card width is out of range \n The range is between 28 and 44"
            )

    @property
    def top_line(self):
        return self._top_line

    @property
    def blank_line(self):
        return self._blank_line

    @property
    def buttom_line(self):
        return self._buttom_line

    def add_lines(self, *sentences) -> None:
        for sentence in sentences:
            lines_per_sentence = [""]
            num_of_sentence_chars = len(sentence)
            index_line = 0
            start_line = 0
            end_line = 32
            if 0 < num_of_sentence_chars <= 192:
                num_of_lines = int(round(num_of_sentence_chars / 32))
                if num_of_lines == 0:
                    num_of_lines = 1
                while index_line in range(num_of_lines):
                    lines_per_sentence[index_line] = sentence[start_line:end_line]
                    lines_per_sentence.append("")
                    start_line = end_line
                    end_line += 32
                    index_line += 1
            else:
                raise ValueError("Maximum number of characters is 192 per line")
            for i in range(len(lines_per_sentence) - 1):
                self.text_line += (
                    "| "
                    + (
                        lines_per_sentence[i]
                        + " " * (self.width_of_card - len(lines_per_sentence[i]))
                    )
                    + "  #"
                    + "\n"
                )

    def print_here(self) -> str:
        return f"{self._top_line}{self._blank_line}{self.text_line}{self._blank_line}{self._buttom_line}"

    def __str__(self) -> str:
        return f"{self._top_line}{self._blank_line}{self.text_line}{self._blank_line}{self._buttom_line}"


def init_header(
    header: str, fore_color: str = "#ffffff", back_color: str = "#000000"
) -> str:
    """Asking for column names"""
    if bool(header) == False:
        raise ValueError("The Maximum Number of stages is 5 and The Minimum Number is 3 \nPlease Check agian ")
    
    """ add colors to header"""
    if len(fore_color) != 7 or fore_color[0] != "#":
        raise ValueError("Please Enter a Right Value !!")
    color = fg(fore_color)
    
    if len(back_color) != 7 or back_color[0] != "#":
        raise ValueError("Please Enter a Right Value !!")
    color += bg(back_color)

    return color + " " + header + " " + attr("reset")


def init_table(file_table_name: str) -> str:
    if "." in file_table_name:
        file_table_name, _ = file_table_name.split(".")
    if os.path.isfile(f"{DATA_DIR}{file_table_name}.csv"):
        return f"{file_table_name}"
    else:
        clearConsole()
        """
        print(
            "It looks like you have not created that table before\nIt will be created"
        )
        """
        file = open(f"{DATA_DIR}{file_table_name}.csv", "w")
        file.close()
        f_name = file.name
        if DATA_DIR in f_name:
            f_name = f_name.replace(DATA_DIR, "")
        return init_table(f_name)


def view_tables() -> list[str]:
    dir_path = f"{DATA_DIR}"
    tables_list = []
    for path in os.scandir(dir_path):
        if path.is_file():
            if path.name == ".DS_Store":
                continue
            tables_list.append(path.name)
    return tables_list
    ...


def open_table(table_name: str) -> any:
    #clearConsole()

    ...

def edit_table_mode (table_name: str) -> None:
    
    ...

def menu() -> int:
    option_menu: list = ["View Tables", "Create Table", "Exit"]
    while True:
        print("Menu:")
        for index, option in enumerate(option_menu):
            print(" " + str(index + 1) + " => " + option)
        selected_option: int = int(input("Enter the number of option in menu: ")) - 1
        if selected_option in range(len(option_menu)):
            return selected_option
        else:
            clearConsole()
            menu()
    ...


def clearConsole():
    command = "clear"
    if os.name in ("nt", "dos"):  # If computer is running windows use cls
        command = "cls"
    os.system(command)


def main():
    clearConsole()

    print(
        fg("#fcdb03")
        + """
    
                    
        $$$$$$$\            $$\   $$\                     $$\                           
        $$  __$$\           $$ | $$  |                    $$ |                          
        $$ |  $$ |$$\   $$\ $$ |$$  /  $$$$$$\  $$$$$$$\  $$$$$$$\   $$$$$$\  $$$$$$$\  
        $$$$$$$  |$$ |  $$ |$$$$$  /   \____$$\ $$  __$$\ $$  __$$\  \____$$\ $$  __$$\ 
        $$  ____/ $$ |  $$ |$$  $$<    $$$$$$$ |$$ |  $$ |$$ |  $$ | $$$$$$$ |$$ |  $$ |
        $$ |      $$ |  $$ |$$ |\$$\  $$  __$$ |$$ |  $$ |$$ |  $$ |$$  __$$ |$$ |  $$ |
        $$ |      \$$$$$$$ |$$ | \$$\ \$$$$$$$ |$$ |  $$ |$$$$$$$  |\$$$$$$$ |$$ |  $$ |
        \__|       \____$$ |\__|  \__| \_______|\__|  \__|\_______/  \_______|\__|  \__|
                  $$\   $$ |                                                            
                  \$$$$$$  |                                                            
                   \______/                                                             

    """
        + attr("reset")
    )

    while True:
        selected_option = menu()
        # View Tables
        if selected_option == 0:
            clearConsole()
            tables_list: list[str] = view_tables()
            for index, table_name in enumerate(tables_list):
                print(f"{index + 1}: {table_name.replace('.csv', '')}")
            selected_table: int = int(input("Enter Number of Table to Open: "))
            print(tables_list)
            open_table(tables_list[selected_table])
            time.sleep(15)
            clearConsole()
            continue
        # Create Table
        elif selected_option == 1:
            clearConsole()
            asked_table_name: str = str(input("Name of New Table is: "))
            edit_table_mode(init_table(asked_table_name))
            #a function that run a 'Edit table mode'
            
            #clearConsole()
            continue
        else:
            clearConsole()
            print("PyKanban will exit in")
            t = 5
            while t:
                mins, secs = divmod(t, 60)
                timer = "{:02d}:{:02d}".format(mins, secs)
                print(timer, end="\r")
                time.sleep(1)
                t -= 1
            clearConsole()
            sys.exit()


if __name__ == "__main__":
    main()
