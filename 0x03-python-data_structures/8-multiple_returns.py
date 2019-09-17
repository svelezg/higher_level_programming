#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if lenght == 0:
        First = "None"
    else:
        First = sentence[:1]

    return lenght, First
