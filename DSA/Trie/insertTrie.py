

"""
    Searching for a string in a Trie:
        Case 1: String does not exist in the Trie
        Case 2: String exists in Trie
        Case 3: String is a prefix of another string, but it does not exist in a Trie

"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word):
        currentRootNode = self.root
        for i in word:
            ch = i 
            childNode = currentRootNode.children.get(ch)
            if childNode == None:
                childNode = TrieNode()
                childNode.children.update({ch:childNode})
            currentRootNode = childNode
        currentRootNode.endOfString = True 
        print("Successfully Inserted")

    
        

        




newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appi")

