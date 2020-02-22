# ENPM 661 Planning for Autonomous Robots 
# Project-1 : 8 Puzzle Problem
# Author: Pruthvikumar Sanghavi; UID: 116951005.

#!/usr/bin/env python
from puzzle_solver import Node
from puzzle_solver import start_state
from puzzle_solver import search_tile
from puzzle_solver import left
from puzzle_solver import right
from puzzle_solver import up
from puzzle_solver import down
from puzzle_solver import move_tile
from puzzle_solver import print_states
from puzzle_solver import node_path
from puzzle_solver import node_searched
from puzzle_solver import node_info
from puzzle_solver import path
from puzzle_solver import searching_nodes
from puzzle_solver import repetition_check
from puzzle_solver import solvability_check

t = start_state()

repetition_check(t)
solvability_check(t)

base = Node(0, t, None, None, 0)


goal, p, q = searching_nodes(base)

if goal is None and p is None and q is None:
    print("Goal State could not be reached, Sorry")
else:
    print_states(path(goal))
    node_path(path(goal))
    node_searched(p)
    node_info(q)
