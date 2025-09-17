
# #Método de referencia
# def bolha(vetor):
#     aux = None
#     for i in range(0,len(vetor)-1):

#         for g in range(0, len(vetor)-1):

#             if(vetor[g] > vetor[g+1]):
#                 aux = vetor[g]
#                 vetor[g] = vetor[g+1]
#                 vetor[g+1] = aux
        
        
vet = [10,9,8,7,6,7,8]
# print(vet)
# bolha(vet)
# print(vet)

#Método de inserção

# def insert(vetor):
#     for i in range(1,len(vetor)):
#         temp = vetor[i] # armazena o valor 
#         j = i - 1 # guarda o i anterior

#         while(j >= 0 and temp < vetor[j]):
#             vetor[j+1] = vetor[j]
#             j -= 1
#         vetor[j+1] = temp        

# print(vet)
# insert(vet)
# print(vet)


#Método de Seleção

def selecao(vetor):
    for i in range(0,len(vetor) -1):
        menor = vetor[i]
        imenor = i

        for j in range(i+1,len(vetor)):
            if(vetor[j] < menor):
                menor = vetor[j]
                imenor = j

        vetor[imenor] = vetor[i]
        vetor[i] = menor
        print(vetor)

print(vet)
selecao(vet)
