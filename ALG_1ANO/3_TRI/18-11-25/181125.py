# linha =3
# coluna= 4
# matriz = [0] * linha
# for i in range(0, linha):
#     matriz[i] = [0] * coluna


# class Disciplina:
#     def __init__(self):
#         self.id = 0
#         self.nome = ""
#         self.ch = 0
#         self.professor = ""

# d1 = Disciplina()
# d1.nome = "Algoritimos"
# d1.ch = 200


# d2 = Disciplina()
# d2.nome = "Eng. de software"
# d1.ch = 100


#LISTAS
# lista = []
# print(lista)

# lista.append(5) # insere no fim da lista
# lista.append("aula") 
# lista.append(80.2)

# print(lista[1])

# lista.insert(1,"oi") # insire na indice, cria um valor novo e empura o resto pra frente

# x = lista.pop(2) #exclui o valor do indice, retorna o valor de dentro

# lista.remove(80.2) #remove a primeira ocorrencia do valor especificado


# Crie um programa que gerencie uma lista de convidados para uma festa
# O programa deve
# começar com uma lista vazia
# pedir ao usuario por 6 nomes para adicionar na lista usando append()
# perguntar ao usuario qual nome ele deseja remover com remove()
# exibir lista final

# convidados = []

# print("Digite 6 nomes para adicionar em sua lista de convidados: ")

# for i in range(0,6):
#     nome = input(f"Digite o {i}º nome: ")
#     convidados.append(nome)


# for y in range(0,len(convidados)):
#     choice = int(input(f"Deseja excluir o {y+1}º convidado {convidados[y]}? Digite 1 se sim": ))

#     if(choice == 1):
#         convidados.remove()
    
#     choice == 0

# for r in range(0,len(convidados)):
#     print(convidados[r])


#TUPLAS
# tupla = ("Ayslan",40,8.79,False)
# print(tupla[0])

# nome = input("Passo o nome de um produto pa nois: ")
# preco = float(input("Passa o preco dele: "))
# qtd = int(input("Passa a quantidade do produto: "))

# produto = (nome,preco,qtd)
# for i in range(0,len(produto)):
#     print(produto[i])

# print(f"O tamanho da tupla é de {len(produto)} indices")


#CONJUNTOS
# a = set()
# a.add(1)
# a.add(5)
# a.add(7)
# a.add(2)

# b = set()
# b.add(2)
# b.add(3)
# b.add(7)
# b.add(35.5)

# uniao = a.union(b)
# inter = a.intersection(b)
# difA = a - b

# x = {1,7}
# subc= x.issubset(a)
# pert = 3 in b



# print(uniao)
# print(inter)
# print(difA)
# print(uniao)
# print(subc)
# print(pert)

''' CRIE DOIS CONJUNTOS:
turma_a = {'Ana','Beto','Carlos','Duda'}
turma_b = {'Carlos','Edu','Fernanda','Ana'}

SEU PROGRAMA DEVE:
MOSTRAR OS ALUNOS QUE ESTÃO NAS DUAS TURMAS (INTERSEÇÃO)
MOSTRAR OS ALUNOS QUE ESTÃO SOMENTE NA TURMA A (DIFERENÇA)
MOSTRAR A UNIAO DAS DUAS TURMAS (TODOS OS ALUNOS SEM REPETIÇÃO)'''

# turma_a = {['Ana','Beto','Carlos','Duda']}
# turma_b = {['Carlos','Edu','Fernanda','Ana']}

# interc = turma_a.intersection(turma_b)
# difeA = turma_a - turma_b
# union = turma_a.union(turma_b)

# print(f"Interceção: {interc}\nAlunos somente da classe A: {difeA}\nTodos os alunos das duas classes: {union}")



#DICIONARIOS




'''CRIE UM DICIONARIO CHAMADO ALUNO CONTENDO:
NOME
IDADE
CURSO
    DEPOIS
EXIBA CADA INFORMAÇÃO SEPARADAMENTE
ATUALIZE A IDADE DO ALUNO
ADICIONE UMA NOVA CHAVE CHAMADA 'NOTA'
REMOVA A CHAVE 'CURSO'
EXIBA O DICIONARIO FINAL
'''

aluno = {
    "nome" : "Juninho",
    "idade" : 20,
    "curso": "eng. de software"

}

for chave, valor in aluno.items():
    print(f" {chave} : {valor}")

aluno["idade"] = 25
aluno["nota"] = "B"
aluno.pop("curso")

print("\n")
for chave, valor in aluno.items():
    print(f" {chave} : {valor}")
