class PQueue:
    #defining the constructor and initialising empty queues, size and front pointer
    DEFAULT_CAPACITY = 2
    def __init__ (self):
        self._data1 = [None]*PQueue.DEFAULT_CAPACITY
        self._size1 = 0
        self._front1 = 0


    #to check if the queue is empty
    def is_empty(self,prio):

        return self._size1 == 0



    def dequeue(self):

        answer = self._data1[self._front1]
        self._data1[self._front1] = None
        self._front1 = (self._front1 + 1) % len(self._data1)
        self._size1 -= 1
        return answer


    
    def enqueue(self,e):

        if self._size1 == len(self._data1):
            self.resize(1,2*len(self._data1))

            avail = (self._front1 + self._size1) % len(self._data1)
            self._data1[avail] = e
            self._size1 += 1


    def resize(self, cap):

            old1 = self._data1 
            self._data1 = [None]* cap 
            walk1 = self._front1
            for k in range(self._size1): 
                self._data1[k] = old1[walk1] 
                walk1 = (1 + walk1) % len(old1)
            self._front1 = 0
            
    def display(self):
        return self._data1
