# ________________________________________________________________________________________________________
# Team Identification Block
# Author 1:     Mr. Kowshik Gunda
# Student ID:   *20473953
# E-Mail:       kgunda@uco.edu
# Author 2:     Ms. Satya Danthuluri
# Student ID:   *20474582
# E-Mail:       sdanthuluri@uco.edu
# Course:       CMSC 5023 . Programming Languages
# CRN:          22058, Spring, 2019
#Project:      p03
# Due:          April 24, 2019
# Project Account Number: tt084
# ________________________________________________________________________________________________________
# -------------------------------------------------------------------------

# ________________________________________________________________________________________________________

# openlist and closed list for bracket matching
# ________________________________________________________________________________________________________

open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]
# ________________________________________________________________________________________________________

# stack implementation
# ________________________________________________________________________________________________________


def balance(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return " is not balanced"
    if len(stack) == 0:
        return "is Balanced"
