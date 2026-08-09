class Stack:
    def __init__(self):
        self.item=[]

    def push(self,element):
        self.item.append(element)

def main():
    stack_1=Stack()
    stack_1.push(1)

if __name__=='__main__':
    main()