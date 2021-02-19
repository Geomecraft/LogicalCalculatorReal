def Or(a,b):
    return (a or b)

def And(a,b):
    return (a and b)

def Nand(a,b):
    return not (a and b)

def Nor(a,b):
    return not (a or b)

def Xor(a,b):
    return (a and not b) or (not a and b)

def IfThen(a,b):
    return (not a) or b

def Iff(a,b):
    return (IfThen(a,b) and IfThen(b,a))