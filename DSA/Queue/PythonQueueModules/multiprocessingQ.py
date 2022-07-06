from multiprocessing import Queue


customQ = Queue(maxsize=3)


customQ.put(1)
customQ.put(2)
customQ.put(3)


for _ in range(customQ.qsize()):
    print(customQ.get())