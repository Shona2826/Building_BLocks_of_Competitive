class QueueWithMax:
	def __init__(self):
		self._entries = collections.deque()
		self._candidates_for_max = collections.deque()

	def enqueue(self,x):
		self._entries.append(x)
		while self._candidates_for_max and self._candidates_for_max[-1] < x:
			self._candidates_for_max.pop()
		self._candidates_for_max.append(x)

	def dequeue(self):
		if self._entries:
			result = self._entries.popleft()
			if result == self._candidates_for_max[0]:
				self._candidates_for_max.popleft()

			return result
		raise IndexError('empty queue')

	def max(self):
		if self._candidates_for_max:
			return self._candidates_for_max[0]
		raise IndexError('empty queue')
