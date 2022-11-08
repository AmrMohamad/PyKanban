from tabulate import tabulate
from colored import fg, bg, attr,stylize
import csv

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



def get_headers (*headers : list[str],fore_color:str = '#ffffff',back_color:str = '#000000') -> list:
    """ Asking for column names"""
    if bool(headers) == False:
        print("Add one space between each column name")
        headers: str = input("Names of each column: ")
    """ add colors to header"""
    header_names = [str(name) for name in headers.split(" ")]
    while True:
        q_add = input("Would like add colors to header?(Y/N)  ").lower()
        if q_add in ["y","yes"]:
            print("Please Enter the values in HEX like this '#000000'")
            for index,h_name in enumerate(header_names):
                while True:
                    fore_color = input("Foreground color of Text:")
                    if len(fore_color) != 7 and fore_color[0] != "#" :
                        print("Please Enter a Right Value !!")
                        continue
                    else:
                        color = fg(fore_color)
                        break
                while True:
                    back_color = input("Background color of Text:")
                    if len(back_color) != 7 and back_color[0] != "#" :
                        print("Please Enter a Right Value !!")
                        continue
                    else:
                        color += bg(back_color)
                        break
                header_names[index] = color + " " + h_name + " " + attr('reset')
            break
        elif q_add in ["n","no"]:
            break
        else:
            print("Please Enter a Right Value !!")
            continue

    return [header_names]

def main():

    #card = Card()

    #title_of_card = input("Title: ")
    #discription_of_card = input("Discription: ")

    table = get_headers()

    print(
        tabulate(table, tablefmt="double_grid", stralign="center", colalign=("center",))
    )



if __name__ == "__main__":
    main()

