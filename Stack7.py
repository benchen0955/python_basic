#ջ��ʵ��

class Stack():
    def __init__(self,size):
        self.stack=[];
        self.size=size;
        self.top=0;

    def push(self,content):
        if self.Full():
            print ("Stack is Full!")
        else:
            self.stack.append(content)
            self.top=self.top+1
            if self.Full():
                print ("Stack is Full!")

    def out(self):
        if self.Empty():
            print ("Stack is Empty!")
        else:            
            self.top=self.top-1
            if self.Empty():
                print ("Stack is Empty!")
            return self.stack.pop()
    def Full(self):
        if  self.top==self.size:
            return True
        else:
            return False
    def Empty(self):
        if self.top==0:
            return True
        else:
            return False
