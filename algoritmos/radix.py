#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

class Radix(object):
    """
    Implement a trie with insert, search, and startsWith methods.
    """
    def __init__(self):
        self.root = defaultdict()

    def insert(self, word):
        """Inserts a word into the trie."""
        current = self.root
        for letter in word.lower():
            current = current.setdefault(letter, {})
        current.setdefault("_end")

    def search(self, word):
        """Returns True if the word is in the trie."""
        current = self.root
        for letter in word.lower():
            if letter not in current:
                return False
            current = current[letter]
        if "_end" in current:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns True if there is any word in the trie
        that starts with the given prefix.
        Returns that find prefix
        """
        current = self.root
        index = 0
        for letter in prefix.lower():
            if letter not in current:
                return (False, None)
            else:
                current = current[letter]
                index = index+1
            
        #~ print index
        return (True, prefix[:index+1])
        


