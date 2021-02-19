from model.generateTruthTable import generateBooleanCombinations

#generateBooleanCombinations() test
assert (generateBooleanCombinations(0) == [[]])
assert (generateBooleanCombinations(1) == [[False],[True]])
assert (generateBooleanCombinations(2) == [[False,False],[False,True],[True,False],[True,True]])
assert (generateBooleanCombinations(3) == [[False,False,False],[False,False,True],[False,True,False],[False,True,True],
                                           [True,False,False],[True,False,True],[True,True,False],[True,True,True]])

#print functions does not need testing as it is trivial and always subject to change
#The final print function is not testable due to file limitations