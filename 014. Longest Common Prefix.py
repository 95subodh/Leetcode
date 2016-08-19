#Write a function to find the longest common prefix string amongst an array of strings.
class Solution(object):
    def longestCommonPrefix(self, strs):
	"""
	:type strs: List[str]
	:rtype: str
	"""
	z=""
	i=f=0
	while 1:
		if len(strs)>0 and len(strs[0])>i:
			tmp=strs[0][i]
		else:
			break
		for str in strs:
			if len(str)==i or str[i]!=tmp:
				f=1
		if f:break
		else:z+=tmp
		i+=1
	return z