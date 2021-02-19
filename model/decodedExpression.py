from model.data.booleanFn import Or
from model.data.booleanFn import And
from model.data.booleanFn import Nand
from model.data.booleanFn import Nor
from model.data.booleanFn import Xor
from model.data.booleanFn import IfThen
from model.data.booleanFn import Iff
def evaluate(var):
	a = var[0]
	t = var[1]
	u = var[2]
	b = var[3]
	return Nand(Xor(a,Iff(Nor(not a,t),not u)),not Or(a,b))