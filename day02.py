class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1] #맨 뒤

s1 = Stack()
s1.push(-9)
s1.push(11)
s1.push(777)
print(s1.pop())
print(s1.peek())
print(s1.peek())


a = list()

#push
a.append(1)

#pop
a.pop()

#Python에서는 굳이 Stack 클래스를 만들 필요가 없다.