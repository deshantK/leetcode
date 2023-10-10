import queue
q = queue.Queue()
stack = []
for i in range(5):
    q.put(i)
    stack.insert(0,i)
while stack:
    s = stack.pop()
    q_ = q.get()
    print (s, q_)
            
