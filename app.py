#!/usr/bin/env python
#!/usr/bin/env python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from algoritmos import Radix


def main():
    
    x = Radix()
    
    x.addWord("abcdef")
    x.addWord("assunto")
    x.addWord("atrevido")
    
    print x._data

    return 0

if __name__ == '__main__':
    main()
