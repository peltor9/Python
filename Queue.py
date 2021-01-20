                                                                        ## Adding/Removing que
queue = []							# Initializing a queue

queue.append('a')							# Adding elements to the queue
queue.append('b')
queue.append('c')
print("Initial queue")
print(queue)
print("\nElements dequeued from queue") 				# Removing elements from the queue
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("\nQueue after removing elements")
print(queue)
                                                                           ## IsFull/IsEmpty/MaxSize
from queue import Queue

q = Queue(maxsize = 3) 						# Initializing a queue
print(q.qsize()) 							#qsize() give the max size  of the Queue 
q.put('a')							# Adding of element to queue
q.put('b')
q.put('c')	
print("\nFull: ", q.full()) 						# Return Boolean for Full # Queue 
print("\nElements dequeued from the queue")  		# Removing element from queue
print(q.get())
print(q.get())
print(q.get())
print("\nEmpty: ", q.empty()) 						# Return Boolean for Empty  # Queue 
q.put(1)
print("\nEmpty: ", q.empty()) 
print("Full: ", q.full())
