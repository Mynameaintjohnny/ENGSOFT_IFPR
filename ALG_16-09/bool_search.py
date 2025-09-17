
vet = [15,10,3,12,5,7,1]
ordvet = [1,3,5,7,10,12,15]

valor = int(input("Informe um numero: "))

# Busca Binária

inicio = 0
fim = len(ordvet)-1
pos = None
teste = False

while(inicio <= fim):
    meio = int((inicio+fim)/2)

    if(ordvet[meio] == valor):
        teste = True
        pos = meio
        break

    elif(ordvet[meio] > valor):
        fim = meio - 1

    else:
        inicio = meio + 1

if(teste == True):
    print(f"O valor informado {valor} existe no vetor na posição {pos}")
else:
    print(f"O valor informado {valor} não existe no vetor")
