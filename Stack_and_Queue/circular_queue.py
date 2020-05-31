class Queue:
	SCALE_FACTOR = 2

	def __init__(self,capacity):
		self._entries = [None] * capacity
		self._head = self._tail = self._num_queue_elements = 0
	def enqueue(self,x):
		if self._num_queue_elements == len(self._entries):
			self._entries = (self._entries[self._head:] + self._entries[:self._head])
			self._head,self._tail = 0,self._num_queue_elements
			self._entries += [None] * (len(self._entries) * Queue.SCALE_FACTOR - len(self._entries))
		self._entries[self._tail] = x
		self._tail = (self._tail + 1) % len(self._entries)
		self._num_queue_elements += 1
	def dequeue(self):
		if not self._num_queue_elements:
			raise IndexError('empty queue')
		self._num_queue_elements -= 1
		ret = self._entries[self._head]
		self._head = (self._head +1)%len(self._entries)
		return ret
	def size(self):
		return self._num_queue_elements


q = Queue(2)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.dequeue()
x = q.size()
print(x)