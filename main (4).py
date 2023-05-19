class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def printQueue(self):
        for e in self.items:
            print(e, end="->")
        print()

fila1 = Queue()
fila2 = Queue()

fila1Ent = input().strip().split()
fila2Ent = input().strip().split()

for i in fila1Ent:
    fila1.enqueue(i)

for i in fila2Ent:
    fila2.enqueue(i)

while not fila2.isEmpty():
    fila1.enqueue(fila2.dequeue())

while not fila1.isEmpty():
    print(fila1.dequeue(), end=" ")