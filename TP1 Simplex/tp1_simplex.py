# -*- coding: utf-8 -*-
import numpy as np
import tp1_simplex_io as io
import tp1_simplex_cert as ct
import tp1_simplex_pivoteamento as pv
import tp1_simplex_aux as ax
import sys

PRECISAO_IMPRESSAO = 2
#!!!!!!antes de rodar simplex sempre testar se PL é inviável ou ilimitada!!!!!

#introzir certificados no pivotemento e plAux
	
def configura_impressao_float():
    # Configura como os dados do tipo float em arrays numpy serao
    #   impressos.
    np.set_printoptions(precision=PRECISAO_IMPRESSAO,floatmode ='fixed')
    
def FPI(matriz): #Ajusta a matriz para FPI(testar função depois que finção de I/O tiver pronta)
	linhas = np.size(matriz[:,0])
	colunas = np.size(matriz[0,:])
	iden = np.zeros(linhas-1,dtype = int) #gerando zeros do vetor C
	iden = np.vstack((iden,np.identity(linhas-1,dtype = int))) #concatenando matriz identidade com os vetores de 0's  (VERIFICAR SE É PASSADO O VALOR CORRETO *qlinha-1)
	matriz = np.concatenate((matriz,iden),axis = 1)#concatendando matriz de folga a matriz original	
	switch = matriz[:,colunas-1] #copia coluna b da matriz
	matriz = np.delete(matriz,colunas-1,1) #retira coluna b da matriz
	matriz = np.concatenate((matriz,switch),axis = 1) #retorna coluna b ao final da matriz
	return matriz

	
def ajustaVecC(matriz): #será passado a matriz já em FPI,funcao que ajusta o vetor C para -C
	matriz[0,:] = matriz[0,:] * -1
	return matriz
	
		
def plAux(aux):#funcao que fornece PL auxiliar
	linhas = np.size(aux[:,0])
	colunas = np.size(aux[0,:])
	iden = np.ones(linhas-1,dtype = float)
	iden = np.vstack((iden,np.identity(linhas-1,dtype = float)))
	#iden = ajustaVecC(iden)
	aux[0,:] = aux[0,:] * 0
	aux = np.concatenate((aux,iden), axis = 1)
	switch = aux[:,colunas-1] #copia coluna b da matriz
	aux = np.delete(aux,colunas-1,1) #retira coluna b da matriz
	aux = np.concatenate((aux,switch),axis = 1) #retorna coluna b ao final da matriz

	tam = np.size(aux[0,:])
	for i in range(1,linhas):
		if aux[i,tam-1] < 0:
			aux[i] = aux[i] * -1
													
	return aux

def concatenaAux_Original(aux,original):
	custos = np.asarray(original[0,:])
	colAux = np.size(aux[0,:])
	colOrigin = np.size(original[0,:])
	delCol = colAux - colOrigin
	tableau = np.delete(aux,0,0)

	for i in range(1,delCol+1):		#gambiarra
		tableau = np.delete(tableau,colAux-i-1,1)	#gambiarra

	tableau = np.concatenate((custos,tableau),axis = 0)	
	return tableau	

	
def main():

	if (len(sys.argv) != 3):
		print("[Erro]: Numero incorreto de parametros.")
		print("Uso: python", sys.argv[0], "<entrada> <saida>")
		return

	nome_entrada = sys.argv[1]
	nome_saida = sys.argv[2]
	
	ref_arquivo = open(nome_entrada,'r')
	arquivo = ref_arquivo.readlines()
	ref_arquivo.close()
	
	ref_arquivo_saida = open(nome_saida,'w')
		
	(matriz,qlinha,qcoluna) = io.leitura(arquivo)
	
	#-------------------------------------
	
	#Ajustando matriz para tableau
	matriz = FPI(matriz) 
	matriz = ajustaVecC(matriz)        
	#-------------------------------------
	#Matriz,passar copia da matriz original

	aux = matriz.copy() 
	aux = plAux(aux)

	#-------------------------------------
	'''Resolvendo Plaux, verificando a viabilidade da PL e achando uma base viável caso precise '''

	auxiliar = ax.pivoteamentoAux(aux)
	auxiliar = pv.simplexPrimal(auxiliar,ref_arquivo_saida)
	
	
	if pv.getOtimo(auxiliar) < 0:
		print('Status: Inviável',file = ref_arquivo_saida)
		print('Certificado: ',file = ref_arquivo_saida)
		print('\n',file = ref_arquivo_saida)
		return 
	elif pv.getOtimo(auxiliar) == 0:		
		resp = pv.simplexPrimal(matriz,ref_arquivo_saida)
		print('Objetivo: ',file = ref_arquivo_saida)
		print(pv.getOtimo(resp),file= ref_arquivo_saida)
		print('Solução: ',file = ref_arquivo_saida)
		print(pv.getResult(matriz),file = ref_arquivo_saida)
		print('Cerificado: ',file = ref_arquivo_saida)
		print('\n', file = ref_arquivo_saida)

			

			
	'''print(matriz)
	print('\n')
	print(aux)
	auxiliar = ax.pivoteamentoAux(aux)
	print(auxiliar)
	print('\n')
	teste = pv.simplexPrimal(auxiliar)
	print(teste)
	print('\n')

	principal = pv.simplexPrimal(matriz)
	print(principal)	
	'''
	#-------------------------------------
	
configura_impressao_float()	
main()