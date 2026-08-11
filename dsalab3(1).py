#queue
class queue:
    def __init__(self):
        self.queue=[]
    def add_element(self,e):
        if (len(self.queue))>3:
                print("queue is full")
        else:
            self.queue.append(e)
            
    def delete_element(self):
        if self.queue==[]:
            print("queue is empty")
        else:
            print("popped element:",self.queue.pop(0))
    def display(self):
        print("queue:",self.queue)
    def peek(self):
        print("top element:",self.queue[0])
q=queue()

while True:
    print("what you want to do?:")
    print("1. add.\n2. delete.\n3. display.\n4. peek.\n5. exit")
    ch=int(input("enter choices:"))
    if ch==1:
        e=int(input("enter element:"))
        q.add_element(e)
    elif ch==2:
        q.delete_element()
    elif ch==3:
        q.display()
    elif ch==4:
        q.peek()
    elif ch==5:
        print("thankyou")
        break
    else:
        break