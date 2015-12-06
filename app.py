#!/usr/bin/env python
# -*- coding: utf-8 -*-

from algoritmos import Radix

# NOTAS SOBRE ESSE PROGRAMA.
# Fiquei com um bug no startWith - gostaria de devolver a palavra
# semelhante encontrada no dicionario, mas ainda não consegui fazer isso
# pensei em apenas identificar o indice de até onde são iguais e fazer
# um slice na string recebida, mas não ficou bom...

def main():
    
    # Loading files content.
    f_dictionary = open("data/dicionario.txt")
    f_text = open("data/texto.txt")
    
    # Create objects to handle with text
    dictionary = Radix()
    
    # Put words from dict file in dict object
    for word in f_dictionary.read().split():
        dictionary.insert(word)
    
    print "Carregando dicionario..."
    print "...pronto!"
    
    print ""
    
    print "Iniciando correcao do texto..."
    
    print ""
    print ""
    
    find, word = dictionary.startsWith("pea")
    print find, word
    
    # Read words from file
    for word in f_text.read().split():
        #~ print word
        if not (dictionary.search(word)):
            print ("palavra: \"" + word + "\" nao estah no dicionario")
            continue
        
        find, t_word = dictionary.startsWith(word)
        if(find):
            print ("Achei algo parecido com: \"" + t_word.lower() + "\" no arquivo com texto")
        
    return 0

if __name__ == '__main__':
    main()
