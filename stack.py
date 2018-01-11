# stack.py

# test code

"""
stack = []
size = 5

def push(element):
    if len(stack) < 5:
        stack.append(element)
    else:
        print('Can\'t push. The stack is full!')

def pop():
    try:
        popped = stack[len(stack)-1]
    except:
        popped = 'The stack is empty!'
        
    return popped
"""

class Stack():
    def __init__(self, aSize):
        self.size = int(aSize)
        self.stack = []
        self.top = None
        
    def push(self, element):
        """push an element to the stack"""
        if len(self.stack) < self.size:
            self.stack.append(element)
            self.top = self.stack[-1]
        else:
            print('Can\'t push. The stack is full!')

    def pop(self):
        """Pop an element from the stack"""
        try: popped = self.stack.pop(-1)
        except: popped = 'The stack is empty!'
        
        return popped

    def isEmpty(self):
        """Check if the stack is empty"""
        if len(self.stack) == 0: return True
        else: return False

    def whosTop(self):
        """See the top element"""
        if self.isEmpty():  print('No top. The stack is empty')
        else: return self.top
                  

if __name__ == '__main__':
    aSize = input('Enter the stack size: ')
    s = Stack(aSize)
    print('Your stack s is generated')
    
