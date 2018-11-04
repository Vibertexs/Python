import random as r
import tensorflow as tf

# the size of the board given by the user
size = int(input("Give a number for dimension: "))

# randomly generate an n x n board
def initboard(n):
    # initialize a board to return
    board = []
    # go through the board to initialize the random values
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(r.randint(1,n-1))
        board.append(temp)
    board[n-1][n-1] = 0
    br = board[n-1][n-1]
    # return the board when complete
    return board

# printing out the board ex) 4 x 4 board
# _______________________
# 4 | 1 | 2 | 3 |
# _______________________
# 3 | 1 | 1 | 1 |
# _______________________
# 1 | 2 | 1 | 2 |
# _______________________
# 2 | 1 | 1 | 2 |
# _______________________
def showboard(x):
    print('_______________________')
    for e in x:
        for element in e:
            print(str(element), end="")
            print(" | ", end=" ")
        print('\n' + '_______________________')


# initialize the board# initi 
b = initboard(size)
print(b)
# showboard(board)
showboard(b)
#showboard(evaluateboard(b))

def copyBoard(board):
    newBoard = []
    for i in range(len(board)):
        newBoard.append(board[i].copy())
    return newBoard

def evaluateboard(b, evaluation, currenteval, size):
    for i in range(size):
        for j in range(size):
            if evaluation[i][j] == currenteval:
                move = b[i][j]
                # moves down a row
                if (i+move) < size and evaluation[i+move][j] == -1:
                        evaluation[i+move][j] = currenteval + 1
                # moves to the right of a column
                if (j+move) < size and evaluation[i][j+move] == -1:
                        evaluation[i][j+move] = currenteval + 1
                # moves up a row
                if (i-move) > 0 and evaluation[i-move][j] == -1:
                        evaluation[i-move][j] = currenteval + 1
                # moves to the left of a column
                if (j-move) > 0 and evaluation[i][j-move] == -1:
                        evaluation[i][j-move] = currenteval + 1                   
    return evaluation

evalpuzzle = []
# initialize the eval board
for i in range(size):
    temp = []
    for j in range(size):
        temp.append(-1)
    evalpuzzle.append(temp)
            
evalpuzzle[0][0] = 0
showboard(evalpuzzle)

current = 0
done = False
temp = copyBoard(evalpuzzle)
print(temp)
while not done:
    temp2 = evaluateboard(b,copyBoard(temp),current,size)
    temp = copyBoard(temp2)
    temp3 = evaluateboard(b,copyBoard(temp),current+1,size)
    if temp2 == temp3:
        done = True
    else:
        temp = copyBoard(temp3)
        current += 2
evalpuzzle = temp
# evaluateboard(b, evalpuzzle, 0, size)
# evaluateboard(b,evalpuzzle,1,size)
# evaluateboard(b,evalpuzzle,2,size)
# evaluateboard(b,evalpuzzle,3,size)
showboard(temp2)
# temp = evalpuzzle
# current = 0
# while not evaluateboard(b, temp, current, size) != evalpuzzle:
#     evalpuzzle = evaluateboard(b, evalpuzzle, current, size)
#     temp = evalpuzzle
#     current += 1
    
# showboard(evalpuzzle)


# hill climbing# hill c 
def subtract(b):
    for x in range(size):
        for i in range (size):
            if b[x][i] > 4:
                b[x][i] = b [x][i] + 4
    return b
    
for x in range(500):
    
    new = initboard(size)
#     crate  the new eval board from while loop above this
    evalnew = []
#     initialize the eval board
    for i in range (size):
            temp = []
            for j in range(size):
                temp.append(-1)
                evalnew.append(temp)
            evalnew[0][0] = 0
            
    current = 0
    done = False
    temp = copyBoard(evalpuzzle)
    while not done:
        temp2 = evaluateboard(new, copyBoard(temp), current, size)
        temp = copyBoard(temp2)
        temp3 = evaluateboard(new, copyBoard(temp), current +1,  size)
        if temp2 == temp3:
            done = True
        else:
            temp = copyBoard(temp3)
        evalnew = copyBoard(temp)
    if evalpuzzle[size-1][size-1] < new [size-1][size-1]:
        evalpuzzle = copyBoard(evalnew)
        b = copyBoard(new)
        subtract(evalpuzzle)
showboard(b)
showboard(evalpuzzle)