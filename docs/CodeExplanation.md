# PyKanban - Code Explanation

## Constants

```py
DATA_DIR = "./data/"
```

This variable contains the path to the directory containing the data files.

## inflect engine

depending on the <a href="https://pypi.org/project/inflect/">documentation</a> of inflect module we need to initialize an object for <code>engine</code>

```py
p = inflect.engine()
```

## Card class

```py
class Card:
    _width_of_card: int = 46
    _top_line: str = " " + ("#" * (_width_of_card + 2)) + "#" + "\n"
    _blank_line: str = "| " + (" " * (_width_of_card + 2)) + "#" + "\n"
    _bottom_line: str = " " + ("-" * (_width_of_card + 2))
    text_line: str = ""
    title: str = ""
    sub_titles: dict = {}

    @property
    def width_of_card(cls):
        return cls._width_of_card

    @width_of_card.setter
    def width_of_card(cls, width_of_card):
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
    def bottom_line(cls):
        return cls._bottom_line

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
        for key_sentence in cls.sub_titles:
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
                wrapped_text = textwrap.wrap(sentences[key_sentence], width=46)
                for line in wrapped_text:
                    lines_per_sentence.append(line)
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
        return f"{cls._top_line}{cls.title}{cls._blank_line}{cls.text_line}{cls._bottom_line}"

```

The Card class is a class that can be used to create and print a card with a title, sub-titles, and sentences.

### Attributes

The class has the following attributes:

```py
    _width_of_card: int = 46
    _top_line: str = " " + ("#" * (_width_of_card + 2)) + "#" + "\n"
    _blank_line: str = "| " + (" " * (_width_of_card + 2)) + "#" + "\n"
    _bottom_line: str = " " + ("-" * (_width_of_card + 2))
    text_line: str = ""
    title: str = ""
    sub_titles: dict = {}
```

_width_of_card (int): The width of the card in characters.

_top_line (str): The top border of the card.

_blank_line (str): A blank line in the card.

_bottom_line (str): The bottom border of the card.

text_line (str): The text in the body of the card.

title (str): The title of the card.

sub_titles (dict): A dictionary of sub-titles and their corresponding text.

<br>

### The classmethods of Card class:

```py
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
        for key_sentence in cls.sub_titles:
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
                wrapped_text = textwrap.wrap(sentences[key_sentence], width=46)
                for line in wrapped_text:
                    lines_per_sentence.append(line)
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
        return f"{cls._top_line}{cls.title}{cls._blank_line}{cls.text_line}{cls._bottom_line}"
```

#### add_title method

```py
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
```

The add_title method allows the user to set the title of the card by passing a string to the method. The method first checks if the string is empty, and if it is, it raises a ValueError with a message prompting the user to enter a non-empty title. If the string is not empty, the method checks if it is less than 34 characters long, and if it is not, it raises a ValueError with a message indicating that the maximum number of characters for the title is 34. If the string is not empty and less than 34 characters long, the method centers the string within the card and stores it in the title attribute.

#### add_sub_titles method

```py
    @classmethod
    def add_sub_titles(cls, sub_title: list[str]) -> None:
        e = ValueError(
            "It should be there at least 1 sub-title and maximum 5 sub-titles\nWithout entering empty sub-title (like just hit enter)"
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
```

The add_sub_titles method allows the user to set the sub-titles of the card by passing a list of strings to the method. The method first checks if the list is empty, and if it is, it raises a ValueError with a message prompting the user to enter at least non-empty sub-title. The method then checks if the list contains between 1 and 5 strings, and if it does not, it raises a ValueError with a message indicating that the number of sub-titles must be between 1 and 5. If the list is not empty and contains between 1 and 5 strings, the method adds each string in the list as a key in the sub_titles dictionary, with an empty string as the corresponding value.

#### add_lines method

```py
@classmethod
    def add_lines(cls, *e_sentences) -> any:
        cls.text_line = ""

        i = 0
        for t in cls.sub_titles:
            cls.sub_titles[t] = e_sentences[i]
            i += 1

        sentences = cls.sub_titles
        for key_sentence in cls.sub_titles:
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
                wrapped_text = textwrap.wrap(sentences[key_sentence], width=46)
                for line in wrapped_text:
                    lines_per_sentence.append(line)
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
```

The add_lines method allows the user to add sentences to the card by passing a variable number of arguments to the method. Each argument corresponds to a sentence for a specific sub-title. The method first initializes the text_line attribute to be empty. It then loops through each sub-title in the sub_titles dictionary and adds the corresponding sentence from the e_sentences input.

Next, the method loops through each sub-title and sentence in the sub_titles dictionary. For each sub-title and sentence, it initializes a list to store the lines of text for the current sub-title. It then adds a space after the sub-title to indent the sentence. The method then uses the textwrap.wrap method to split the sentence into a list of lines that are no longer than 45 characters long. These lines are added to the lines_per_sentence list.

Once all of the lines for the current sub-title have been added to the lines_per_sentence list, the method loops through the list and formats each line with the correct indentation and padding. The resulting lines are added to the text_line attribute, which stores all of the lines of text that make up the card.

#### print_here method

```py
    @classmethod
    def print_here(cls) -> str:
        return f"{cls._top_line}{cls.title}{cls._blank_line}{cls.text_line}{cls._bottom_line}"
```

The print_here method is used to display the card on the screen by returning a string containing the top_line, title, blank_line, text_line, and bottom_line attributes. This string can be printed to the screen to show the card.

## init_header function

```py
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
```

header (str): The header string to be checked and colored.

fore_color (str, optional): The foreground color of the header in hex code. The default value is #ffffff (white).

back_color (str, optional): The background color of the header in hex code. The default value is #000000 (black).

The init_header function is used to add color to a string that is used as a header in a table or kanban board. The function takes a string (header) as a required argument, and two optional arguments: fore_color and back_color. These arguments are used to specify the foreground (text) color and background color, respectively.

The function first checks if the header argument is empty. If it is, it raises a ValueError with an appropriate message. If the header is not empty, the function then uses a regular expression to check if the fore_color and back_color arguments are valid hexadecimal color codes. If either of them is not a valid hexadecimal color code, a TypeError is raised with an appropriate message.

If both the header and color arguments are valid, the function uses the fg and bg functions from the colored library to apply the specified colors to the header string. Finally, the function returns the colored header string.

## init_table function

```py
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
```

The init_table function in the given code checks if a table with the given name exists in the DATA_DIR directory. If the table does not exist, the function creates the table and its corresponding latest.csv file in the DATA_DIR directory.

 The function takes the following argument:

table_name (str): The name of the table to be checked or created.
The function raises a TypeError if the table_name string is empty or None. If the table_name is valid, the function checks if a directory with the same name exists in the DATA_DIR directory. If the directory exists and contains a latest.csv file, the function returns the table_name string. Otherwise, the function creates the directory and latest.csv file, and then calls itself recursively to check if the table was created successfully. This way, the function guarantees that the table and its latest.csv file are created before returning the table_name string.

## view_tables function

```py
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

```

The view_tables function is used in the PyKanban program to list the names of all tables that are currently stored in the DATA_DIR directory. The function takes no arguments and returns a list of strings, where each string is the name of a table.

The function first checks if the DATA_DIR directory is empty by using the os.listdir method. If the directory is empty, the function returns a string message saying that "No Tables Exist". If the directory is not empty, the function uses the os.scandir method to iterate through the contents of the DATA_DIR directory and identify any directories that are present. The function then adds the name of each directory (i.e., the name of each table) to the tables_list list, which is then returned by the function.

## open_table function

```py

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
```

The open_table function is used in the PyKanban program to open an existing table. The function takes two arguments:

table_name (str): The name of the table to open.
table_version (str): The version of the table to open. If no version is specified, the function opens the latest version of the table.

The function first checks if the table_name argument is valid (i.e. not empty or None) and if the table exists in the DATA_DIR directory. If either of these conditions is not met, the function raises an appropriate error.

Next, the function checks if a table_version was specified. If no table_version was specified, the function opens the latest.csv file in the table's directory and reads the data from the file using the csv module's DictReader. The data is then stored in a dictionary with the column names as keys and the corresponding column data as values.

If a table_version was specified, the function checks if the table_version string is in the correct format using a regular expression. If the table_version is valid, the function opens the corresponding .csv file and reads the data from the file in the same way as when no table_version is specified. If the table_version is invalid, the function raises a ValueError.

Finally, the function replaces any "\n" escape sequences in the data with actual newline characters and returns the data as a dictionary.

### Regular Expression at open_table function

The regular expression in the open_table function is used to validate the table_version argument. The table_version argument is an optional parameter that specifies the version of the table to open. If table_version is not provided, the function opens the latest version of the table.

The regular expression is defined as follows:

```py
r"^_ (([0-2][0-9]|[3][0-1])-([0][1-9]|[1][1-2])-((19|20)\d\d)) ((1[0-2]|0?[1-9])\.[0-5][0-9]\.[0-5][0-9] (AM|PM))\.csv$"
```

This regular expression is used to match the file name of a table version. The file name has the following format:

```py
_ dd-mm-yyyy hh.mm.ss AM/PM.csv
```

where dd, mm, yyyy, hh, mm, ss, AM/PM represent the day, month, year, hour, minute, second and AM/PM, respectively.

The regular expression matches the following parts of the file name:

- The underscore character (_) at the beginning of the file name
- The date in the format dd-mm-yyyy
- The time in the format hh.mm.ss AM/PM
- The .csv extension at the end of the file name

If the table_version argument matches the regular expression, the function extracts the file name from the table_version string using the .string attribute of the re.Match object. The extracted file name is used to open the corresponding table version.

If the table_version argument does not match the regular expression or is not provided, the function opens the latest version of the table by default.

## save_table function

```py
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
```

The save_table function is used to save changes made to a table in the PyKanban program. It takes two arguments:

table_name (str): The name of the table to save.
table_data (dict): A dictionary containing the data to be saved in the table. The keys of the dictionary represent the column names of the table, and the values are lists of strings containing the data in each column.

The function first renames the latest.csv file in the table's directory by appending the current date and time to its name. This is done to create a backup of the previous version of the table. Then, the function opens the latest.csv file again in write mode and creates a new DictWriter object using the fieldnames from the table_data dictionary as the column names for the table. The function then writes the column names to the file using the writeheader() method of the DictWriter object.

Next, the function loops through the values in the table_data dictionary and finds the longest list of strings. This is done to determine the number of rows in the table. The function then loops through the rows and creates a new dictionary containing the data for each row. The keys of the dictionary are the column names, and the values are the strings in the corresponding column at the current row. The function then writes the row data to the file using the writerow() method of the DictWriter object. This process is repeated for all rows in the table, saving the changes made to the table in the latest.csv file.


## add_card function

```py

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
```

The add_card function is used to add a card to a table in the PyKanban program. It takes several arguments:

table_name_to_edit (str): The name of the table to which the card will be added.

name_of_card (str): The name of the card to be added.

add_to_column_name (str): The name of the column in the table where the card will be added.

sub_titles (list[str]): A list of strings containing the sub-titles for the card.

lines_per_sub_title (list[str]): A list of strings containing the lines of text for each sub-title in the card.

The function first creates a new card using the Card class, passing the name_of_card, sub_titles, and lines_per_sub_title arguments to the add_title, add_sub_titles, and add_lines methods of the Card class, respectively. The function then uses the print_here method of the Card class to get the string representation of the card, which is stored in the added_card variable.

Next, the function tries to open the table with the given name using the open_table function. If the table does not exist, a FileNotFoundError is raised and a TypeError is thrown with an error message.

If the table exists, the function gets the column names of the table from the dictionary returned by the open_table function and creates a new dictionary named new_card_table to store the updated table data. The function then loops through the columns in the old table and checks if the add_to_column_name argument matches the name of any of the columns. If a match is found, the added_card is appended to the list of cards in that column and the c_exist variable is set to True. If no match is found, the c_exist variable remains False.

If the c_exist variable is False, the function raises a ValueError with an error message indicating that the given column name does not exist in the table. If the c_exist variable is True, the function loops through the old table data and adds the non-empty cards to the new_card_table dictionary. Finally, the function saves the updated table data using the save_table function and returns the string "Added" if the card was added successfully. If the card was not added, the function returns the string "NotAdded".

## move_card function

```py
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
```

The move_card function is used to move a card from one column to another in the PyKanban program. It takes three arguments:

table_name_to_edit (str): The name of the table containing the card to be moved.
card_name (str): The name of the card to be moved.
move_to (str): The name of the column to move the card to.

The function first opens the table using the open_table function and checks if the table exists. If the table does not exist, the function raises a TypeError. Next, the function loops through the rows and columns of the table using the csv module and finds the column containing the card to be moved. It saves the card's name and the column index and removes the card from the old column.

If the card is not found, the function raises a ValueError. The function then loops through the columns again and finds the column with the name specified in the move_to argument. If the column is not found, the function raises a ValueError. Otherwise, the function adds the card to the new column.

Finally, the function saves the updated table using the save_table function and returns a string indicating whether the card was moved successfully. If the card was not moved, the function raises a TypeError.

## delete_card function

```py

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
```

The delete_card function is used to delete a card from a table in the PyKanban program. It takes two arguments:

table_name_to_edit (str): The name of the table where the card to be deleted is located.
card_name (str): The name of the card to be deleted.

The function first tries to open the table with the given name using the open_table() function. If the table does not exist, a FileNotFoundError is raised.

Next, the function reads the latest.csv file for the table and searches for the card with the given name. If the card is found, the function removes it from the table data and sets a flag to indicate that the card was deleted.

Finally, the function saves the updated table data using the save_table() function and returns a message indicating whether the card was deleted or not. If the card was not found in the table, a ValueError is raised.

## view_history function

```py
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
```

The view_history function returns a list of all the saved versions of a table in the PyKanban program. It takes a single argument:

table_name (str): The name of the table whose history is to be viewed.

The function first gets the path to the directory containing the table files. It then loops through all the files in the directory and checks if the file name matches a specific pattern using a regular expression. This pattern is used to identify the saved versions of the table, which are the files with names starting with an underscore, followed by the date and time the table was saved, and ending with the .csv extension.

If a file name matches the pattern, the function adds it to the list of tables. The function then returns the list of tables, which can be used to view the history of the table.

## menu function

```py

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
                "Move a Card",
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

```

The menu function is a helper function used to display a menu of options to the user and prompt them to select an option. It takes a single argument type_menu which is a string representing the type of menu to display. There are two possible values for type_menu: "main" and "edit".

If type_menu is "main", the function displays the main menu with the following options: "View Tables", "Create Table", and "Exit". The function then prompts the user to enter the number corresponding to the option they want to select, and returns the zero-based index of the selected option.

If type_menu is "edit", the function displays the edit menu with the following options: "Add a Card", "Move a Card", "Delete a Card", "View History", and "Back to Main Screen". The function then prompts the user to enter the number corresponding to the option they want to select, and returns the zero-based index of the selected option.

If the user enters an invalid value, the function displays an error message and prompts the user to try again. The function continues to do this until the user enters a valid value.

## clearConsole function

```py
def clearConsole():
    command = "clear"
    if os.name in ("nt", "dos"):  # If computer is running windows use cls
        command = "cls"
    os.system(command)
```

The clearConsole() function is used to clear the console screen. It does this by running the clear command on Unix-based systems (such as Linux and macOS) and the cls command on Windows systems. This allows the user to see a fresh, clean console screen, which can be useful when working with a program that outputs a lot of text to the console.

___
**The following shows how all of the previous functions are used**

## main function

```py

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
                        # Add a Card
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
                                "Which Column do you want to put the Card in? => "
                            )
                            add_card(
                                table_name_to_edit=tables_list[selected_table],
                                name_of_card=title_of_added_card,
                                add_to_column_name=add_to_column,
                                **data_of_added_card,
                            )
                        # Move a Card
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
```

### selecting View Tables

```py

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
                        # Add a Card
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
                                "Which Column do you want to put the Card in? => "
                            )
                            add_card(
                                table_name_to_edit=tables_list[selected_table],
                                name_of_card=title_of_added_card,
                                add_to_column_name=add_to_column,
                                **data_of_added_card,
                            )
                        # Move a Card
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
```

When the user selects the "View Tables" option from the main menu, the main function will call the view_tables function, which will return a list of the names of all the tables that exist in the tables directory. If there are no tables, the view_tables function will return the string "No Tables Exist".

Next, the main function will iterate over the list of table names, printing each table name with a corresponding number. The user will then be prompted to enter the number of the table they want to view. The main function will then call the open_table function, passing in the name of the selected table, which will return a dictionary containing the data from the selected table.

The main function will then use the tabulate function to print the contents of the table in a nicely formatted table. The user can then choose to perform one of several actions on the table, such as adding a card, moving a card, or viewing the history of the table. These actions are handled by additional functions, which are called by the main function based on the user's input.

### selecting Create Table

```py
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

```

The Create Table process allows the user to create a new table in the system. To create a table, the user must specify a name for the table and the number of columns they want the table to have. Once the user has provided this information, the system will create a new table with the specified number of columns, each with an empty header. The user can then add cards to the table and organize them within the columns as needed.

The Create Table process involves the following steps:

1. The user is presented with a prompt asking them how many columns they want to create in the table. The user inputs a number of columns, which must be greater than or equal to 1.

1. For each column, the user is asked to enter a name for the column.

1. Once all column names have been entered, the table is created and stored in a CSV file. The file is saved in a tables directory, with the name of the table being the name of the CSV file.

1. The user is then presented with the newly created table and is given the option to add, move, or delete cards within the table. The user can also view the history of the table, which includes a list of previous versions of the table.

1. Once the user is finished editing the table, they can return to the main menu and view or edit other tables, or they can exit the program.

