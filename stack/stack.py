class Stack:
    def __init__(self):
        self.item=[]
    def is_empty(self):
        return len(self.item)==0
    def push(self,element):
        self.item.append(element)
    def pop(self):
        if self.is_empty():
            return 'Stack is empty.'
        return self.item.pop()
    def peek(self):
        if self.is_empty():
            return 'Stack is empty.'
        return self.item[-1]

    def size(self):
        return len(self.item)

    def clear(self):
        self.item=[]
    def __str__(self):
        if self.is_empty():
            return "Stack is empty."
        values=[str(x) for x in reversed(self.item)]
        return '\n'.join(values)
def main():
    stack_1=Stack()
    stack_1.push(1)
    print(stack_1.is_empty())
    print(stack_1)
    val=stack_1.pop()
    print(stack_1)
    print(f"Popped value is: {val}.")
if __name__=='__main__':
    main()