class MinStack:
	def __init__(self):
		self.stack, self.minStack = [], []
	# @param x, an integer
	# @return an integer
	def push(self, x):
		self.stack.append(x)
		if len(self.minStack):
			if x < self.minStack[-1][0]:
				self.minStack.append([x, 1])
			elif x == self.minStack[-1][0]:
				self.minStack[-1][1] += 1
		else:
			self.minStack.append([x, 1])

	# @return nothing
	def pop(self):
		x = self.stack.pop()
		if x == self.minStack[-1][0]:
			self.minStack[-1][1] -= 1
			if self.minStack[-1][1] == 0:
				self.minStack.pop()
		
	# @return an integer
	def top(self):
		return self.stack[-1]
		
	# @return an integer
	def getMin(self):
		return self.minStack[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()