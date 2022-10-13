
# PROGRAMMING ASSIGNMENT 

----------commands for executing and compiling the program are given at the end ------------

 # QUESTION 2

 1. The basic logic of my program is that first it takes the inital state matrix as input and goal state matrix as input now it creates all possible childs of the given matrix, here child means that we move the blank character ```_``` to all possible positions[ up,down,left ,right ], the new matrix formed is called child of the present matrix

 2. Now we compare all childs and find the one which has the minimum ```f value``` the one child which has the minimum f value gets printed.

 3. Now this loop goes on, we print the child which has least f value and after taking that child we take it's all possible children and do the same.

 4. when we go from one child to it's child our ```level``` increases 1.

 5. This loop goes on until we reach our goal node. If goal node is not reachable it will print ```goal not reachable``` and it will print all the states until my steps are less than 50000 if puzzle is solveable but the steps required are more than 50000 then it will print solveable and all the states less than 50000

 6. The ```difference``` between goal matrix and current matrix is given by my difference function

 7. So f value is defined as ```f value = level + difference``` 

 8. Now ```inversion count``` is defined as - A pair of tiles form an inversion if the values on tiles are in reverse order of their appearance in goal state.

 9. We find the inversion count of inital matrix and goal matrix using my ```getinvcount``` function. If inversion count of inital,goal matrix is even,odd or odd,even then the goal is reachable else the goal is not reachable

10. Finally i use my ```Puzzle``` class and put dimension as 3 and store it in variable named puzzle and puzzle.process() will start the process.There are classes and functions in my code which i have defined in comments of the code.

11. For running program type ```python3 main.py``` or ```python main.py```

12. Input should be given in the format
``` 
enter the puzzle problem

1 2 3
8 _ 3
7 6 5

enter the goal you want

2 8 1
_ 4 3
7 6 5

```
    

13. NOTE - I have used numpy library in my python code.To make sure this code runs install numpy first by typing 
```sudo apt install python3-numpy``` or ```sudo apt install python``` in terminal. After installing this you can run the program.
 




