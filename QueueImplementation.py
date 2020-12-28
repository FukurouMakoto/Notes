class Queue:
    def __init__(self):
        self.QueueList = []
        #self.front = self.QueueList[0]
        #self.back = self.QueueList[-1]

    #Is queue empty?
    def is_empty(self):
        return len(self.QueueList) == 0

    #Return the size of the queue
    def size(self):
        if self.is_empty():
            return "Queue Empty"
        else:
            return len(self.QueueList)
    
    #Peek the element at the front of the queue
    #Throw error if queue is empty
    def peek(self):
        if self.is_empty():
            return "Queue Empty"
        else:
            return self.QueueList[0]
    
    #Poll an element from the front of the queue
    #Throw error if queue is empty
    def poll(self):
        if self.is_empty():
            return "Queue Empty"
        else:
            return self.QueueList.pop(0)

    #Add an element to the back of the queue
    def offer(self, element):
        self.QueueList.append(element)
    


    