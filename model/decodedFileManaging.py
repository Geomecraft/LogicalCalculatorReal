from model.data.logicSymbols import logicSymbolImportString
from model.decoding import generatePythonExpression, generateVar

decodedExpressionPath = "decodedExpression.py"

#SIGNATURE (void -> void)
#EFFECTS: clear the decodedExpression file, only leaving a stub behind
def clear():
    decodedExpression = open(decodedExpressionPath,"w")
    decodedExpression.write("#EFFECTS: return the boolean output from var\n"
                            "def evaluate():\n"
                            "\t#Expression will show up here\n"
                            "\treturn \"test\"\n")
    decodedExpression.close()

#SIGNATURE (void -> void)
#EFFECTS: make the decodedExpression file blank
def makeBlank():
    f = open(decodedExpressionPath, "w")
    f.write("")
    f.close()

#SIGNATURE (string -> void)
#EFFECTS: write the given string into decodedExpression file
def override(str):
    f = open(decodedExpressionPath, 'w')
    f.write(str)
    f.close()

#SIGNATURE (string -> void)
#EFFECTS: append given string into decodedExpression file
def append(str):
    f = open(decodedExpressionPath, 'a')
    f.write(str)
    f.close()

#SIGNATURE (expression -> void)
#EFFECTS: generate a logical equivalent python expression and write it in decodedExpression.py
def generatedDecodedFile(expression):
    exp = logicSymbolImportString + "def evaluate(var):\n"
    var = generateVar(expression)
    # the variables
    for i in range(0, len(var)):
        exp += "\t" + var[i] + " = var[" + str(i) + "]\n"

    exp += "\treturn " + generatePythonExpression(expression)
    override(exp)