class Node:
    def __init__(self,value):
        self.value = value
        self.next = []

class Trie:
    def __init__(self):
        self.root = Node(None)
    def add(self,parent,string):
        if len(string)==0:
            return
        find_char = string[0]
        for n in parent.next:
            if n.value == find_char:
                self.add(n,string[1:])
                return
        child=Node(find_char)
        parent.next.append(child)
        self.add(child,string[1:])
            
    def printAll(self,node):
        if not node.next:
            return
        for n in node.next:
            print(n.value)
            self.printAll(n)

trie = Trie()
trie.add(trie.root,"ball")
trie.add(trie.root,"boll")
trie.add(trie.root,"baoo")
trie.printAll(trie.root)