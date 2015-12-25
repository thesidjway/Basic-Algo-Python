# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

from operator import itemgetter

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
costa = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']
lister=[[0,0,0]] #[cost,y,x]


def update(grid,lister,init,delta):
    a=lister.pop()
    a_x=a.pop()
    a_y=a.pop()
    cost=a.pop()
    grid[0][0]=1
    for i in range(len(delta)):
        a_x1=a_x+delta[i][1]
        a_y1=a_y+delta[i][0]
        if a_x1>=0 and a_y1>=0 and a_x1<len(grid[1]) and a_y1<len(grid):
            if grid[a_y1][a_x1]==0:
                grid[a_y1][a_x1]=1
                lister.append([cost+1,a_y1,a_x1])

    
def search(grid,init,goal,costa,delta):
    while(grid[goal[0]][goal[1]]!=1):
        lister.sort(key=itemgetter(0),reverse=True)
        update(grid,lister,init,delta)
        print lister
        if len(lister)==0:
            print "fail"
            return 0
    return 0

search(grid,init,goal,costa,delta)
