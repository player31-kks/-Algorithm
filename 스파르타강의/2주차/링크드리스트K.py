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

    def get_kth_node_from_last(self, k):
        
        fast = self.head
        count = 0
        while fast and fast.next:
            fast = fast.next.next
            count+=1    
        if fast:
            count = count*2+1
        else:
            count = count*2
        
        return self.head
    def getLen(self):
        fast = self.head
        count = 0
        while fast and fast.next:
            fast = fast.next.next
            count+=1    
        if fast:
            count = count*2+1
        else:
            count = count*2
        
        return count
        


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)
linked_list.append(10)
linked_list.append(10)
linked_list.append(10)

# print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
print(linked_list.getLen())
