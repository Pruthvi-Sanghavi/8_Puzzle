# ENPM - 661 Planning for Autonomous Robots
## Project 1: 8 Puzzle Solver
This 8-Puzzle problem is solved used BFS (BREADTH FIRST SEARCH) strategy.

### Dependencies

- Numpy [link](https://scipy.org/install.html)
- Command given below can be used for installation in Ubuntu. 
```
sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
``` 

### Cloning and Running Instructions
- On Ubuntu, open a terminal and type the following commands
```
git clone https://github.com/Pruthvi-Sanghavi/8_Puzzle.git
cd 8_Puzzle
python execute.py
```
### Remarks
- Here I have separated the code into two python files - ```execute.py``` and ```puzzle_solver.py```. 
- ```puzzle_solver.py``` contains all the functions defined for the solution of the puzzle.
- ```execute.py``` contains the code necessary for execution.

### Demo
```
pruthvi@pruthvi:~/Documents/ENPM 661/Project_1$ python execute.py 
Type numbers from 1 to 8 (Gets printed row-wise)
Element 1: 1
Element 2: 3
Element 3: 2
Element 4: 4
Element 5: 5
Element 6: 6
Element 7: 8
Element 8: 7
Element 9: 0
The start state is: 
[[ 1.  3.  2.]
 [ 4.  5.  6.]
 [ 8.  7.  0.]]
The goal state is: 
[[1 2 3]
 [4 5 6]
 [7 8 0]]
Solvable
Searching the tree
Goal_achieved
Move : None

Result : 

[[ 1.  3.  2.]
 [ 4.  5.  6.]
 [ 8.  7.  0.]]

level:0
Move : up

Result : 

[[ 1.  3.  2.]
 [ 4.  5.  0.]
 [ 8.  7.  6.]]

level:1
Move : up

Result : 

[[ 1.  3.  0.]
 [ 4.  5.  2.]
 [ 8.  7.  6.]]

level:4
Move : left

Result : 

[[ 1.  0.  3.]
 [ 4.  5.  2.]
 [ 8.  7.  6.]]

level:10
Move : left

Result : 

[[ 0.  1.  3.]
 [ 4.  5.  2.]
 [ 8.  7.  6.]]

level:22
Move : down

Result : 

[[ 4.  1.  3.]
 [ 0.  5.  2.]
 [ 8.  7.  6.]]

level:49
Move : right

Result : 

[[ 4.  1.  3.]
 [ 5.  0.  2.]
 [ 8.  7.  6.]]

level:92
Move : down

Result : 

[[ 4.  1.  3.]
 [ 5.  7.  2.]
 [ 8.  0.  6.]]

level:155
Move : left

Result : 

[[ 4.  1.  3.]
 [ 5.  7.  2.]
 [ 0.  8.  6.]]

level:267
Move : up

Result : 

[[ 4.  1.  3.]
 [ 0.  7.  2.]
 [ 5.  8.  6.]]

level:469
Move : right

Result : 

[[ 4.  1.  3.]
 [ 7.  0.  2.]
 [ 5.  8.  6.]]

level:788
Move : right

Result : 

[[ 4.  1.  3.]
 [ 7.  2.  0.]
 [ 5.  8.  6.]]

level:1276
Move : down

Result : 

[[ 4.  1.  3.]
 [ 7.  2.  6.]
 [ 5.  8.  0.]]

level:2060
Move : left

Result : 

[[ 4.  1.  3.]
 [ 7.  2.  6.]
 [ 5.  0.  8.]]

level:3354
Move : left

Result : 

[[ 4.  1.  3.]
 [ 7.  2.  6.]
 [ 0.  5.  8.]]

level:5420
Move : up

Result : 

[[ 4.  1.  3.]
 [ 0.  2.  6.]
 [ 7.  5.  8.]]

level:8743
Move : up

Result : 

[[ 0.  1.  3.]
 [ 4.  2.  6.]
 [ 7.  5.  8.]]

level:13907
Move : right

Result : 

[[ 1.  0.  3.]
 [ 4.  2.  6.]
 [ 7.  5.  8.]]

level:22068
Move : down

Result : 

[[ 1.  2.  3.]
 [ 4.  0.  6.]
 [ 7.  5.  8.]]

level:34167
Move : down

Result : 

[[ 1.  2.  3.]
 [ 4.  5.  6.]
 [ 7.  0.  8.]]

level:52335
Move : right

Result : 

[[ 1.  2.  3.]
 [ 4.  5.  6.]
 [ 7.  8.  0.]]

level:77488
```
