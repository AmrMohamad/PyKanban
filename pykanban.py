from tabulate import tabulate
from colored import fg, bg, attr
import csv
import os
import sys
import re
import time


DATA_DIR = "./data/"


class Card:

    _width_of_card: int = 46
    _top_line: str = " " + ("#" * (_width_of_card + 2)) + "#" + "\n"
    _blank_line: str = "| " + (" " * (_width_of_card + 2)) + "#" + "\n"
    _buttom_line: str = " " + ("-" * (_width_of_card + 2))
    text_line: str = ""
    title: str = ""
    sub_titles: dict[str] = {}

    @property
    def width_of_card(cls):
        """Getter of width_of_card"""
        return cls._width_of_card

    @width_of_card.setter
    def width_of_card(cls, width_of_card):
        """Setter of width_of_card
        Args:
            width_of_card (_int_): _setting the value of width_of_card_
        Raises:
            ValueError: _The value of card width is out of range,The range is between 28 and 44_
        """
        if 28 <= width_of_card <= 48:
            cls._width_of_card = width_of_card
        else:
            raise ValueError(
                "The value of card width is out of range \n The range is between 28 and 44"
            )

    @property
    def top_line(cls):
        return cls._top_line

    @property
    def blank_line(cls):
        return cls._blank_line

    @property
    def buttom_line(cls):
        return cls._buttom_line

    @classmethod
    def add_title(cls, title: str) -> None:
        e = ValueError(
            "It should be there title\nWithout entering empty title (like just hit enter)"
        )
        if bool(title) == False:
            raise e
        if 0 < len(title) < 34:
            cls.title = title
        else:
            raise ValueError("The Maximum No. of Characters for Title is 34")

    @classmethod
    def add_sub_titles(cls, sub_title: list[str]) -> None:
        e = ValueError(
            "It should be there at lest 3 sub-titles and maximum 5 sub-titles\nWithout entering empty sub-title (like just hit enter)"
        )
        if bool(sub_title) == False:
            raise e
        for i in sub_title:
            if i == "":
                raise e
            else:
                continue
        cls.sub_titles = {}
        if 3 <= len(sub_title) <= 5:
            for s_t in sub_title:
                cls.sub_titles[s_t] = ""
            return cls
        else:
            raise e

    @classmethod
    def add_lines(cls, *e_sentences) -> None:
        i = 0
        for t in cls.sub_titles:
            cls.sub_titles[t] = e_sentences[i]
            i += 1
        sentences = cls.sub_titles
        for key_sentence in sentences:
            lines_per_sentence = []
            sentences[key_sentence] = (" " * len(key_sentence)) + sentences[
                key_sentence
            ]
            num_of_sentence_chars = len(sentences[key_sentence])
            start_line = 0
            end_line = 45
            if 0 < num_of_sentence_chars <= 244:
                num_of_lines = int(round(num_of_sentence_chars / 45))
                lines_per_sentence.append((key_sentence + " :"))
                lines_per_sentence.append("")
                for index_line in range(num_of_lines + 1):
                    lines_per_sentence[index_line + 1] = sentences[key_sentence][
                        start_line:end_line
                    ]
                    lines_per_sentence.append("")
                    start_line = end_line
                    end_line += 45
            else:
                raise ValueError("Maximum number of characters is 192 per line")
            cls.text_line = ""
            for i in range(len(lines_per_sentence)):
                cls.text_line += (
                    "| "
                    + (
                        lines_per_sentence[i]
                        + " " * (cls._width_of_card - len(lines_per_sentence[i]))
                    )
                    + "  #"
                    + "\n"
                )
        return cls

    @classmethod
    def print_here(cls) -> str:
        return f"{cls._top_line}{cls._blank_line}{cls.text_line}{cls._blank_line}{cls._buttom_line}"

    """
    def __str__(self) -> str:
        return f"{self._top_line}{self._blank_line}{self.text_line}{self._blank_line}{self._buttom_line}" """


def init_header(
    header: str, fore_color: str = "#ffffff", back_color: str = "#000000"
) -> str:
    """Checking for column names it should be set"""
    if bool(header) == False:
        raise ValueError("Please check, re-enter name of header maybe you missed one")

    """ add colors to header and check if they correct in hex value or not"""
    if f_color := re.search(r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$", fore_color):
        color = fg(f_color.group(0))
    else:
        raise TypeError(
            "Please Enter a Right Value !!\nOR Not a valid value in hex code of color"
        )

    if b_color := re.search(r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$", back_color):
        color += bg(b_color.group(0))
    else:
        raise TypeError(
            "Please Enter a Right Value !!\nOR Not a valid value in hex code of color"
        )

    return color + "    " + header + "    " + attr("reset")


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


def open_table(table_name: str) -> list:
    clearConsole()
    vt = []
    with open(f"{DATA_DIR}{table_name}", "r") as vtable:
        reader = csv.DictReader(vtable)
        vt = {h:[] for h in reader.fieldnames}
        for row in reader:
            for _,h_p in enumerate(reader.fieldnames):
                vt[h_p].append((f'{row[h_p]}'.replace('\\n', '\n')))
    return vt


def menu() -> int:
    option_menu: list = ["View Tables", "Create Table", "Exit"]
    while True:
        print("Menu:")
        for index, option in enumerate(option_menu):
            print(" " + str(index + 1) + " => " + option)
        try:
            selected_option: int = (
                int(input("Enter the number of option in menu: ")) - 1
            )
        except ValueError:
            print("Please re-enter a number of menu list in right way as integer")
            time.sleep(2)
            clearConsole()
            continue

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
        match selected_option:
            # View Tables
            case 0:
                clearConsole()
                tables_list: list[str] = view_tables()
                for index, table_name in enumerate(tables_list):
                    print(f"{index + 1}: {table_name.replace('.csv', '')}")
                selected_table: int = int(input("Enter Number of Table to Open: ")) - 1
                print(
                    tabulate(
                        open_table(tables_list[selected_table]),
                        headers="keys",
                        tablefmt="double_grid",
                        stralign="center",
                    )
                )
                time.sleep(15)
                clearConsole()
                continue
            # Create Table
            case 1:
                clearConsole()
                asked_table_name: str = str(input("Name of New Table is: "))
                with open(
                    f"{DATA_DIR}{init_table(asked_table_name)}.csv", "a", newline=""
                ) as table:
                    table_data: dict = {}
                    headers: list[str] = []
                    num_stages: int = 0
                    while True:
                        n_s: int = int(input("Number of stages"))
                        if 3 <= n_s <= 5:
                            num_stages = n_s
                            break
                        else:
                            print("The Maximum Stages is 5\nThe Minimum Stages is 3")
                            time.sleep(4)
                            continue
                    for _ in range(num_stages):
                        while True:
                            header: str = input("Names of column: ")
                            fore_color: str = input("Foreground color of Text in HEX: ")
                            back_color: str = input("Background color of Text in HEX: ")
                            try:
                                h = init_header(header, fore_color, back_color)
                                break
                            except (ValueError, TypeError) as e:
                                print(e)
                                continue
                        headers.append(h)
                    for h in headers:
                        cards = []
                        while True:
                            try:
                                num_of_cards = int(
                                    input("How many cards do you want?  ")
                                )
                                break
                            except ValueError:
                                print(
                                    "Please Enter the Number of Cards do you want in the right way\n only numbers like 1 2 3 ... etc"
                                )
                                continue
                        for card_num in range(num_of_cards):
                            print(
                                "Enter the name of each sub-title, The maximum is 4 sub-titles !"
                            )
                            added_sub_titles: list[str] = []
                            n_c = 0
                            while n_c != 3:
                                added_sub_titles.append(input("==> "))
                                n_c += 1
                            added_lines: list[str] = []
                            print(
                                "Enter the data of each sub-title, The maximum is 244 characters per paragraph !"
                            )
                            for _, s_title in enumerate(added_sub_titles):
                                print(
                                    "Do not hit enter for new line,\nWe handle it automatically"
                                )
                                print(f"For {s_title} :")
                                added_lines.append(input(">>> "))
                            cards.append(
                                Card.add_sub_titles(added_sub_titles)
                                .add_lines(*added_lines)
                                .print_here()
                            )
                        table_data[h] = cards
                    print(
                        tabulate(
                            table_data,
                            headers="keys",
                            tablefmt="double_grid",
                            stralign="center",
                        )
                    )
                    writer = csv.DictWriter(table, fieldnames=headers)
                    writer.writeheader()
                    writer.writerow(table_data)
                # clearConsole()
                continue
            # Exit
            case _:
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
