class Stack:

    def __init__(self, items=[], limit=100):
        self.items = []
        self.limit = limit
        if (len(items) > 0):
            for item in items:
                if (len(self.items) < self.limit):
                    self.items.append(item)

    def isEmpty(self):
        if (len(self.items) == 0):
            return True
        return False

    def push(self, item):
        if (len(self.items) < self.limit):
            self.items.append(item)

    def pop(self):
        if (len(self.items) != 0):
            return self.items.pop(-1)

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        if (len(self.items) == self.limit):
            return True
        return False

    def search(self, target):
        if (target in self.items):
            i = 1
            for item in self.items:
                if (item == target):
                    return len(self.items) - i
                i += 1
        return -1
