class PriorityQueuedown(int):
	def __init__(self):
		self.queue = []

	def __str__(self):
		return ' '.join([str(i) for i in self.queue])

	# for checking if the queue is empty
	def isEmpty(self):
		return len(self.queue) == 0

	# for inserting an element in the queue
	def insert(self, data):
		self.queue.append(data)
		self.queue.sort()


	def peek(self):
		if self.queue.__sizeof__()!=0:
			x = self.queue.pop()
			self.queue.append(x)
			return int(x)

	def size(self):
		self.queue.__sizeof__()

	# for popping an element based on Priority
	def delete(self):
		self.queue.pop()

class PriorityQueueup(int):
	def __init__(self):
		self.queue = []

	def __str__(self):
		return ' '.join([str(i) for i in self.queue])

	# for checking if the queue is empty
	def isEmpty(self):
		return len(self.queue) == 0

	# for inserting an element in the queue
	def insert(self, data):
		self.queue.append(data)
		self.queue.sort()
		self.queue.reverse()


	def peek(self):
		if self.queue.__sizeof__() != 0:
			x = self.queue.pop()
			self.queue.append(x)
			return int(x)

	def size(self):
		self.queue.__sizeof__()

	# for popping an element based on Priority
	def delete(self):
		self.queue.pop()


if __name__ == '__main__':
		myQyeue = PriorityQueueup()
		myQyeue.insert(5)
		myQyeue.insert(3)
		myQyeue.insert(39)
		myQyeue.insert(1)
		print(myQyeue.peek())
		print(myQyeue)





