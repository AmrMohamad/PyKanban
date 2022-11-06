from tabulate import tabulate

class Card :
    def __init__(self, width_of_card) -> None:
        self.width_of_card = width_of_card

def card(*sentences) -> str:
    width_of_card: int = 38
    blank_line: str = "| " + (" " * (width_of_card + 2)) + "#" + "\n"
    top_line: str = " " + ("#" * (width_of_card + 2)) + "#" + "\n"
    text_line: str = ""
    for sentence in sentences:
        lines_per_sentence = [""]
        num_of_sentence_chars = len(sentence)
        index_line = 0
        start_line = 0
        end_line = 32
        if 0 < num_of_sentence_chars <= 192:
            num_of_lines = int(round(num_of_sentence_chars / 32))
            while index_line in range(num_of_lines):
                lines_per_sentence[index_line] = sentence[start_line:end_line]
                lines_per_sentence.append("")
                start_line = end_line
                end_line += 32
                index_line += 1
        else:
            raise ValueError("maximum number of characters is 192")
        for i in range(len(lines_per_sentence) - 1):
            text_line += (
                "| "
                + (
                    lines_per_sentence[i]
                    + " " * (width_of_card - len(lines_per_sentence[i]))
                )
                + "  #"
                + "\n"
            )
    buttom_line: str = " " + ("-" * (width_of_card + 2))
    return f"{top_line}{blank_line}{text_line}{blank_line}{buttom_line}"



title_of_card = input("Title: ")
discription_of_card = input("Discription: ")

table = [
    ["c1","c2","c3"],
    [card(title_of_card,discription_of_card),card(title_of_card,discription_of_card),card(title_of_card,discription_of_card)],
    [card(title_of_card,discription_of_card),card(title_of_card,discription_of_card),card(title_of_card,discription_of_card)]
]
print(tabulate(table, tablefmt="double_grid", stralign="center", colalign=("center",)))

