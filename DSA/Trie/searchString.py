

"""
    Insertion Cases:
        1. A Trie is Blank e.g inserting "APP" as a string prefix to a blank Trie
        2. New string's prefix is common to another string's prefix e.g inserting "API" to a Trie which alreay has "APP" as prefix
        3. New string's prefix is already present as complete  string e.g inserting "APIS" to  Trie which alreay has "API" as prefix
        4. String to be inserted is already present in the Trie e.g inserting "APIS" to a Trie which already has "APIS" as prefix


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

    
    def searchString(self, word):
        """Searches a string in Trie"""
        currentNode = self.root
        for ch in word:
            node = currentNode.children.get(ch)
            if node == None:
                return False
            currentNode = node

        if currentNode.endOfString == True:
            return True
        else:
            return False

        




newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appi")
print(newTrie.searchString("DCD"))
