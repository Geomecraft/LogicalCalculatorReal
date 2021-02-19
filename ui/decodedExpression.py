from model.data.booleanFn import Or
from model.data.booleanFn import And
from model.data.booleanFn import Nand
from model.data.booleanFn import Nor
from model.data.booleanFn import Xor
from model.data.booleanFn import IfThen
from model.data.booleanFn import Iff
def evaluate(var):
	q = var[0]
	r = var[1]
	p = var[2]
	return Or(And(q,r),Or(Nor(p,q),And(not p,r)))