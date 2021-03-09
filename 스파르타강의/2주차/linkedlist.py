class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head        
        for i in range(index):
            cur = cur.next
        return cur

    def add_node(self, index, value):
        temp = Node(value)
        cur = self.get_node(index)

        temp.next = cur.next
        cur.next = temp
        return "index 번째 Node 뒤에 value 를 추가하세요!"
    
    def delete_node(self, index):
        cur = self.get_node(index-1)
        cur.next=  cur.next.next
        return "index 번째 Node를 제거해주세요!"
    


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(0, 3)
linked_list.print_all()
