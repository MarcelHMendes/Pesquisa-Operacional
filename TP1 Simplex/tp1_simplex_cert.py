import numpy as np
PRECISAO_IMPRESSAO = 5

def cert(qlinha,qcoluna):
	iden = np.zeros(qlinha-1,dtype = float) #gerando zeros do vetor C
	iden = np.vstack((iden,np.identity(qlinha-1,dtype = float))) #concatenando matriz identidade com os vetores de 0's
	cert = iden
	cert = cert.astype(float)
	return cert

def getCertificado(cert):
	return cert[0,:]