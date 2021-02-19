from model import decodedFileManaging

decodedExpressionPath = "decodedExpression.py"

#helpers

#clear() test
decodedFileManaging.clear()
f = open(decodedExpressionPath, "r")
assert (f.read() == "#EFFECTS: return the boolean output from var\n"
                            "def evaluate():\n"
                            "\t#Expression will show up here\n"
                            "\treturn \"test\"\n")
f.close()

#makeBlank() test
decodedFileManaging.makeBlank()
f = open(decodedExpressionPath, "r")
assert (f.read() == "")
f.close()

#override() test
decodedFileManaging.override("no you")
f = open(decodedExpressionPath, "r")
assert (f.read() == "no you")
f.close()

#append() test
decodedFileManaging.append("test string")
f = open(decodedExpressionPath, "r")
assert (f.read() == "no youtest string")
f.close()

#generatedDecodedFile() test
decodedFileManaging.generatedDecodedFile("(a + ((~a) |v t) <-> (~u)) |^ (~(a v b))")
f = open(decodedExpressionPath, "r")
str = "from model.data.booleanFn import Or\n" \
                          "from model.data.booleanFn import And\n" \
                          "from model.data.booleanFn import Nand\n" \
                          "from model.data.booleanFn import Nor\n" \
                          "from model.data.booleanFn import Xor\n" \
                          "from model.data.booleanFn import IfThen\n" \
                          "from model.data.booleanFn import Iff\n" \
"def evaluate(var):\n"\
"\ta = var[0]\n"\
"\tt = var[1]\n"\
"\tu = var[2]\n"\
"\tb = var[3]\n"\
"\treturn Nand(Xor(a,Iff(Nor(not a,t),not u)),not Or(a,b))"
str2 = f.read()
assert (str2 == str)
f.close()



#clean up the file
# decodedFileManaging.makeBlank()