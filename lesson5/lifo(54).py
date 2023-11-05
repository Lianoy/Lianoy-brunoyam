class Stack:
    def __init__(self):
        self._storage = []

    def __repr__(self):
        return str(self._storage)

    def push(self, value: int):
        self._storage.append(value)
        print (f'Add {value} - Ok')

    def size(self):
        return len(self._storage)

    def back(self):
        back_ind = self.size()
        return self._storage[back_ind-1]

    def pop(self):
        result = self.back()
        self._storage.pop()
        return result

    def clear(self):
        while self.size():
            self.pop()
        print ('Clear - Ok')


stack = Stack()
while True:
    command=input("Введите команду:")
    if command == 'pop':
        print (stack.pop())
    elif command == 'back':
        print (stack.back())
    elif command == 'size':
        print (stack.size())
    elif command == 'clear':
        stack.clear()
    elif command == 'exit':
        print('Bye!~')
        break
    elif command == 'print':
        print(stack)
    else:
        lst=command.split()
        if lst[0] == 'push':
            stack.push(int(lst[1]))
        else:
            print ("Такой команды не существует!")