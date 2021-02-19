from model.data.logicSymbols import logicSymbolList, OperatorMapping
from model.generateTruthTable import printTruthTable

while True:
    expression = input("You can enter a valid logical expression here for it to be evaluated\n"
          "Precedance MUST be forced or you may get unexpected output\n"
          "You can use /help for a list of accepted symbols\n")
    if expression == "/help":
        print("Not is represented as ~")
        for x in logicSymbolList:
            print(OperatorMapping[x][:-1] + " is represented as " + x)
        print("")
    else:
        printTruthTable(expression)