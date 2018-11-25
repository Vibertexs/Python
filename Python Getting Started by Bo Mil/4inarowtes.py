grid1 = [0,0,0,0,0,0,0] #This is the top row   
grid2 = [0,0,0,0,0,0,0]
grid3 = [0,0,0,0,0,0,0]
grid4 = [0,0,0,0,0,0,0]
grid5 = [0,0,0,0,0,0,0]
grid6 = [0,0,0,0,0,0,0] # This is the bottom row

gridSen = ["Bilal", "is", "a", "boy"] # This is the bottom row

print("Player one is represented as 'x' while player two is represented as 'o'")

def printGrid():
    print("", grid1, "\n", grid2, "\n", grid3, "\n", grid4, "\n", grid5, "\n", grid6, "\n", gridSen)


a = 0
for i in grid1:
    
    print(i)
    if i == 0:
        grid1[a] = "+"
    # grid1 = grid1
    str(grid1).replace(",", " ")
    a = a + 1

a = 0
comSen = ""
for i in gridSen:
    
    print(i)
    if i == 0:
        comSen = comSen + gridSen[a]
    a = a + 1


print(comSen)
printGrid()
# s = 'Foo, bar'
# s.replace(',',' ')
# print(s)