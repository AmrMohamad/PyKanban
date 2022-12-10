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
