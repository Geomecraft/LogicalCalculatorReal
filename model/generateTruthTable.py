
import importlib
from model.decodedFileManaging import generatedDecodedFile
from model.decoding import generateVar
from ui import decodedExpression

def generateBooleanCombinations(NumofVar):
    return generateBooleanCombinationsHelper(NumofVar,[[]])
def generateBooleanCombinationsHelper(NumofVar,rsf):
    if (NumofVar == 0):
        return rsf
    else:
        NumofVar -= 1
        #Merge the list with an exact same list
        rsf = rsf + rsf.copy()
        #append T in each sublist in the first half at front
        for i in range(0,len(rsf) // 2):
            rsf[i] = [False] + rsf[i]
        #append F in each sublist in the later half
        for i in range(len(rsf) // 2,len(rsf)):
            rsf[i] = [True] + rsf[i]
        return generateBooleanCombinationsHelper(NumofVar,rsf)

#SIGNATURE ((listof String) -> String)
def printRow(lst):
    for i in range(0,len(lst)-1):
        print("{0:^9}".format(lst[i]),end='')
    print("{0:^40}".format(lst[-1]))

#SIGNATURE (expression -> String)
def printTruthTable(expression):
    var = generateVar(expression)
    valueIterations = generateBooleanCombinations(len(var))

    #printing the first row
    varList = var
    varList.append(expression)
    printRow(varList)

    #printing the rest of the row
    def generateResult(expression):
        generatedDecodedFile(expression)
        importlib.reload(decodedExpression)
        from ui.decodedExpression import evaluate

        result = []
        for x in valueIterations:
            result.append(evaluate(x))
        return result
    result = generateResult(expression)
    for i in range(0,len(result)):
        # print(valueIterations[i] + [result[i]])
        printRow(valueIterations[i] + [result[i]])