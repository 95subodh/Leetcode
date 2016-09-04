#Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
#
#The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

class Solution(object):
    def isValidSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: bool
		"""
		def isValid(l):
			z=[]
			for i in l:
				if i!='.':
					z.append(i)
			return len(z)==len(set(z))
			
		for i in xrange(9):
			if not isValid(board[i]):
				return False
			
		for j in xrange(9):
			temp=[]
			for i in xrange(9):
				temp.append(board[i][j])
			if not isValid(temp):
				return False
		
		for i in xrange(3):
			for j in xrange(3):
				if not isValid([board[m][n] for n in xrange(3 * j, 3 * j + 3) for m in xrange(3 * i, 3 * i + 3)]):
					return False
		
		return True