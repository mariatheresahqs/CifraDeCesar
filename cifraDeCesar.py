codificacao = int(input()) #1 codificar 0 descodificar 
chave_alfabeto = int(input()) # um valor em número que será usado para codificar a msg
chave_numeros = int(input()) # um valor em número que será usado para codificar a msg
frase  = input()

numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
i=0
novaPalavra = ""


if(codificacao==1):
    while(i<len(frase)):
        for j in range(len(alfabeto)):
            if frase[i]==alfabeto[j]:
                if (j+chave_alfabeto <26):
                    novaPalavra = novaPalavra + alfabeto[j+chave_alfabeto] 
                elif (j+chave_alfabeto > 26 and j<26):
                    novaPalavra = novaPalavra + alfabeto[((j+chave_alfabeto)%26)]
                elif (j+chave_alfabeto < 51 and j>25):
                    novaPalavra = novaPalavra + alfabeto[((j+chave_alfabeto))]
                elif (j>26 and j+chave_alfabeto > 51):
                    novaPalavra = novaPalavra + alfabeto[((j+chave_alfabeto)%52)+26]
        for j in range(len(numeros)):
            if frase[i]==numeros[j]:
                novaPalavra = novaPalavra + numeros[((j+chave_numeros)%10)]
        if (frase[i]==" "):
                novaPalavra = novaPalavra + " "
        i += 1
    print(novaPalavra)


if(codificacao==0):
    while(i<len(frase)):
        for j in range(len(alfabeto)):
            if frase[i]==alfabeto[j]:

                if (j-chave_alfabeto < 0):
                    novaPalavra = novaPalavra + alfabeto[26+(j-chave_alfabeto)]
                elif (j-chave_alfabeto < 26 and j>25):
                    novaPalavra = novaPalavra + alfabeto[26+(j-chave_alfabeto)]
                elif ((j-chave_alfabeto >=0 and j-chave_alfabeto<26) or (j-chave_alfabeto>=26 and j>25)):
                    novaPalavra = novaPalavra + alfabeto[((j-chave_alfabeto))]


        for j in range(len(numeros)):
            if frase[i]==numeros[j]:
                novaPalavra = novaPalavra + numeros[((j-chave_numeros)%10)]
        if (frase[i]==" "):
                novaPalavra = novaPalavra + " "
        i += 1
        
    print(novaPalavra)
