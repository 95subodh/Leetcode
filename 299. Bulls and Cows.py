#You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.
#
#For example:
#
#Secret number:  "1807"
#Friend's guess: "7810"

class Solution(object):
    def getHint(self, secret, guess):
		"""
		:type secret: str
		:type guess: str
		:rtype: str
		"""
		b=c=0
		dict={}
		for i in xrange(len(secret)):
			if secret[i]==guess[i]:
				b+=1
			else:
				if secret[i] in dict:
					dict[secret[i]]+=1
					if dict[secret[i]]<1:
						c+=1
				else:
					dict[secret[i]]=1
				
				if guess[i] in dict:
					dict[guess[i]]-=1
					if dict[guess[i]]>-1:
						c+=1
				else:
					dict[guess[i]]=-1
		return "%dA%dB" % (b, c)