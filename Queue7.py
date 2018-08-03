#
class Queue():
    def __init__(self,size):
        self.queue=[];
        self.size=size;
        self.head=0;
        self.tail=0;
    def Empty(self):
        if self.head==self.tail:
            return True
        else:
            return False
    def Full(self):
        if self.tail-self.head==self.size:
            return True
        else:
            return False
    def enQueue(self,content):
        if self.Full():
            print ("Queue is Full!")
        else:
            self.queue.append(content)
            self.tail=self.tail+1
            # print(self.tail)
            if self.tail>(2*self.size) :
                self.tail=self.tail-self.size
                self.head=self.head-self.size
            if self.Full():
                print ("Queue is Full!")                
    def outQueue(self):
        if self.Empty():
            print ("Queue is Empty!")
        else:
            self.head=self.head+1
            # print(self.head)
            if self.Empty():
                print ("Queue is Empty!")
            return self.queue.pop(0)

            
