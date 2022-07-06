
"""
    FIFO queue -Queue
    LIFO queue -Stack
    Priority queue - orders the elements and returns the first lowest one


    Queue class methods
    -qsize()
    -empty()
    -full()
    -put()
    -get()
    -task_done()
    -join()
"""

import queue as q


customQ = q.Queue(maxsize=3)

print(customQ.qsize())
print(customQ.empty())

for x in range(3):
    customQ.put(x)

for _ in range(customQ.qsize() -1):
    customQ.get()

print(customQ.qsize())
print("Full: ", customQ.full())
