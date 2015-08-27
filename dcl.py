#!usr/bin/python
"""A simple recursive descent parser for explaining c declarations"""
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

    decl_buf = list(raw_input("\nEnter declaration: "))

    of_type = gettoken()

    if of_type == "NAME":
        datatype = token

    dcl()

    if tokentype != '\n':
        print "Syntax error!"

    print name, ":", out, datatype

def dcl():
    """Function to parse a declaration"""
    global out
    global of_type
    num_of_ptrs = 0

    of_type = gettoken()

    while of_type == '*':
        num_of_ptrs += 1
        of_type = gettoken()

    dirdcl()

    while num_of_ptrs > 0:
        out += " Pointer of"
        num_of_ptrs -= 1

def dirdcl():
    """Function to parse a direct declaration"""
    global out
    global token
    global of_type
    global tokentype
    global name
    global i

    if tokentype == '(':
        dcl()

        if tokentype != ')':
            print "Error: missing ')'\n"

    elif tokentype == "NAME":
        name += token

    else:
        print "Error: expected name or (dcl)\n"

    of_type = gettoken()

    while (
        of_type == "PARANTHESES" or \
        of_type == "BRACKETS"
    ):
        if of_type == "PARANTHESES":
            out += " function returning"
        else:
            out += " array"
            out += token
            out += " of"

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
