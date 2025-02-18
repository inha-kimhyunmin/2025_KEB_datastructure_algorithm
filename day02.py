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

    def printall(self):
        current = self.head
        while current:
            print(f"{current.data}", end = ' ')
            current = current.next
        print()

    def __str__(self):
        return "링크드 리스트 입니다."


a = LinkedList()

a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)

a.printall()
a.delete(4)
a.printall()

print(a)