#There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
#
#You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
#
#Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
		"""
		:type gas: List[int]
		:type cost: List[int]
		:rtype: int
		"""
		ind=z=g=0
	    	for i in xrange(len(gas)):
	    		g+=gas[i]-cost[i]
	    		if g<0:
	    			z+=-g
	    			ind=i+1
	    			g=0
	    	return -1 if g-z<0 else ind