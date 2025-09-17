'''
Exercício 01: Utilizando o algoritmo de ordenação por Bolha (Bubble Sort) onde um ciclo de trocas corresponde
a fazer a comparação de todos os valores do vetor com os seus adjacentes. Considere o seguinte vetor:
valores = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Considere ainda que o vetor “valores” precise ser ordenado de forma crescente. Considerando o “pior caso”
(onde o vetor está completamente desordenado, na ordem inversa a que se deseja), quantos ciclos de troca
serão necessários para ordenar o vetor valores?
'''

vet = [0] * 10
cont = 10
aux = None
for i in range(0,len(vet)):
    vet[i] = cont
    cont = cont - 1
    
print(f"Vetor cru: {vet}\n")
for g in range(0,len(vet)-1):
    
    for y in range(0,len(vet)-1):
        
        if(vet[y] > vet[y+1]):
            aux = vet[y]
            vet[y] = vet[y+1]
            vet[y+1] = aux
            
    print(f"{g+1}ª execução: {vet}")