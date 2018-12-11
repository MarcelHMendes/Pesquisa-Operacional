import tp1_simplex_pivoteamento as pv 
import numpy as np
def pivoteamentoAux(aux):
	linhas = np.size(aux[:,0])	
	for i in range(1,linhas):	#colocando matriz plAux na forma canonica 
		aux[0] = aux[0] + (aux[i] * -1)
	return (aux)

def simplexAux(aux):
	(mat) = pv.simplexPrimal(aux)	
	return (mat)

