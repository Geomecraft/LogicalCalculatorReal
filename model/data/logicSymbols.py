#INVARIANT:symbols in logicSymbolList are and are the only keys in OperatorMapping,
# with corresponding value being a function that exists in booleanFN.py and is being
# imported in logicSymbolImportString

logicSymbolList = ["^","v","|^","|v","->","<->","+"]

OperatorMapping = {"v":"Or(",
                                "^":"And(",
                                "|^":"Nand(",
                                "|v":"Nor(",
                                "->":"IfThen(",
                                "<->":"Iff(",
                                "+":"Xor("}

logicSymbolImportString = "from model.data.booleanFn import Or\n" \
                          "from model.data.booleanFn import And\n" \
                          "from model.data.booleanFn import Nand\n" \
                          "from model.data.booleanFn import Nor\n" \
                          "from model.data.booleanFn import Xor\n" \
                          "from model.data.booleanFn import IfThen\n" \
                          "from model.data.booleanFn import Iff\n"