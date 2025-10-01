# '''1. Crie um programa que abra (ou crie) um arquivo chamado frutas.txt 
# e escreva nele 5 nomes de frutas, um em cada linha. Use o modo de abertura w.
# '''
# arquivo = open("frutas.txt","w")


# for i in range(0,5):
#     fruta = input("Digite uma fruta: ")
#     arquivo.write(f"{fruta}\n")




# '''
# 2.Crie um programa que leia o conteúdo do arquivo frutas.txt e mostre cada fruta precedida da frase:
#  "Eu adoro a fruta: <fruta>"
# '''
# conteudo = arquivo.readlines()

# for y in range(0,len(conteudo)):
#     print(f"Eu adoro a fruta: {conteudo[y]}")

# arquivo.close()

# '''
# 3. Agora abra o arquivo frutas.txt no modo a e adicione mais 3 frutas. Depois, leia e exiba todo o conteúdo novamente.
# '''

# arquivo = open("frutas.txt","a")

# for o in range(0,8):
#     fruta = input("Digite uma fruta: ")
#     arquivo.write(f"{fruta}\n")


# conteudo = arquivo.readlines()

# for h in range(0,len(conteudo)):
#     print(f"Eu adoro a fruta: {conteudo[h]}")

# arquivo.close()

# '''
# Crie um programa que apague todo o conteúdo do arquivo frutas.txt 
# (dica: modo w sem escrever nada) e escreva apenas: "Desculpe, esqueci tudo
# '''

# arquivo = open("frutas.txt","w")

# arquivo.write("Desculpe, esqueci tudo\n")

# arquivo.close

'''
5. Lista de compras interativa
Peça para o usuário digitar 5 itens de compra e escreva cada um em uma nova linha no arquivo compras.txt.
'''

arquivo = open("compras.txt","w")

for i in range(0,5):
    compra = input("Digitive um item de compra: ")
    arquivo.write(f"{compra}\n")

arquivo.close()

arquivo = open("compras.txt","r")

ler = arquivo.readlines()
for y in range(0,5):
    print(f"{y+1} - {ler[y]}")

arquivo.close()

