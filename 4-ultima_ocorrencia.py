entrada = input("Escreva uma frase: ")

letra= input("digite a letra que deseja encontrar a ultima posição:")

posicao = -1
i = 0

while i < len(entrada):
	if entrada[i] == letra:
		posicao = i 

	i += 1


if posicao != -1:
    print(f"A última ocorrência da letra '{letra}' está na posição {posicao + 1 }.")
else:
    print(f"A letra '{letra}' não foi encontrada na frase.")


