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


DATA_DIR = "./data/"
p = inflect.engine()


class Card:

    _width_of_card: int = 46
    _top_line: str = " " + ("#" * (_width_of_card + 2)) + "#" + "\n"
    _blank_line: str = "| " + (" " * (_width_of_card + 2)) + "#" + "\n"
    _buttom_line: str = " " + ("-" * (_width_of_card + 2))
    text_line: str = ""
    title: str = ""
    sub_titles: dict = {}

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
    def add_title(cls, added_title: str) -> any:
        e = ValueError(
            "It should be there title\nWithout entering empty title (like just hit enter)"
        )
        if bool(added_title) == False:
            raise e
        cls.title = ""
        if 0 < len(added_title) < 34:
            padding_for_center_title = int((cls._width_of_card - len(added_title)) / 2)
            added_title = (
                "| "
                + (
                    padding_for_center_title * " "
                    + added_title
                    + padding_for_center_title * " "
                )
                + "  #"
                + "\n"
            )
            cls.title = added_title
            return cls
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
        if 1 <= len(sub_title) <= 5:
            for s_t in sub_title:
                cls.sub_titles[s_t] = ""
            return cls
        else:
            raise e

    @classmethod
    def add_lines(cls, *e_sentences) -> any:
        cls.text_line = ""
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
        return f"{cls._top_line}{cls.title}{cls._blank_line}{cls.text_line}{cls._buttom_line}"


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


def init_table(table_name: str) -> str:
    if table_name == None or table_name == "":
        raise TypeError("There is not Table Name check again please")
    if os.path.isdir(f"{DATA_DIR}{table_name}") and os.path.isfile(
        f"{DATA_DIR}{table_name}/latest.csv"
    ):
        return f"{table_name}"
    else:
        os.makedirs(f"{DATA_DIR}{table_name}")
        file = open(f"{DATA_DIR}{table_name}/latest.csv", "w")
        file.close()
        return init_table(table_name)


def view_tables() -> list[str]:
    dir_path = f"{DATA_DIR}"
    if len(os.listdir(dir_path)) == 0:
        return f"No Tables Exist"
    tables_list = []
    for path in os.scandir(dir_path):
        if path.is_dir():
            if path.name == ".DS_Store":
                continue
            tables_list.append(path.name)
    return tables_list


def view_history(table_name: str) -> list[str]:
    dir_path = f"{DATA_DIR}{table_name}"
    tables_list = []
    for path in os.scandir(dir_path):
        if path.is_file():
            if path.name == ".DS_Store" or path.name in ["latest.csv", "latest"]:
                continue
            if matches := re.search(
                r"^_ (([0-2][0-9]|[3][0-1])-([0][1-9]|[1][1-2])-((19|20)\d\d)) ((1[0-2]|0?[1-9])\.[0-5][0-9]\.[0-5][0-9] (AM|PM))\.csv$",
                path.name,
            ):
                tables_list.append(matches.string)
    return tables_list


def open_table(table_name: str, table_version: str = None) -> dict:
    vt: dict = {}
    if bool(table_name) == False:
        raise TypeError(
            "There is no table name, please check again there is and it's right"
        )
    if table_name not in os.listdir(DATA_DIR):
        raise FileNotFoundError("The Table not exist or The Table Name is not right")
    if bool(table_version) == False:
        with open(f"{DATA_DIR}{table_name}/latest.csv", "r") as vtable:
            reader = csv.DictReader(vtable)
            vt = {h: [] for h in reader.fieldnames}
            for row in reader:
                for h_p in reader.fieldnames:
                    f_data = row[h_p].replace("\\n", "\n")
                    vt[h_p].append(f_data)
    else:
        table_file_name = ""
        if matches := re.search(
            r"^_ (([0-2][0-9]|[3][0-1])-([0][1-9]|[1][1-2])-((19|20)\d\d)) ((1[0-2]|0?[1-9])\.[0-5][0-9]\.[0-5][0-9] (AM|PM))\.csv$",
            table_version,
        ):
            table_file_name = matches.string

        with open(f"{DATA_DIR}{table_name}/{table_file_name}", "r") as vtable:
            reader = csv.DictReader(vtable)
            vt = {h: [] for h in reader.fieldnames}
            for row in reader:
                for h_p in reader.fieldnames:
                    f_data = row[h_p].replace("\\n", "\n")
                    vt[h_p].append(f_data)
    return vt


def save_table(table_name:str,table_data:dict):
    os.rename(
        f"{DATA_DIR}{table_name}/latest.csv",
        f"{DATA_DIR}{table_name}/_ {datetime.now().strftime('%d-%m-%Y %I.%M.%S %p')}.csv",
    )
    with open(f"{DATA_DIR}{table_name}/latest.csv", "w") as new_table:
        writer = csv.DictWriter(new_table, fieldnames=list(table_data.keys()))
        writer.writeheader()
        longest_header_in_cards = 0
        for c in list(table_data.keys()):
            if longest_header_in_cards < len(table_data[c]):
                longest_header_in_cards = len(table_data[c])
            else:
                continue
        for row in range(longest_header_in_cards):
            cards_in_row = {}
            for header_pointer in table_data:
                if row in range(len(table_data[header_pointer])):
                    cards_in_row[header_pointer] = table_data[header_pointer][row]
                else:
                    continue
            writer.writerow(cards_in_row)


def add_card(
    table_name_to_edit: str = "",
    name_of_card: str = "",
    add_to_column_name: str = "",
    sub_titles: list[str] = [],
    lines_per_sub_title: list[str] = [],
) -> str:

    added_card = (
        Card.add_title(name_of_card)
        .add_sub_titles(sub_titles)
        .add_lines(*lines_per_sub_title)
        .print_here()
    )
    try:
        old_card_table: dict = open_table(table_name_to_edit)
    except FileNotFoundError:
        is_card_added = "NotAdded"
        raise TypeError("Please check of Name of Table")
    columns_name = list(old_card_table.keys())
    new_card_table: dict = {header_name: [] for header_name in columns_name}
    c_exist = False
    is_card_added = ""
    for cn in columns_name:
        if add_to_column_name in cn:
            old_card_table[cn].append(added_card)
            is_card_added = "Added"
            c_exist = True
            break
        else:
            continue
    if c_exist == False:
        raise ValueError("The Column name does not exist")

    for h_n in columns_name:
        for c in old_card_table[h_n]:
            if c != "":
                new_card_table[h_n].append(c)
            else:
                continue
    save_table(table_name_to_edit,new_card_table)
    if is_card_added != "Added":
        raise TypeError("Please check of Name of card and Name of Table")
    return is_card_added


def move_card(table_name_to_edit: str, card_name: str, move_to: str) -> str:
    is_moved_right: str = ""
    try:
        old_card_table: dict = open_table(table_name_to_edit)
    except FileNotFoundError:
        is_moved_right = "NotMoved"
        raise TypeError("Please check of Name of Table")
    card: str = ""
    """for holding the Card that will change his place
    """
    column_index_card: int = 0
    """for know the old place of card to delete it 
    """
    columns_name = list(old_card_table.keys())
    """headers names
    """
    new_card_table: dict = {header_name: [] for header_name in columns_name}
    """Adding headers for new table
    """
    reader = csv.reader(open(f"{DATA_DIR}{table_name_to_edit}/latest.csv", "r"))
    break_out_flag = False  # for break nested loops at once
    cd_exist = False
    for row in reader:
        """for reading each row in file"""
        for column in row:
            """for read each column in the row"""
            if card_name in column:
                """Searching about the Card that we want to move to other column"""
                column_index_card += row.index(column)
                card = column
                cd_exist = True
                old_card_table[columns_name[column_index_card]].remove(column)
                break_out_flag = True
                break
            else:
                continue
        if break_out_flag:  # for break nested loops at once
            break
    if cd_exist == False and card == "":
        raise ValueError("The Card name is not exist, Please check again")
    c_exist = False
    for col_name in columns_name:
        """Searching about header we want to move the card to him"""
        if move_to in col_name:
            old_card_table[col_name].append(card)
            is_moved_right = "Moved"
            c_exist = True
            break
        else:
            continue
    if c_exist == False:
        raise ValueError("The Column name does not exist")
    for h_n in columns_name:
        for c in old_card_table[h_n]:
            if c != "":
                new_card_table[h_n].append(c)
            else:
                continue
    save_table(table_name_to_edit,new_card_table)
    if is_moved_right != "Moved":
        raise TypeError(
            "the card is not moved, please check of card name, column name and table name"
        )
    return is_moved_right


def delete_card(table_name_to_edit: str, card_name: str) -> str:
    is_card_deleted: str = ""
    try:
        old_card_table: dict = open_table(table_name_to_edit)
    except FileNotFoundError:
        is_card_deleted = "NotDeleted"
        raise TypeError("Please check of Name of Table")
    columns_name = list(old_card_table.keys())
    new_card_table: dict = {header_name: [] for header_name in columns_name}
    reader = csv.reader(open(f"{DATA_DIR}{table_name_to_edit}/latest.csv", "r"))
    break_out_flag = False  # for break nested loops at once
    cd_exist = False
    for row in reader:
        """for reading each row in file"""
        for column in row:
            """for read each column in the row"""
            if card_name in column:
                """Searching about the Card that we want to move to other column"""
                old_card_table[columns_name[row.index(column)]].remove(column)
                break_out_flag = True
                cd_exist = True
                is_card_deleted = "Deleted"
                break
            else:
                continue
        if break_out_flag:  # for break nested loops at once
            break
    if cd_exist == False:
        raise ValueError("The Card name is not exist, Please check again")
    for h_n in columns_name:
        for c in old_card_table[h_n]:
            if c != "":
                new_card_table[h_n].append(c)
            else:
                continue
    save_table(table_name_to_edit,new_card_table)
    if is_card_deleted != "Deleted":
        raise ValueError(
            "the card is not deleted, please check if the card name is right"
        )
    return is_card_deleted


def menu(type_menu: str) -> int:
    match type_menu:
        case "main":
            option_menu_main: list = ["View Tables", "Create Table", "Exit"]
            print("Menu:")
            for index, option in enumerate(option_menu_main):
                print(" " + str(index + 1) + " => " + option)
            try:
                selected_option_menu_main: int = (
                    int(input("Enter the number of option in menu: ")) - 1
                )
            except ValueError:
                print("Please re-enter a number of menu list in right way as integer")
                time.sleep(2)
                clearConsole()
            if selected_option_menu_main in range(len(option_menu_main)):
                return selected_option_menu_main
            else:
                clearConsole()
                menu("main")
        case "edit":
            option_menu_edit: list = [
                "Add a Card",
                "Move a Crad",
                "Delete a Card",
                "View History",
                "Back to Main Screen",
            ]
            print("Options:")
            for index, option in enumerate(option_menu_edit):
                print(" " + str(index + 1) + " => " + option + " ", end="")
            print()
            try:
                selected_option_menu_edit: int = (
                    int(input("Enter the number of option: ")) - 1
                )
            except ValueError:
                print("Please re-enter a number of option in right way as integer")
                time.sleep(2)
                # clearConsole()
            if selected_option_menu_edit in range(len(option_menu_edit)):
                return selected_option_menu_edit
            else:
                clearConsole()
                menu("edit")


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
        selected_option = menu("main")
        match selected_option:
            # View Tables
            case 0:
                clearConsole()
                #tables_list: list[str] = [t.replace(".csv", "") for t in view_tables()]
                if view_tables() == "No Tables Exist":
                    print("No Tables Exist")
                    time.sleep(4)
                    clearConsole()
                    main()
                else:
                    tables_list: list[str] = [t.replace(".csv", "") for t in view_tables()]
                for index, table_name in enumerate(tables_list):
                    print(f"{index + 1}: {table_name}")
                selected_table: int = int(input("Enter Number of Table to Open: ")) - 1
                clearConsole()
                try:
                    table_to_view = open_table(tables_list[selected_table])
                except TypeError as e:
                    print(e)
                print(
                    tabulate(
                        table_to_view,
                        headers="keys",
                        tablefmt="double_grid",
                        stralign="center",
                    )
                )
                time.sleep(1)
                print()
                while True:
                    selected_action = menu("edit")
                    match selected_action:
                        # Add a Crad
                        case 0:
                            print("Enter the Title of Card, It's one title only !")
                            title_of_added_card = input("==> ")
                            while True:
                                num_of_sub_titles = int(
                                    input(
                                        "How many sub-titles do you want to add ? => "
                                    )
                                )
                                if 1 <= num_of_sub_titles <= 5:
                                    break
                                else:
                                    if num_of_sub_titles < 2:
                                        print(
                                            "It's less than minimum, at least 1 sub-title"
                                        )
                                        continue
                                    if num_of_sub_titles > 5:
                                        print(
                                            "It's more than maximum, the maximum is 5 sub-titles"
                                        )
                                        continue
                            print("Enter the name of each sub-title")
                            sub_titles_of_added_card: list[str] = []
                            for _ in range(num_of_sub_titles):
                                sub_titles_of_added_card.append(input(" => "))
                            print(
                                "Enter the data of each sub-title, The maximum is 244 characters per paragraph !"
                            )
                            added_lines_of_added_card: list[str] = []
                            for st in sub_titles_of_added_card:
                                print(f"For {st} :")
                                added_lines_of_added_card.append(input(">>> "))
                            data_of_added_card: dict = {
                                "sub_titles": sub_titles_of_added_card,
                                "lines_per_sub_title": added_lines_of_added_card,
                            }
                            add_to_column = input(
                                "Which Column do you want to put the Card in? =>"
                            )
                            add_card(
                                table_name_to_edit=tables_list[selected_table],
                                name_of_card=title_of_added_card,
                                add_to_column_name=add_to_column,
                                **data_of_added_card,
                            )
                        # Move a Crad
                        case 1:
                            while True:
                                try:
                                    name_of_card_to_move = input(
                                        "Enter the Title of Card => "
                                    )
                                    column_move_to = input(
                                        "Which Column do you want to put the Card in? => "
                                    )
                                    state = move_card(
                                        tables_list[selected_table],
                                        name_of_card_to_move,
                                        column_move_to,
                                    )
                                    if state == "Moved":
                                        print(
                                            f"{name_of_card_to_move} moved to {column_move_to} successfully"
                                        )
                                    break
                                except ValueError as e:
                                    print(e)
                                    continue
                        # Delete a Card
                        case 2:
                            while True:
                                try:
                                    name_of_card_to_delete = input(
                                        "Enter the Title of Card => "
                                    )
                                    state = delete_card(
                                        tables_list[selected_table],
                                        name_of_card_to_delete,
                                    )
                                    if state == "Deleted":
                                        print(
                                            f"{name_of_card_to_delete} Deleted Successfully"
                                        )
                                    break
                                except ValueError as e:
                                    print(e)
                                    continue
                        # View History
                        case 3:
                            while True:
                                history_list: list[str] = [
                                    ht
                                    for ht in view_history(tables_list[selected_table])
                                ]
                                clearConsole()
                                for index, t_name in enumerate(history_list):
                                    if matches := re.search(
                                        r"^_ (([0-2][0-9]|[3][0-1])-([0][1-9]|[1][1-2])-((19|20)\d\d)) ((1[0-2]|0?[1-9])\.[0-5][0-9]\.[0-5][0-9] (AM|PM))\.csv$",
                                        t_name,
                                    ):
                                        print(
                                            f"{index + 1}: Edited on {matches.group(1)} at {matches.group(6)}"
                                        )
                                selected_old_table: int = (
                                    int(
                                        input(
                                            "Enter the Number of the Old Table to View: "
                                        )
                                    )
                                    - 1
                                )
                                print(
                                    tabulate(
                                        open_table(
                                            tables_list[selected_table],
                                            table_version=history_list[
                                                selected_old_table
                                            ],
                                        ),
                                        headers="keys",
                                        tablefmt="double_grid",
                                        stralign="center",
                                    )
                                )
                                input("Press any key to back...")
                                break
                        # Back to Main Screen
                        case 4:
                            clearConsole()
                            break
                    clearConsole()
                    print(
                        tabulate(
                            open_table(tables_list[selected_table]),
                            headers="keys",
                            tablefmt="double_grid",
                            stralign="center",
                        )
                    )
                main()
            # Create Table
            case 1:
                clearConsole()
                ask_table_name: str = str(input("Name of New Table is: "))
                while True:
                    try:
                        asked_table_name: str = init_table(ask_table_name)
                        break
                    except TypeError as e:
                        print(e)
                        continue
                with open(
                    f"{DATA_DIR}{asked_table_name}/latest.csv",
                    "a",
                    newline="",
                ) as table:
                    table_data: dict = {}
                    headers: list[str] = []
                    num_stages: int = 0
                    while True:
                        n_s: int = int(input("Number of stages => "))
                        if 2 <= n_s <= 5:
                            num_stages = n_s
                            break
                        else:
                            print("The Maximum Stages is 5\nThe Minimum Stages is 2")
                            time.sleep(4)
                            continue
                    clearConsole()
                    for num_s in range(num_stages):
                        print()
                        print(f"For {p.ordinal( 1 + num_s )} Stage")
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
                    clearConsole()
                    for h in headers:
                        cards = []
                        print(f"For {h}")
                        while True:
                            try:
                                num_of_cards = int(
                                    input("How many cards do you want?  ")
                                )
                                break
                            except ValueError:
                                print(
                                    "Please Enter the Number of Cards do you want in the right way\n only integer numbers like 0, 1, 2, ... etc"
                                )
                                continue
                        for card_num in range(num_of_cards):
                            print(f"For {p.ordinal( 1 + card_num )} Card")
                            print("Enter the Title of Card, It's one title only !")
                            title_of_card = input("==> ")
                            added_sub_titles: list[str] = []
                            while True:
                                try:
                                    num_of_sub_titles_in_card = int(
                                        input(
                                            "How many sub-titles do you want to add ? => "
                                        )
                                    )
                                    if 1 <= num_of_sub_titles_in_card <= 5:
                                        break
                                    else:
                                        if num_of_sub_titles_in_card < 2:
                                            print(
                                                "It's less than minimum, at least 1 sub-title"
                                            )
                                            continue
                                        if num_of_sub_titles_in_card > 5:
                                            print(
                                                "It's more than maximum, the maximum is 5 sub-titles"
                                            )
                                            continue
                                except ValueError:
                                    print(
                                        "Please Enter the Number of Sub-Titles do you want in the right way\n only integer numbers like 0, 1, 2, ... etc"
                                    )
                            print("Enter the name of each sub-title")
                            for _ in range(num_of_sub_titles_in_card):
                                added_sub_titles.append(input(">>> "))
                            added_lines: list[str] = []
                            print(
                                "Enter the content of each sub-title, The maximum is 244 characters per paragraph !"
                            )
                            for _, s_title in enumerate(added_sub_titles):
                                print(
                                    "Do not hit enter for new line,\nWe handle it automatically"
                                )
                                print(f"For {s_title} :")
                                added_lines.append(input(">>> "))

                            cards.append(
                                Card.add_title(title_of_card)
                                .add_sub_titles(added_sub_titles)
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
                    time.sleep(5)
                    writer = csv.DictWriter(table, fieldnames=headers)
                    writer.writeheader()
                    longest_header_in_cards = 0
                    for h in headers:
                        if longest_header_in_cards < len(table_data[h]):
                            longest_header_in_cards = len(table_data[h])
                        else:
                            continue
                    for row in range(longest_header_in_cards):
                        cards_in_row = {}
                        for header_pointer in table_data:
                            if row in range(len(table_data[header_pointer])):
                                cards_in_row[header_pointer] = table_data[
                                    header_pointer
                                ][row]
                            else:
                                continue
                        writer.writerow(cards_in_row)
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
