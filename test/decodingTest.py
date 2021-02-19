from model.decoding import generateVar, isVar, isBinaryOperator, isUnaryExpression, split, generatePythonExpression

#generateVar() test
assert(generateVar("a") == ["a"])
assert(generateVar("v") == [])
assert(generateVar("a ^ b") == ["a","b"])
assert(generateVar("a v b") == ["a","b"])
assert(generateVar("q |v ((a v b) ^ (q + p))") == ["q","a","b","p"])
assert(generateVar("q ^ (q |v ((A v b) ^ (q + a)))") == ["q","A","b", "a"])

#isVar() test
assert(isVar("a"))
assert(isVar("A"))
assert(isVar("O"))
assert(not isVar("v"))
assert(not isVar("V"))
assert(not isVar("&"))
assert(not isVar("-"))

#isBinaryOperator() test
assert(isBinaryOperator("^"))
assert(isBinaryOperator("v"))
assert(not isBinaryOperator("<-"))
assert(isBinaryOperator("<->"))
assert(isBinaryOperator("|v"))

#isUnaryExpression() test
assert(not isUnaryExpression("a ^ b"))
assert(isUnaryExpression("a"))
assert(isUnaryExpression("~a"))
assert(isUnaryExpression("~(a ^ b)"))
assert(isUnaryExpression("(a ^ b)"))
assert(not isUnaryExpression("(a ^ b) v (c ^ d)"))
assert(isUnaryExpression("((a ^ b) v (c ^ d))"))

#split test
assert(split("a ^ b") == ["a", "^", "b"])
assert(split("a ^ ~b") == ["a", "^", "~b"])
assert(split("(~a) ^ (~b)") == ["(~a)", "^", "(~b)"])
assert(split("(a ^ b) v (p + q)") == ["(a ^ b)", "v", "(p + q)"])
assert(split("(u ^ (a ^ b)) v p") == ["(u ^ (a ^ b))", "v", "p"])
assert(split("(u ^ (a ^ b)) <-> ((u ^ a) ^ b)") == ["(u ^ (a ^ b))", "<->", "((u ^ a) ^ b)"])

#generatePythonExpression() test
assert(generatePythonExpression("a") == "a")
assert(generatePythonExpression("~a") == "not a")
assert(generatePythonExpression("a ^ b") == "And(a,b)")
assert(generatePythonExpression("(a ^ b)") == "And(a,b)")
assert(generatePythonExpression("~(a ^ b)") == "not And(a,b)")
assert(generatePythonExpression("~((~a) ^ b)") == "not And(not a,b)")
assert(generatePythonExpression("~((~a) ^ (~b))") == "not And(not a,not b)")
assert(generatePythonExpression("p -> (a v b)") == "IfThen(p,Or(a,b))")
assert(generatePythonExpression("(a + b) <-> (~(a v b))") == "Iff(Xor(a,b),not Or(a,b))")
assert(generatePythonExpression("(a + ((~a) |v t) <-> (~u)) |^ (~(a v b))") == "Nand(Xor(a,Iff(Nor(not a,t),not u)),not Or(a,b))")