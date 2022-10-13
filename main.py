# my program can be compiled and executed in linux os environment
# importing numpy library if it is not installed in your system i have given method in my readme file to install
import numpy as np


# Defining class node and inside it we are defining many functions
class Node:
    # After calling node class it will directly assign value of node with 3 parameters given below
    # Data, level and f value
    def __init__(self, data, level, fval):
        self.data = data
        self.level = level
        self.fval = fval

    def find(self, puz):
        # This function find will find the poaition of empty space in puzzle
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puz[i][j] == '_':
                    return i, j

    def copy(self, root):
        # This function will create a similar matrix of a given node
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def move(self, puz, x1, y1, x2, y2):
        # Given initial position x1 y1 it will move the puzzle to x2 y2 given that it is possible
        # If not possible then return none
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

    def generate_child(self):
        # This function will return all the possible children node of a given state
        x, y = self.find(self.data)
        # valid_list contains 4 directions [up,down,left,right] respectively.
        valid_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []
        for i in valid_list:
            child = self.move(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level + 1, 0)
                children.append(child_node)
        return children  # function returning all possible children node


# Defining a class named Puzzle and putting various functions inside it
class Puzzle:
    def __init__(self, dimension):
        # calling this class 'Puzzle' the dimension will be stored into respective variable and 2 empty arrays will be
        # created
        self.n = dimension
        self.open = []
        self.closed = []

    def takeinput(self):
        # This function will accept input from user and store it in the form of 2D array
        puz = []
        for i in range(0, self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def difference(self, start, goal):
        # This function calculates difference between given state and the goal state
        temp = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp

    def f(self, start, goal):
        # Heuristic function to calculate Heuristic value f = difference + level of current state
        return self.difference(start.data, goal) + start.level

    def getinvcount(self, start):
        # This function is basically made to check whether a puzzle can reach the goal or not
        # if 'getinvcount' returns an even number then we can reach the goal matrix else not
        # Description on inversion count is given in my readme file
        inv_count = 0
        empty_value = '_'
        new_array = np.array(start)  # using numpy function to convert 2d array into 1d array for evaluating invcount
        modified_array = new_array.flatten()  # here my 2d array is converted into 1d array and stored in new variable
        for i in range(0, 9):
            for j in range(i + 1, 9):
                if modified_array[j] != empty_value and modified_array[i] != empty_value and int(
                        modified_array[i]) > int(modified_array[j]):
                    inv_count += 1
        return inv_count

    def process(self):
        # Taking input from user and storing it in start and initializing goal matrix
        print("enter the puzzle problem \n")
        start = self.takeinput()
        print("enter the goal you want \n")
        goal = self.takeinput()
        goal1 = goal #just making a copy of goal variable so to convernt it into a node and apply my inversion count fucntion
        start = Node(start, 0, 0)
        goal1 = Node(goal1, 0, 0)
        start.fval = self.f(start, goal)  # initializing the f value of the starting puzzle
        goal1.fval = self.f(goal1, goal)
        self.open.append(start)  # now we are putting the start node in the self.open list which we created before
        self.closed.append(goal1)
        cur1 = self.closed[0]
        print("\n\n")
        steps = 0  # Created a steps variable to keep track on how many steps are taken to solve the problem

        while True:
            # This is just printing the puzzle in a matrix format

            cur = self.open[0]
            print("==================================================\n")
            for i in cur.data:
                for j in i:
                    print(j, end=" ")
                print("")

            # This is inversion count if statement which i have explained in my readme file briefly
            if (self.getinvcount(cur.data) % 2 != 0 and self.getinvcount(cur1.data) % 2 == 0) or (self.getinvcount(cur.data) % 2 == 0 and self.getinvcount(cur1.data) % 2 != 0):
                print("This puzzle cannot be solved")
                break

            if steps > 50000:
                print("This problem can be solved but it will take more than 50000 steps")
                break
            # If difference between my current and goal state is 0 then it will break the while loop and print
            if self.difference(cur.data, goal) == 0:
                print("==================================================\n")
                print("It took my program " + str(steps) + " steps to solve this puzzle")
                break

            # Now both of the if condition are not true then it will append all child of current state in self.open list
            for i in cur.generate_child():
                i.fval = self.f(i, goal)
                self.open.append(i)

            # Now deleting first element of self.open because it was the current state and we want all child nodes of
            # current state not current node itself in self.open list because we are sorting self.open in the next step
            del self.open[0]
            # sort the open list based on f value, such that child node with least f value can be processed further
            self.open.sort(key=lambda x: x.fval, reverse=False)
            # incrementing steps
            steps = steps + 1


# creating a puzzle varibale and storing class Puzzle in it with given dimension 3
puzzle = Puzzle(3)
# starting the process by calling the function process
puzzle.process()
