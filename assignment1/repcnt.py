#! /usr/bin/env python
import rep
import pprint
pp = pprint.PrettyPrinter(indent=4)

# A function to return the number of '[' in a given 'n' 'set of sets'
def repcnt (n):
    """
    Return the number of open brackets '[' in the 'set of sets given by 'n'
    """
    output = str(rep.rep(n))
    return output.count("[")


if __name__ == '__main__': #block, include the test    
    for i in range(8):
        pp.pprint(("Number of [ in " + str(i) + " is: ", repcnt(i)))

    help (repcnt)
