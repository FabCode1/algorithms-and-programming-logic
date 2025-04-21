frase = input("Digite uma frase: ")
letra = input("Digite a letra a ser removida (primeira ocorrência): ")

indice = frase.find(letra)
if indice != -1:

	nova_frase = frase[:indice] + frase[indice+1:]
	print("Frase após a remoção:", nova_frase)
else:
	print("A letra não foi encontrada na frase.")