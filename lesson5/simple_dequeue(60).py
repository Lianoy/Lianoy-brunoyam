class Dequeue:
    def __init__(self):
        self._storage = []

    def __repr__(self):
        return str(self._storage)

    def push_back(self, value: int):
        self._storage.append(value)
        print (f'Add {value} at back - Ok')

    def push_front(self, value: int):
        self._storage.insert(0,value)
        print (f'Add {value} at front - Ok')

    def size(self):
        return len(self._storage)

    def front(self):
        return self._storage[0]
    
    def back(self):
        back_ind = self.size()
        return self._storage[back_ind-1]

    def pop_front(self):
        result = self.front()
        self._storage.pop(0)
        return result

    def pop_back(self):
        result = self.back()
        self._storage.pop()
        return result

    def clear(self):
        while self.size():
            self.pop_front()
        print ('Clear - Ok')


dequeue = Dequeue()
while True:
    command=input("Введите команду:")
    if command == 'pop_back':
        print (dequeue.pop_back())
    elif command == 'pop_front':
        print (dequeue.pop_front())
    elif command == 'back':
        print (dequeue.back())
    elif command == 'size':
        print (dequeue.size())
    elif command == 'clear':
        dequeue.clear()
    elif command == 'exit':
        print('Bye!~')
        break
    elif command == 'print':
        print(dequeue)
    else:
        lst=command.split()
        if lst[0] == 'push_back':
            dequeue.push_back(int(lst[1]))
        elif lst[0] == 'push_front':
            dequeue.push_front(int(lst[1]))
        else:
            print ("Такой команды не существует!")