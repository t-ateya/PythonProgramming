from collections import deque

customQueue = deque(maxlen=3)
print(customQueue)


for element in range(3):
    customQueue.append(element)


print(customQueue)
#print(customQueue.popleft())
print(customQueue.clear())
print(customQueue)