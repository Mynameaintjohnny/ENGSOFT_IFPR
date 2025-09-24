
def bolha (vetor):
    aux = None

    
    for i in range (0,len(vetor)-1):

        for y in range(0,len(vetor)-1):
            if(vetor[y] > vetor[y+1]):
                aux = vetor[y]
                vetor[y] = vetor[y+1]
                vetor[y+1] = aux
    

    return vetor

def insercao (vetor):

    for i in range(1,len(vetor)):
        aux = vetor[i]
        j = i - 1

        while (j >= 0) and (vetor[j] > aux):
            vetor[j+1] = vetor[j]
            j = j - 1
        
        vetor[j+1] = aux
    
    return vetor


def selecao (vetor):
    menor = None
    aux = None
    for i in range(0,len(vetor)-1):
        menor = vetor[i]
        i_menor = i

        for y in range(i+1,len(vetor)):
            
            if(menor > vetor[y]):
                menor = vetor[y]
                i_menor = y

        aux = vetor[i]
        vetor[i] = vetor[i_menor]
        vetor[i_menor] = aux
    
    return vetor

