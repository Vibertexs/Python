grid1 = [0,0,0,0,0,0,0] #This is the top row   
grid2 = [0,0,0,0,0,0,0]
grid3 = [0,0,0,0,0,0,0]
grid4 = [0,0,0,0,0,0,0]
grid5 = [0,0,0,0,0,0,0]
grid6 = [0,0,0,0,0,0,0] # This is the bottom row

print("Player one is represented as 'x' while player two is represented as 'o'")

def printGrid():
    print("", grid1, "\n", grid2, "\n", grid3, "\n", grid4, "\n", grid5, "\n", grid6)    
# printGrid()

a = 0
for i in grid1:
    if i == 0:
        grid1[a]  = " | - | "
        a+= 1


grid1str = str(grid1)
print(grid1str)
grid1str.replace(",", " ")
print(grid1str)