import random
def make_password(how_many_chars : int = 4,bid_chars : int = 0,num_chars : int = 0):
    bc = bid_chars
    nc = num_chars
    pasword_len = 0
    pasword_list = []
    nums = ("0","1","2","3","4","5","6","7","8","9")
    chars = (
         "a",
         "b",
         "c",
         "d",
         "e",
         "f",
         "g",
         "h",
         "i",
         "g",
         "k",
         "l",
         "m",
         "n",
         "o",
         "p",
         "q",
         "r",
         "s",
         "y",
         "u",
         "x"
         "j"
    )
    chars_big = (
         "A",
         "B",
         "C",
         "D",
         "E",
         "F",
         "G",
         "H",
         "I",
         "G",
         "K",
         "L",
         "M",
         "N",
         "O",
         "P",
         "Q",
         "R",
         "S",
         "Y",
         "U",
         "X"
         "J"
    )
    pasword = ""
    while pasword_len <= how_many_chars:
        what_to_do = random.randint(0,4)
        if (what_to_do == 1 and nc > 0):
            _pasword = nums[random.randint(0,nums.__len__()) - 1]
            pasword += _pasword
            pasword_list.append(_pasword)
            nc -= 1
            pasword_len += 1
        elif (what_to_do == 2 and bc > 0):
            _pasword = chars_big[random.randint(0,chars_big.__len__()) - 1]
            pasword += _pasword
            pasword_list.append(_pasword)
            bc -= 1
            pasword_len += 1
        elif (what_to_do == 3):
            _pasword = chars[random.randint(0,chars.__len__()) - 1]
            pasword += _pasword
            pasword_list.append(_pasword)
            pasword_len += 1
    return pasword
