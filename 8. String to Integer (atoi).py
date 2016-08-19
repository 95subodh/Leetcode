#Implement atoi to convert a string to an integer.
class Solution(object):
	    def myAtoi(self, str):
		"""
		:type str: str
		:rtype: int
		"""
		z=""
		f=0
		for i in xrange(len(str)):
			if str[i]==' ' and f==0:
				continue
			if f==0 and str[i] in '-+':
				z+=str[i]
				f=1
			elif '0'<=str[i]<='9':
				z+=str[i]
				f=2
			else:
				break
		if f==1 or len(z)<1:
			return 0
		else:
			if int(z)>2147483647:return 2147483647
			elif int(z)<-2147483648:return -2147483648
			else:return int(z)