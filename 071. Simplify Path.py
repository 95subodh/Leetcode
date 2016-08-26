#Given an absolute path for a file (Unix-style), simplify it.
class Solution(object):
    def simplifyPath(self, path):
		"""
		:type path: str
		:rtype: str
		"""
		l=map(str, path.split("/"))
		ans=[]
		for i in l:
			if i=='..':
				if len(ans):
					ans.pop()
			elif i!='.' and len(i):
				ans.append(i)
		result=""
		for i in ans:
			result+="/"+i
		return result if len(result) else "/"