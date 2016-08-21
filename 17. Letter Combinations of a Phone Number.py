#Given a digit string, return all possible letter combinations that the number could represent.
class Solution(object):
    def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		if len(digits)==0:
			return []
		l=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
		ans=[""]
		for i in digits:
			t=[]
			for j in l[int(i)]:
				for k in ans:
					t.append(k+j)
			ans=t
		return ans