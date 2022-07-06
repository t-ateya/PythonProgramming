

"""
    Deletion Cases:
    N.B: Deletion of any string from Trie always starts from the leaf node
        Case 1. Some other prefix of string is same as the one that we want to delete.E.g (API, APPLE)
        Case 2. The string is a prefix of another string. (API, APIS)
        Case 3. Other string is a prefix of this string. (APIS, AP)
        Case 4. Not any node depends on this string (K)


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


def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False

    if len(currentNode.children) > 1:
        deleteString(currentNode,word, index+1)
        return False

    if index == len(word) -1:
        if len(currentNode.children) >=1:
            currentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True

    if currentNode.endOfString == True:
        deleteString(currentNode, word, index + 1)
        return False

    canThisNodeBeDeleted = deleteString(currentNode, word, index +1)
    if canThisNodeBeDeleted:
        root.children.pop(ch)
        return True
    else:
        return False





newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appi")
deleteString(newTrie.root, "App", 0)
print(newTrie.searchString("App"))
