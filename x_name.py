import string
import keyword
from tkinter.font import names


def is_valid_variable_name(x_name):
    if not x_name:
        return False
    if x_name[0].isdigit():
        return False
    if any(c.isupper() for c in x_name):
        return False
    wrong_symbols = string.punctuation.replace("_", "")
    if any(c in wrong_symbols or c.isspace() for c in x_name):
        return False
    if x_name in keyword.kwlist:
        return False
    if x_name.count("_") > 1:
        return False
    return True
priklady = [
    "_", "__", "___", "a", "al_lex", "al lex", "al@lex",
    "a_l_ex", "Al_lex", "a_Lex", "aLex",
    "18a", "a18", "alex", "al_lexM"
]

for name in priklady:
    print(f"{name}: {is_valid_variable_name(name)}")
pass