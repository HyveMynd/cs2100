#! /usr/bin/env python
import pprint
pp = pprint.PrettyPrinter(indent=4)


# This function will return the 'set of sets' representation up to the number 'n' #
def rep (n):
    """
    Returns the 'set of sets' for the given number 'n'
    """
    output = ""
    if n==0:
        return output + "[]"
    return [rep(r) for r in range(n)]

if __name__ == '__main__':
    for i in range(8):
        print("Rep of " + str(i) + " is: "), # print and suppress newline with ","
        pp.pprint(rep(i)) # continue and print on the same line
    help(rep)
