# Implementation d'une file
class MyQueue:
    def __init__(self):
        # La queue
        self.in_stack = []
        # La tete
        self.out_stack = []

    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)

    def push(self,obj):
        self.in_stack.append(obj)

    def pop(self):
        # tete vide
        if not self.out_stack:
            self.out_stack = self.in_stack[::-1]
            self.in_stack = []
        return self.out_stack.pop()

    def __str__(self):
        return str(self.out_stack[::-1] + self.in_stack)
