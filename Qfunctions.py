class PQueue:
    #defining the constructor and initialising empty queues, size and front pointer
    DEFAULT_CAPACITY = 2
    def __init__ (self):
        self._data1 = [None]*PQueue.DEFAULT_CAPACITY
        self._data2 = [None]*PQueue.DEFAULT_CAPACITY
        self._size1 = 0
        self._size2 = 0
        self._front1 = 0
        self._front2 = 0
        self.prio=1

    #to check if the queue is empty
    def is_empty(self,prio):
        if prio=="1":
            return self._size1 == 0
        if prio=="2":
            return self._size2 == 0


    def dequeue(self,prio):
        if prio=="1":
            answer = self._data1[self._front1]
            self._data1[self._front1] = None
            self._front1 = (self._front1 + 1) % len(self._data1)
            self._size1 -= 1
            return answer

        elif prio=="2":
            answer = self._data2[self._front2]
            self._data2[self._front2] = None
            self._front2 = (self._front2 + 1) % len(self._data2)
            self._size1 -= 1
            return answer
        


    
    def enqueue(self,e):
        if self.prio==1:
            if self._size1 == len(self._data1):
                self.resize(1,2*len(self._data1))

                avail = (self._front1 + self._size1) % len(self._data1)
                self._data1[avail] = e
                self._size1 += 1
                self.prio=2
            else:
                avail = (self._front1 + self._size1) % len(self._data1)
                self._data1[avail] = e
                self._size1 += 1
                self.prio=2
                
        #if priority is set to high priority queue
        elif self.prio==2:
            if self._size2 == len(self._data2):
                self.resize(2,2*len(self._data2))
                avail = (self._front2 + self._size2) % len(self._data2)
                self._data2[avail] = e
                self._size2 += 1
                self.prio=1
            else:
                avail = (self._front2 + self._size2) % len(self._data2)
                self._data2[avail] = e
                self._size2 += 1
                self.prio=1


    def resize(self, prio, cap):
        if prio==1:
            old1 = self._data1 
            self._data1 = [None]* cap 
            walk1 = self._front1
            for k in range(self._size1): 
                self._data1[k] = old1[walk1] 
                walk1 = (1 + walk1) % len(old1)
            self._front1 = 0
        elif prio==2:
            old2 = self._data2 
            self._data2 = [None]* cap 
            walk2 = self._front2
            for k in range(self._size2): 
                self._data2[k] = old2[walk2] 
                walk2 = (1 + walk2) % len(old2)
            self._front2 = 0

    def display(self):
        return self._data1,self._data2


"""ts=PQueue()
print(ts.is_empty(1))
ts.enqueue(2)
ts.enqueue(2)
ts.enqueue(2)
ts.enqueue(2)
ts.dequeue("1")
ts.dequeue("1")
ts.display()
print(ts.is_empty(1))"""