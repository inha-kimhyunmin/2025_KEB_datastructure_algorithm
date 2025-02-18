class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def delete(self, data):
        if self.head.data == data:
            self.head.next = self.head
        else:
            current = self.head
            while current.next:
                if current.next.data == data:
                    current.next = current.next.next
                    # current.next 객체 삭제
                    print(f"값이 {data}인 노드 삭제")
                    break
                current = current.next



    def __str__(self):
        current = self.head
        return_str = ""
        while current:
            return_str += f"{current.data} "
            current = current.next
        return return_str


a = LinkedList()

a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)

print(a)
a.delete(4)
print(a)