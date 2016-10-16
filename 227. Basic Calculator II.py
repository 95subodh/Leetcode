#Implement a basic calculator to evaluate a simple expression string.
#
#The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
#
#You may assume that the given expression is always valid.
#
#Some examples:
#"3+2*2" = 7
#" 3/2 " = 1
#" 3+5 / 2 " = 5
#Note: Do not use the eval built-in library function.

class Solution(object):
	def calculate(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		stack=[]
		num=0
		for i in s:
			if '0'<=i<='9':
				num = num*10 + int(i)
			elif i=='-' or i=='+' or i=='/' or i=='*':
				if len(stack)>1 and stack[-1] in ['/','*']:
					x=stack.pop()
					z=stack.pop()
					if x=='/':
						stack.append(z/num)
					else:
						stack.append(z*num)
				else:
					stack.append(num)
				stack.append(i)
				num=0
		stack.append(num)
		if len(stack)>1:
			if stack[-2]=='/':
				z=stack.pop()
				stack.pop()
				y=stack.pop()
				stack.append(y/z)
			elif stack[-2]=='*':
				z=stack.pop()
				stack.pop()
				y=stack.pop()
				stack.append(y*z)
		stack=stack[::-1]
		while len(stack)>1:
			z=stack.pop()
			x=stack.pop()
			y=stack.pop()
			if x=='+':
				stack.append(y+z)
			elif x=='-':
				stack.append(z-y)
		return stack[-1]