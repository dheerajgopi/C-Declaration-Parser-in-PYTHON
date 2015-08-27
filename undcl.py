#!usr/bin/python
"""Function to convert description of declaration to its c declaration"""
import sys

#GLOBALS---------
tokentype = ""
token = ""
name = ""
datatype = []
out = ""
decl_buf = []
i = 0
of_type = ""
#------------------------------------------------------------------------#

def main():
    global token
    global name
    global datatype
    global out
    global decl_buf
    global of_type

    temp = ""

    decl_buf = list(raw_input("\nEnter declaration explanation: "))

    of_type = gettoken()

    while of_type != '\n':
        if of_type == "PARANTHESES" or of_type == "BRACKETS":
            out += token
        elif of_type == '*':
            temp = '(*' + out + ')'
            print temp
            out = temp
        elif of_type == "NAME":
            temp = token + out
            print temp
            out = temp
        else:
            print "invalid input"

        of_type = gettoken()

def gettoken():
    """Function to skip blanks and tabs, then finds the next token in the input; a ``token''
    is a name, a pair of parentheses, a pair of brackets perhaps including a number, or any other
    single character."""
    global token
    global tokentype
    global decl_buf
    global i
    global out
    global datatype

    len_decl = len(decl_buf)

    if (
        (i < len_decl and decl_buf[i] == '\t') or \
        (i < len_decl and decl_buf[i] == ' ')
    ):
        i += 1

    if i < len_decl and decl_buf[i] == '(':
        i += 1
        if decl_buf[i] == ')':
            token = ""
            token += "()"
            i += 1
            tokentype = "PARANTHESES"
            return tokentype
        else:
            tokentype = '('
            return tokentype

    elif i < len_decl and decl_buf[i] == '[':
        token = ""
        token += decl_buf[i]
        i += 1

        while i < len_decl and decl_buf[i] != ']':
            token += decl_buf[i]
            i += 1

        token += decl_buf[i]
        i += 1
        tokentype = "BRACKETS"
        return tokentype

    elif i < len_decl and decl_buf[i].isalpha():
        token = ""
        token += decl_buf[i]
        i += 1

        while i < len_decl and decl_buf[i].isalnum():
            token += decl_buf[i]
            i += 1

        tokentype = "NAME"
        return tokentype
    else :
        if i < len_decl:
            tokentype = decl_buf[i]
            i += 1
            return tokentype
        else:
            tokentype = '\n'
            return tokentype

if __name__ == "__main__":
    main()
