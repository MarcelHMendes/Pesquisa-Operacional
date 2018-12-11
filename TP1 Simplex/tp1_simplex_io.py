import numpy as np

def leitura(arquivo):
	qlinha = int(arquivo[0].strip("\n"))
	qcoluna = int(arquivo[1].strip("\n"))
	qlinha = qlinha + 1
	qcoluna = qcoluna + 1 
	
	matriz = np.matrix(arquivo[2], dtype = float)
	matriz = np.reshape(matriz,(qlinha,qcoluna))
	return (matriz,qlinha,qcoluna)
	