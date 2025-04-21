frase=input('Frase:')
tam=len(frase)
i=0
palavra=0
while i < tam:
    #ignora os espaços em branco
    while i < tam and frase[i]==' ':
        i+=1
    #verifica se encontrou algo
    if i < tam:
        palavra+=1
        #avança até encontrar outro espaço e repete o processo
        while i < tam and frase[i]!=' ':
            i+=1

print(f'Nro de palavras: {palavra}')