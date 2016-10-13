#Given an array of strings, group anagrams together.
#
#For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
#Return:
#
#[
#	["ate", "eat","tea"],
#	["nat","tan"],
#	["bat"]
#]
#Note: All inputs will be in lower-case.

class Solution(object):
	def groupAnagrams(self, strs):
		"""
		:type strs: List[str]
		:rtype: List[List[str]]
		"""
		dict={}
		for i in strs:
			z="".join(sorted(i))
			if z in dict:
				dict[z].append(i)
			else:
				dict[z]=[i]
		ans=[]
		for i in dict:
			ans.append(dict[i])
		return ans