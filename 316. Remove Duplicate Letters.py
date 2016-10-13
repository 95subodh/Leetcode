#Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
#
#Example:
#Given "bcabc"
#Return "abc"
#
#Given "cbacdcbc"
#Return "acdb"

class Solution(object):
	def removeDuplicateLetters(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		appeared={}
		for i in s:
			if i in appeared:
				appeared[i]+=1
			else:
				appeared[i]=1
		stack=[]
		for i in s:
			if i not in stack:
				while stack and stack[-1]>i and appeared[stack[-1]]:
					stack.pop()
				stack.append(i)
			appeared[i]-=1
		return "".join(stack)