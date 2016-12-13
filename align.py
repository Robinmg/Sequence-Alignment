import sys

#m = scoring matrix
#s1 = sequence1
#s2 = sequence2
def traceBack(M, s1, s2):
	seq = ''
	row = len(s1)
	col = len(s2)
	while(True):
		if(col == 0): return seq
		if(row == 0):
			for i in range(col):
				seq += '_'
			return seq
		s = getNext(row, col, M)
		if(s[2] == 'x'):
			seq += s1[col-1]
		if(s[2] == 'z'):
			seq += '_'
		row = s[0]
		col = s[1]
	
	return seq
def getNext(row, col, M):#returns next cell in the traceback
	x = M[row-1][col-1]
	y = M[row-1][col]
	z = M[row][col-1]
	if((x >= y) & (x >=z)):
		return (row-1, col-1, 'x')#shift diagnal = in sequence
	elif(z >= y):
		return(row, col-1,'z')#shift left = add gap
	else: return (row-1, col, 'y')#shift down = do nothing

def score(indexOne, indexTwo, listOne, listTwo):
	if(listOne[indexOne] == listTwo[indexTwo]):
		return 5
	else: return (-2)


inputOne = raw_input("Sequence alphabet = {A, C, G, T}\nenter sequence #1: ")
inputTwo = raw_input("enter sequence #2: ")

#put input into list
sequenceOne = list(inputOne.rstrip())
sequenceTwo = list(inputTwo.rstrip())

#scoring matrix
M = [[0 for x in range(len(sequenceOne)+1)]for x in range(len(sequenceTwo)+1)]
TM = [[0 for x in range(len(sequenceOne)+1)]for x in range(len(sequenceTwo)+1)]
#opening and extension penalty
op = 6
ext = 1

#algorithm implementation
for j in range(1, len(sequenceOne)+1):#start at 1 since 0th row is zero-filled
	for i in range(1, len(sequenceTwo)+1):
		S = M[i-1][j-1] + score(j-1, i-1, sequenceOne, sequenceTwo)#must use j-1 for correct index since first rwo/column is zero filled
		if(M[i][j-1] - ext >= M[i][j-1] - op):#function I
			I = M[i][j-1] - ext
		else:
			I = M[i][j-1] - op
		if(M[i-1][j] - ext >= M[i-1][j] - op):
			D = M[i-1][j] - ext
		else:
			D = M[i-1][j] - op
		M[i][j] = max(S, I, D)
		
		if(M[i][j] == S):
			TM[i][j] = 'd'
		elif(M[i][j] == I):
			TM[i][j] = 'l'
		else: TM[i][j] = 'u'
formatString = ''
for i in range(len(sequenceTwo)+1):
	for j in range(len(sequenceOne)+1):
		formatString += str(M[i][j]) + " "
	formatString += '\n'
print formatString

#ans = traceBack(M, sequenceOne, sequenceTwo)
#print ans
col = len(sequenceOne)
row = len(sequenceTwo)
seq1 = ''
seq2 = ''
while(True):
	if(row == 0 and col ==0):
		print seq1
		print seq2
		sys.exit()
	nxt = TM[row][col]
	if nxt == 'd':
		seq1 = sequenceOne[col-1] + seq1
		seq2 = sequenceTwo[row-1] + seq2
		row = row - 1
		col = col - 1
	if nxt == 'l':
		seq1 = sequenceOne[col-1] + seq1
		seq2 = '_' + seq2
		col = col-1
	if nxt == 'u':
		seq1 = '_' + seq1
		seq2 = sequenceTwo[row-1] + seq2
		row = row-1

	
