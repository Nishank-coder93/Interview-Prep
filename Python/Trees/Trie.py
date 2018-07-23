"""
Trie Tree to tackle String related problems 
Trie Operations: 
* insert(word)
* search(word)
* startsWith(prefix)
"""

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.root = TrieNode()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        
        for ch in word: 
            if node.children.get(ch,None) == None: 
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        
        for ch in word: 
            if ch not in node.children: 
                return False
            node = node.children[ch]
        
        return node.word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        
        for ch in prefix: 
            if ch not in node.children: 
                return False
            node = node.children[ch]
        
        return True