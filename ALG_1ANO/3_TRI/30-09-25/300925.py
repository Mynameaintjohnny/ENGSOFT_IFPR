arquivo = open("dados.txt","a", encoding = "utf8")

nome = input("Digita um nome ai pa nois: ")
arquivo.write(f"\nNomezin do usuário é {nome}")

arquivo.close()