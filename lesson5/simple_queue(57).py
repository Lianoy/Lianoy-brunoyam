class Queue:
    def __init__(self):
        self._storage = []

    def __repr__(self):
        return str(self._storage)

    def push(self, value: int):
        self._storage.append(value)
        print (f'Add {value} - Ok')

    def size(self):
        return len(self._storage)

    def front(self):
        return self._storage[0]

    def pop(self):
        result = self.front()
        self._storage.pop(0)
        return result

    def clear(self):
        while self.size():
            self.pop()
        print ('Clear - Ok')


queue = Queue()
while True:
    command=input("Введите команду:")
    if command == 'pop':
        print (queue.pop())
    elif command == 'back':
        print (queue.back())
    elif command == 'size':
        print (queue.size())
    elif command == 'clear':
        queue.clear()
    elif command == 'exit':
        print('Bye!~')
        break
    elif command == 'print':
        print(queue)
    else:
        lst=command.split()
        if lst[0] == 'push':
            queue.push(int(lst[1]))
        else:
            print ("Такой команды не существует!")