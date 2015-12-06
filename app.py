#!/usr/bin/env python
# -*- coding: utf-8 -*-

from algoritmos import Radix


def main():
    
    x = Radix()
    
    x.addWord("abcdef")
    x.addWord("assunto")
    x.addWord("atrevido")

    x.addWord("boa")
    x.addWord("bolacha")
    
    x.addWord("calota")
    x.addWord("colecao")
    
    
    print x._data

    return 0

if __name__ == '__main__':
    main()
