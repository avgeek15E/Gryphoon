from pyparsing import alphas


def checkError(Exception):
    try:
        name = input("Enter your name")
        if(name is not alphas):
