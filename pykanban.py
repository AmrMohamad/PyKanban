from tabulate import tabulate


def card(*sentences) -> str:
    width_of_card :int = 0
    for i in range(len(sentences) - 1) : 
        """Determine the width of card 
           denpends on longest sentence
           in sentences
        """
        if len(sentences[i+1]) > len(sentences[i]):
            width_of_card = len(sentences[i+1])
        else :
            width_of_card = len(sentences[i])
    card : str = ""
    blank_line : str = "| " + (" " * (width_of_card + 2)) + "#" +"\n"
    top_line : str = " " + ("#" * (width_of_card + 2)) + "#" + "\n"
    card = card + top_line + blank_line
    text_line : str = ""
    for sentence in sentences:
        text_line += "| " + (sentence + " " * (width_of_card - len(sentence))) + "  #" + "\n"
    card = card + text_line
    buttom_line : str = " " + ("-" * (width_of_card + 2))
    card = card + blank_line + buttom_line
        
    return card

title_of_card = input("Title: ")
discription_of_card = input("Discription: ")

print(card(title_of_card,discription_of_card))
print("\n")

table = [
    ["c1","c2","c3"],
    [card(title_of_card,discription_of_card),card(title_of_card,discription_of_card),card(title_of_card,discription_of_card)],
    [card(title_of_card,discription_of_card),card(title_of_card,discription_of_card),card(title_of_card,discription_of_card)]
]
print(tabulate(table, tablefmt="double_grid", stralign="center", colalign=("center",)))