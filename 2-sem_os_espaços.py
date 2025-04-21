# APR1 - Strings
# Exercício 02
# ● Faça um programa que leia uma frase e imprima a quantidade de caracteres que
# essa string contém, com exceção de espaços em branco.

entrada = input("escreva uma uma palavra: ")
c = 0
for caractere in entrada:
    if caractere != " ":  
        c += 1
print(f"A quantidade de caracteres é sem os espaços é {c}") 

# Com o while 


c = 0
i = 0

while i < len(entrada):
    if entrada[i] != " ":  
        c += 1
    i += 1  

print(f"A quantidade de caracteres sem os espaços é {c}")