def nand2(a,b):
    return mux41(1,1,1,0)(a,b)

def mux41(i0,i1,i2,i3):
    return lambda s1,s0:{(0,0):i0,(0,1):i1,(1,0):i2,(1,1):i3}[(s1,s0)]

def nor2(a, b):
    return {(0,0):1,
        (0,1):0,
        (1,0):0,
        (1,1):0}[(a,b)]

def mux21b(s, i1, i0):
    # Your code for mux21b that invokes nor2 (and nothing else).
    # We will work this out in class today.
    #
    # !s.i0 + s.i1 = !((s+!i0) . (!s+!i1)) = !(s+!i0)+!(!s+!i1)
    #
    # p = !(s+!i0) q = !(!s+!i1)
    #
    ni0 = nor2(i0,i0)
    ns = nor2(s,s)
    ni1 = nor2(i1,i1)
    p = nor2(s,ni0)
    q = nor2(ns, ni1)
    nrslt = nor2(p,q)
    return nor2(nrslt, nrslt)
# We will draw the above circuit in TkGate and simulate

def test_mux21c_eq_mux21b():
    testTriples = cart3(set({0,1}), set({0,1}), set({0,1}))
    testResults = map(lambda (s, i1, i0): mux21c(s, i1, i0) == mux21b(s, i1, i0), testTriples)
    bigAnd = reduce(lambda a, b: a and b, testResults)
    if bigAnd:
        print("Testing succeeded. mux21c and mux21b are the same function.")
    else:
        print("Testing FAILED. mux21c and mux21b are NOT the same function.")

def cart3(A, B, C):
    return {(a,b,c) for a in A for b in B for c in C}

def mux21c(s, i1, i0):
    p = nand2 (nand2(s,s), i0)
    q = nand2(s, i1)
    return nand2 (p,q)


if __name__ == '__main__':
    test_mux21c_eq_mux21b()
    
