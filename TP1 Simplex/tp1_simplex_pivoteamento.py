import numpy as np
from fractions import Fraction
import tp1_simplex_cert as ct


def pivotP(matriz): 
	tamColuna = np.size(matriz[0,:]) #tamanho Coluna
	tamLinha = np.size(matriz[:,0]) #tamaho Linhas
	minC = 0
	indiceC = 0
	for k in range(0,tamColuna-1):
		if matriz[0,k] < minC:
			minC = matriz[0,k]
			indiceC = k
							
	numerador = matriz[:,tamColuna-1]
	denominador = matriz[:,indiceC]
	min = numerador[1]
	indice = 0
	for l in range(1,tamLinha): 
		if denominador[l] > 0:
			div = numerador[l]/denominador[l]	
			if div < min:
				min = div
				indice = l
	return (indice,indiceC) 

def verifIlim(matriz): #modulo que verifica se matriz é ilimitada
	verifVec = np.all(matriz <= 0, axis = 0)
	verifIlim = np.any(verifVec)
	
	return verifIlim
	
def verifInv(aux): #modulo que verifica se a matriz é inviavel
	aux = pivoteamento(aux)
	if getOtimo(aux) < 0:
		return True
	else:
		return False
	
def verifPrimal(matriz):	
	flag = False
	tamColuna = np.size(matriz[0,:])
	for i in range(0,tamColuna-1):
		if matriz[0,i] < 0:
			flag = True 
			break
	for j in range(1,np.size(matriz[:,0])):
		if matriz[j,tamColuna-1] < 0:
			flag = False
	return flag


def pivoteamento(matriz,lPivot,cPivot):	#matriz resultado e certificado
	linhas = np.size(matriz[:,0])

	multi = 1/Fraction(matriz[lPivot,cPivot])
	matriz[lPivot] = matriz[lPivot] * multi

	for i in range(0,linhas):
		if i != lPivot and matriz[i,cPivot] != 0:
			soma = matriz[lPivot]
			multi2 = matriz[i,cPivot]

			soma = soma * -1 * multi2

			matriz[i] = np.add(matriz[i], soma)

	return matriz

def simplexPrimal(matriz,arquivo):
	while verifPrimal(matriz) == True:
		(lPivot,cPivot) = pivotP(matriz)
		mat = pivoteamento(matriz,lPivot,cPivot)
		if verifIlim(mat) == True:
			mat[0,np.size(mat[0,:])-1] = float("inf")
			print('Status: ilimitada', file = arquivo)
			print('Certificado: ',file = arquivo)
			print('\n',file = arquivo)
			return (mat) 		
					
	return (mat) 

def getOtimo(matriz):
	tam = np.size(matriz[0,:])
	return matriz[0,tam-1]
def getResult(matriz):
	tamL = np.size(matriz[:,0])	#tamanho linha
	tamC = np.size(matriz[0,:])	#tamanho coluna
	result = matriz[:,tamC-1]
	result = np.delete(result,0)
	
	return result

