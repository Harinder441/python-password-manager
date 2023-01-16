# IMPROVMents
## choose list com[prehension
##  use of shuffle in random
## use join method
## randomise no. of letters ..

import random as rd

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
LETTERS_COUNT = 8
SYMBOLS_COUNT = 4
NUMBERS_COUNT = 4


def pass_generator(lc=LETTERS_COUNT, sc=SYMBOLS_COUNT, nc=NUMBERS_COUNT):
    password = ""
    total = lc + sc + nc
    index = [0, 1, 2]
    for i in range(0, total):

        rd_index = rd.choice(index)
        if rd_index == 1:
            ris = rd.randint(0, len(symbols) - 1)
            password = password + symbols[ris]
            sc -= 1
            if sc <= 0:
                index.remove(1)

        elif rd_index == 2:
            ris = rd.randint(0, len(numbers) - 1)
            password = password + numbers[ris]
            nc -= 1
            if nc <= 0:
                index.remove(2)
        else:
            ris = rd.randint(0, len(letters) - 1)
            password = password + letters[ris]
            lc -= 1
            if lc <= 0:
                index.remove(0)

    return password


if __name__ == "__main__":
    print(pass_generator())
    # import json
    # with open("passwords.json", mode="r") as file:
    #     data=json.load(file)

