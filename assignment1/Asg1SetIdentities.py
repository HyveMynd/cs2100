A = { i for i in range(2,17) if (i%2 == 0) }
B = { i for i in range(2,17) if (i%2 == 1) }
C = { i for i in range(2,17) if ((i%3 == 0) | (i%4 == 0)) }
Comp = { i for i in range(2,17) }


ids = ["Identity (A | (B & C)) == (A | B) & (A | C) ",
       "Identity (A & (B | C)) == (A & B) | (A & C) ",
       "Identity (A | B) == Comp-(A-Comp & B-Comp) ",
       "Identity (A & B) == (A-Comp | B-Comp)-Comp ",
       "Identity A - (B | C) == (A - B) & (A - C) ",
       "Identity A | (B - C) == (A | B) - C ",
       "Identity (A | B) - B == A ",
       "Identity (A - B) | (B - A) == (A | B) - (B & A) "
       ]
       
bools = [((A | (B & C)) == (A | B) & (A | C)),
         (A & (B | C)) == (A & B) | (A & C),
         (A | B) == Comp-(A-Comp & B-Comp),
         (A & B) == (A-Comp | B-Comp)-Comp,
         A - (B | C) == (A - B) & (A - C),
         A | (B - C) == (A | B) - C,
         (A | B) - B == A,
         (A - B) | (B - A) == (A | B) - (B & A)
         ]

def printResult (identity, result):
    print identity,
    if (result):
        print "was found true for the given sets.\n"
    else:
        print "was found violated for the given sets.\n"

if __name__ == '__main__':
    for  i ,j in zip(ids,bools):
        printResult(i,j)
