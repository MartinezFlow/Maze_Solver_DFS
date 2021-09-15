from numpy import *
import numpy as np

def mazeSolver(start, end, maze):
    right_way.append(start)
    current_pos = start

    y, x = maze.shape
    print(y, x)
    #end = np.where(matrix3 == 'E')
    solutionFound = False

    while solutionFound == False:
        obstructed = 0

        possible_pos = [
                        (current_pos[0] - 1, current_pos[1]), #up
                        (current_pos[0], current_pos[1] + 1), #right
                        (current_pos[0] + 1, current_pos[1]), #down
                        (current_pos[0], current_pos[1] - 1)  #left
                        ]

        print(right_way)
        print(current_pos)
        for pos in possible_pos:
            if pos == end:
                for path in right_way:
                    maze[path] = 'x'
                print("Path Found!")
                print(maze)
                return solutionFound == True
            if pos[0] < 0 or pos[1] < 0 or pos[0] > (y - 1) or pos[1] > (x - 1):
                print("out of bounds")
                obstructed += 1
                continue
            if maze[pos] == '*':
                print("blocked")
                obstructed += 1
                continue
            if pos in traversed:
                print("been here")
                obstructed += 1
                continue
            else:
                break

        if obstructed == 4:
            right_way.pop()
            current_pos = right_way[-1]
            print(current_pos)
        else:
            current_pos = pos
            traversed.append(pos)
            right_way.append(pos)
            for path in right_way:
                maze[path] = 'o'
                print(maze, end='\n\n')


            #else:
                #right_way.pop()
                #mazeSolver(current_pos, maze)

maze0 = array([
    ["*", " ", "*", " ", " ", "*", "*", "E"],
    [" ", " ", "*", " ", "*", "*", " ", " "],
    [" ", "*", "*", " ", "*", "*", " ", "*"],
    [" ", "*", "*", " ", " ", "*", " ", "*"],
    [" ", "*", "*", "*", " ", "*", " ", "*"],
    [" ", " ", "*", "*", " ", "*", " ", " "],
    ["*", " ", " ", " ", " ", " ", "*", " "],
    ["S", " ", "*", "*", "*", " ", " ", " "]
])

maze1 = array([
    [" ", " ", "*", "E"],
    [" ", "*", " ", " "],
    [" ", "*", " ", "*"],
    [" ", "*", " ", "*"],
    [" ", "*", " ", "*"],
    [" ", " ", " ", "*"],
    ["*", " ", "*", " "],
    ["S", " ", "*", "*"]
])

maze2 = array([
    ["*", " ", "E"],
    [" ", "*", " "],
    ["S", " ", " "]
    ])

maze3 = array([
    ["*", "*", "*", "E"],
    [" ", "*", "*", " "],
    [" ", " ", "*", " "],
    ["S", " ", " ", " "]
])

#maze as a matrix
matrix0 = matrix(maze0)
matrix1 = matrix(maze1)
matrix2 = matrix(maze2)
matrix3 = matrix(maze3)

traversed = []
right_way = []


    #setting up the staring line
start = np.where(matrix0 == 'S')
end = np.where(matrix0 == 'E')
print(start,end)

for x in maze2:
    for y in x:
        if y == '*':
            print(y)


mazeSolver(start, end, maze0)
