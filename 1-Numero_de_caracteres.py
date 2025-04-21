# Exercício 01
# ● Faça um programa que leia uma String e escreva:
# ○ O número de caracteres que a string contém
# ○ Caractere por caractere, utilizando laço de repetição
# ○ Caractere por caractere, porém na ordem inversa, utilizando laço de repetição


entrada = input("escreva uma uma palavra: ")
c = 0
for i in entrada:
	c+= 1 
print(f"A quantidade de caracteres é {c}") 