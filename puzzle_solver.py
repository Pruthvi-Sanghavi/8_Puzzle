# ENPM 661 Planning for Autonomous Robots 
# Project-1 : 8 Puzzle Problem
# Author: Pruthvikumar Sanghavi; UID: 116951005.

#!/usr/bin/env python 
# Importing the Libraries
import numpy as np                   									# Allows operations to be perfomed on arrays.                            
import os 																# Allows making changes on files.

class Node:
    def __init__(self, level, data, parent, act, cost):
        self.data = data
        self.parent = parent
        self.act = act
        self.level = level
        self.cost = cost

# Function that takes in the start state
def start_state():													
    print("Type numbers from 1 to 8 (Gets printed row-wise)")
    initial_state = np.zeros(9)											# Constructs a matrix / 2d array
    for i in range(9):													# Take the input 9 times.
        entries = int(input("Element " + str(i + 1) + ": "))			# Input entries
        if entries < 0 or entries > 8:									# Check: Entries should be numbers from 1 to 8.
            print("Insert numbers from 1 to 8")
            exit(0)
        else:
            initial_state[i] = np.array(entries)						# Stores the entry as the initial state
    print("The start state is: ")
    print(np.reshape(initial_state, (3,3)))								# Prints the initial state.
    goal_node = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    print("The goal state is: ")
    print(goal_node)
    return np.reshape(initial_state, (3, 3))							# returns the array aranged in 3x3 form.

# Function that declare the position of empty tile '0'
def search_tile(tile):
    i, j = np.where(tile == 0)											# (i,j) defines the empty tile position.
    i = int(i)															# declare i as an integer.
    j = int(j)															# declare j as an integer.
    return i, j															# returns the coordinate position puzz = (i,j) 

# Function that Searches for the tile on left
def left(data):
    i, j = search_tile(data)											# defines the current empty tile position
    if j == 0:															# checks for the tile coordinate
        return None                                                     # if tile has j as zero, movement on left is not possible
    else:
        pre_pos = np.copy(data)											# copies the present position from data to pre_pos
        pos = pre_pos[i, j - 1]											
        pre_pos[i, j] = pos 											# Switching the postion of the empty tile 
        pre_pos[i, j - 1] = 0											
        return pre_pos													# return the present position


def right(data):
    i, j = search_tile(data)											# defines the current empty tile position
    if j == 2:															# checks for the tile coordinate
        return None 													# if tile has j as 2, movement on left is not possible
    else:
        pre_pos = np.copy(data)											# copies the present position from data to pre_pos
        pos = pre_pos[i, j + 1]											
        pre_pos[i, j] = pos 											# Switching the postion of the empty tile 
        pre_pos[i, j + 1] = 0											
        return pre_pos													# return the present position


def up(data):
    i, j = search_tile(data)											# defines the current empty tile position
    if i == 0:															# checks for the tile coordinate
        return None 													# if tile has j as 2, movement on left is not possible
    else:
        pre_pos = np.copy(data)											# copies the present position from data to pre_pos
        pos = pre_pos[i - 1, j]											
        pre_pos[i, j] = pos 											# Switching the postion of the empty tile 
        pre_pos[i - 1, j] = 0											
        return pre_pos													# return the present position


def down(data):
    i, j = search_tile(data)											# defines the current empty tile position
    if i == 2:															# checks for the tile coordinate
        return None 													# if tile has j as 2, movement on left is not possible
    else:
        pre_pos = np.copy(data)											# copies the present position from data to pre_pos
        pos = pre_pos[i + 1, j]											
        pre_pos[i, j] = pos 											# Switching the postion of the empty tile 
        pre_pos[i + 1, j] = 0											
        return pre_pos													# return the present position

# Function that moves the tile
def move_tile(action, data):
    if action == 'up':													# move up using function up
        return up(data)
    if action == 'down':												# move down using function down
        return down(data)
    if action == 'left':												# move left using function left
        return left(data)							
    if action == 'right':												# move right using function right
        return right(data)
    else:
        return None 													# return none if no condition is satisfied


# Function that prints the output
def print_states(result): 
	
    for l in result:
        print("Move : " + str(l.act) + "\n" + "\n" + "Result : " + "\n" + "\n" + str(l.data) + "\n" + "\n" + "level:" + str(l.level))

# Function that prints the path file
def node_path(path):  
    if os.path.exists("Path_file.txt"):
        os.remove("Path_file.txt")

    f = open("Path_file.txt", "a")
    for node in path:
        if node.parent is not None:
            f.write(str(node.level) + "\t" + str(node.parent.level) + "\t" + str(node.cost) + "\n")
    f.close()

# Function that prints the node file
def node_searched(searched):  
    if os.path.exists("node.txt"):
        os.remove("node.txt")

    f = open("node.txt", "a")
    for element in searched:
        f.write('[')
        for i in range(len(element)):
            for j in range(len(element)):
                f.write(str(element[i][j]) + " ")
        f.write(']')
        f.write("\n")
        f.write("\n")
    f.close()

# Function that prints the node_info output file
def node_info(info):  
    if os.path.exists("info.txt"):
        os.remove("info.txt")

    f = open("info.txt", "a")
    for n in info:
        if n.parent is not None:
            f.write(str(n.level) + "\t" + str(n.parent.level) + "\t" + str(n.cost) + "\n")
    f.close()

# Function to search the path from goal node to the starting node
def path(node):  
    p = []  
    p.append(node)
    parent_node = node.parent
    while parent_node is not None:
        p.append(parent_node)
        parent_node = parent_node.parent
    return list(reversed(p))

# function that explores the tree
def searching_nodes(node):
    print("Searching the tree")
    actions = ["down", "up", "left", "right"]
    goal_node = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    node_q = [node]
    final_nodes = []
    info = []
    final_nodes.append(node_q[0].data.tolist())  
    node_counter = 0  

    while node_q:
        current_base = node_q.pop(0)  
        if current_base.data.tolist() == goal_node.tolist():
            print("Goal achieved")
            return current_base, final_nodes, info

        for move in actions:
            temp_data = move_tile(move, current_base.data)
            if temp_data is not None:
                node_counter += 1
                child_node = Node(node_counter, np.array(temp_data), current_base, move, 0)  

                if child_node.data.tolist() not in final_nodes:  
                    node_q.append(child_node)
                    final_nodes.append(child_node.data.tolist())
                    info.append(child_node)
                    if child_node.data.tolist() == goal_node.tolist():
                        print("Goal_achieved")
                        return child_node, final_nodes, info
    return None, None, None  

# Function that checks that no entry is repeated
def repetition_check(l):
    mat_1 = np.reshape(l, 9)
    for i in range(9):
        n = 0
        f = mat_1[i]
        for j in range(9):
            if f == mat_1[j]:
                n += 1
        if n >= 2:
            print("Repetition of number is not allowed")
            exit(0)


# Function that checks whether solution is possible is not
def solvability_check(g):
    mat_2 = np.reshape(g, 9)
    m = 0
    for i in range(9):
        if not mat_2[i] == 0:
            check = mat_2[i]
            for x in range(i + 1, 9):
                if check < mat_2[x] or mat_2[x] == 0:
                    continue
                else:
                    m += 1
    if m % 2 == 0:
        print("Solvable")
    else:
        print("Unsolvable")


