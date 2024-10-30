#!/usr/bin/python3

mystr = "10101"

def strtoint(mystr):
    for x in mystr:
        if x not in "01":
            return "Error.String with non-binary characters"
    num = int(mystr, 2)
    return num

print(f"binary: {mystr} integer: {strtoint(mystr)}")
    