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