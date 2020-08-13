class stack():
    def __init__(self):
        self.myStorage = []
        self.stackType = None

    def push(self, data):
        if self.isEmpty():
            self.myStorage.append(data)
            self.stackType = type(data)

        elif self.stackType == type(data):
            self.myStorage.append(data)
        else:
            raise Exception('Error: Wrong Type')

    def top(self):
        return self.myStorage[-1]

    def pop(self):
        if not self.isEmpty():
            self.myStorage.pop()
        else:
            raise Exception('Error: Nothing in myStorage to pop')

    def isEmpty(self):
        return len(self.myStorage) == 0

    def display(self):
        output = ""
        for item in self.myStorage:
            item = str(item)
            if item == str(self.myStorage[0]):
                output = output + item
            else:
                output = output + "\n" + item
        return output

    def getType(self):
        return type(self.myStorage[0])
    
    def getSize(self):
        return len(self.myStorage)
