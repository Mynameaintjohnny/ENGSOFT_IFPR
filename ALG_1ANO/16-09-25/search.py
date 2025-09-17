
vet = [15,10,3,12,5,7,1]
ordvet = [1,3,5,7,10,12,15]

valor = int(input("Informe um numero: "))
teste = False
pos = None
for i in range(0,len(vet)):
    if(valor == vet[i]):
        teste == True
        pos = i
        break


if(teste == True):
    print(f"O valor informado {valor} existe no vetor na posição {pos}")
else:
    print(f"O valor informado {valor} não existe no vetor")


# Versão 2 para vetores ordenados:






# Busca Binária

inicio = 0
fim = len(vet)-1
pos = None

while(inicio <= fim):
    meio = int((inicio+fim)/2)

    if(vet[meio] == valor):
        teste == True
        pos = meio
        break

    elif(vet[meio] > valor):
        fim = meio - 1

    else:
        inicio = meio + 1

if(teste == True):
    print(f"O valor informado {valor} existe no vetor na posição {pos}")
else:
    print(f"O valor informado {valor} não existe no vetor")
