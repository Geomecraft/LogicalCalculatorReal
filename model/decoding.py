
#Constants:
#ALPHABETS is a list of alphabets of both upper and lower case excluding v and V
from model.data.logicSymbols import logicSymbolList, OperatorMapping

ALPHABETS = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
a2 = []
for x in ALPHABETS:
    a2.append(x.upper())
ALPHABETS.extend(a2)



#Data Definition:
# expression is one-of:
# - unary expression
# - binary expression
# interp. an abstract logical expression
# example:
expression1 = "(a ^ b)"
expression2 = "(a ^ b) v c"

# unary expression is one-of:
# - var
# - a string "~" + expression
# - a string "(" + expression + ")"
# intrep. a logical expression that is not immediatly operatable with a binary operator
# example:
unaryExpression1 = "a"
unaryExpression2 = "~(a ^ b)"
unaryExpression3 = "(a ^ b)"
#helpful functions for this data:

#SIGNATURE (string -> boolean)
#EFFECTS return if input string is a unary expression or not
def isUnaryExpression(str):
    def isBigBracket(str):
        if str[0] != "(":
            return False
        else:
            openCount = 1
            closeCount = 0
            for i in range(1,len(str)):
                if str[i] == "(":
                    openCount += 1
                elif str[i] == ")":
                    closeCount += 1

                if openCount == closeCount:
                    return (i == (len(str) -1))
            return False

    return (isVar(str) or (str[0] == "~") or (isBigBracket(str)))

# binary expression is:
# a string unary expression + binary operator + unary expression
# intrep. a logical expression that is immediatly operatable with a binary operator
# example:
binaryExpression1 = "(a ^ b) v c"
binaryExpression2 = "a ^ b"
#helpful functions for this data:

#SIGNATURE (binary expression -> listof string)
#EFFECTS return the disasembled list version of the binary expression, like [unary expression, binary operator, unary expression]
def split(str):
    lst = str.split(" ")
    index = 0
    openCount = 0
    closeCount = 0
    for i in range(0, len(lst)):
        openCount += lst[i].count("(")
        closeCount += lst[i].count(")")

        if (openCount == closeCount) and (lst[i] in logicSymbolList):
            index = i
            break

    firstexp = ""
    for i in range(0, index):
        firstexp += lst[i]
        firstexp += " "
    firstexp = firstexp[:-1]

    secondexp = ""
    for i in range(index + 1, len(lst)):
        secondexp += lst[i]
        secondexp += " "
    secondexp = secondexp[:-1]

    return [firstexp, lst[index], secondexp]

# var is:
# a single alphabetical character that is not "v" or "V"
# intrep. a logical variable
# example is redundant for enumeration
# helpful functions for this data:

#SIGNATURE (string -> boolean)
#EFFECTS: see if the given stirng is a var
def isVar(str):
    return (str in ALPHABETS)

# binary operator is:
# a multi-character string that is in the logicSymbolList in logicSymbols.py
# intrep. a logical binary operator
# example is redundant for enumeration
# helpful functions for this data:

#SIGNATURE (string -> boolean)
#EFFECTS: see if the given stirng is a binary operator
def isBinaryOperator(str):
    return (str in logicSymbolList)



#-----------Actual Functions------------#
#SIGNATURE (expression -> var)
#EFFECTS: return a list of var that is used in this expression,
# the order in the list is same as order of first apperance in the expression, no duplicates
def generateVar(expression):
    vars = []
    for x in expression:
        if isVar(x) and (x not in vars):
            vars.append(x)
    return vars

#SIGNATURE (expression -> string)
#EFFECTS: return a string representing a logically equivalent python expression to input expression, using functions from booleanFn
def generatePythonExpression(expression):
    def fn_for_una(una):
        if isVar(una):
            return una
        elif (una[0] == "~"):
            return "not " + generatePythonExpression(una[1:])
        else:
            return generatePythonExpression(una[1:-1])
    def fn_for_bin(bin):
        splittedBin = split(bin)
        return OperatorMapping[splittedBin[1]] + \
               generatePythonExpression(splittedBin[0]) + "," \
               + generatePythonExpression(splittedBin[2]) + ")"
    if (isUnaryExpression(expression)):
        return fn_for_una(expression)
    else:
        return fn_for_bin(expression)








