import copy

#Setup Test Input
input = [[".", "*", "*", "."], ["*", "*", ".", "."], ["*", ".", "*", "*"], ["*", "*", "*", "*"]]
for i in range(len(input)):
    print(input[i])

#Set Dimensions
m = 4
n = 4
total = 0
def findwater(grid):
    if (grid is None or len(grid) == 0 or len(grid[0]) == 0):
        return 0
    count = 0
    for i in range (0, m):
        for j in range(0, n):
            if (grid[i][j] == "."):
                checkarr = check(grid, i, j)
                if (checkarr):
                    surround = True
                    for dir in checkarr:
                        if (dir == 0):
                            surround = False
                            grid[i][j] = "X"
                            count+=1
                    if (surround):
                        grid[i][j] = "X"
                        count+=1        
    return count           
                    


def check(grid, i, j):
    if (i > 0 and i < m - 1 and j >0 and j< n -1):
        up = grid[i-1][j]
        right = grid[i][j+1]
        down = grid[i+1][j]
        left = grid[i][j-1]
        arr = [up, right, down, left]
        result = []
        for i in arr:
            if (i == "*"):
                result.append(1)
            else:
                result.append(0)
        return result
    else:
        return None

total = 0
def iterate():
    global total
    for i in range (0, m):
            for j in range(0, n):
                if (input[i][j] == "X"):
                    if (not checkleak(input, i, j)):
                        total +=1

def checkleak(grid, i, j):
    global total
    up = grid[i-1][j]
    right = grid[i][j+1]
    down = grid[i+1][j]
    left = grid[i][j-1]
    arr = [up, right, down, left]
    result = []
    leak = False
    for y in arr:
        if (y == "."):
            result.append(1)
        else:
            result.append(0)
    for x in result:
        if (x == 1):
            leak = True
            total -= 1
            grid[i][j] = "."
    return leak

findwater(input)
print(input)
cp = copy.deepcopy(input)
iterate()
while(cp != input):
    cp = copy.deepcopy(input)
    iterate()

ans = 0
for i in range (0, m):
            for j in range(0, n):
                if (input[i][j] == "X"):
                    ans += 1
print(ans)





