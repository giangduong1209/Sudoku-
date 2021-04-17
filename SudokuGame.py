import random
import sys
m = 51800973
random.seed(m)
def latinSquare():
	matrixLatin = [[9,9,9],[9,9,9],[9,9,9]]
	for i in range(3):
		for j in range(3):
			col = [matrixLatin[0][j],matrixLatin[1][j],matrixLatin[2][j]]
			row = matrixLatin[i]
			latinTest = [0,1,2]
			if i>0 and j>0:
				latinTest = list(set(latinTest).difference(set(col+row)))
				if len(latinTest) > 1 and matrixLatin[i-1][j-1] in latinTest:
					latinTest.remove(matrixLatin[i-1][j-1])
				matrixLatin[i][j] = latinTest[0]
			else:		
				number = random.choice(latinTest)
				while(number in col or number in row):
					number = random.choice(latinTest)
				matrixLatin[i][j] = number
	return matrixLatin
def createLatinSquare(number):
    arrLatin=[]
    for i in range(number):
        arrLatin.append(latinSquare())
    return arrLatin
number = 12
print("Print 12 latin square")
for i in range(len(createLatinSquare(number))):
    print(createLatinSquare(number)[i])
def selectLatinSquare(matrixLatin):
    Cell = []
    for i in range(0,27,3):
        Cell.append(matrixLatin[i:i+3])
    Cell = [arr[0]+arr[1]+arr[2] for arr in Cell]
    return Cell
Block = []
for j in range(3):
    for k in range(9):
        Block.append(createLatinSquare(9)[k][j])
table = selectLatinSquare(Block)
print("Print 9 latin square")
for k in range(len(table)):
    print(table[k])
def latinSolve(index,matrixLatin):
    solve = [[[] for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            solve[i][j] = (1 + matrixLatin[i][j] + index*3)
    return solve
def SudokuSolveGame():
    tableGame = createLatinSquare(10)
    index = tableGame.pop()
    index = [index[i][j] for i in range(3) for j in range(3)]
    solveGame = []
    for i in range(9):
        solveGame.append(latinSolve(index[i],tableGame[i]))
    game=[]
    for j in range(3):
        for k in range(9):
            game.append(solveGame[k][j])
    boardGame = selectLatinSquare(game)
    return boardGame

def DiggingHole(n):
    SudokuGame = []
    SudokuGame = SudokuSolveGame()
    if n < 81 and n % 9 == 0:
        holeEachBlock = int(int(n)/9)
        for i in range(0,9):
            num = 0
            while num < holeEachBlock:
                j = random.randint(0,8)
                if SudokuGame[i][j] != 0:
                    SudokuGame[i][j] = 0
                    num += 1
        return SudokuGame
    else:
        exit
M=DiggingHole(int(sys.argv[1]))
def convert(M):
    arr=[]
    a = 0
    b = 3
    while a < 7 and b <10:
        temp1 = []
        temp2 = []
        temp3 = []
        for i in range(a,b):
            temp1 +=[M[i][m] for m in range(0,3)]
            temp2 +=[M[i][m] for m in range(3,6)]
            temp3 +=[M[i][m] for m in range(6,9)]
        arr += [temp1] + [temp2] + [temp3]
        a+=3
        b+=3
    return arr
sys.argv[2]
f = open(sys.argv[2],'w')
for l in convert(M):
    f.write(",".join(str(i) for i in l))
    f.write("\n")
f.close()