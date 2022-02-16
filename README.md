# Lab A - Part 1  
*Egan White and Katrina Ziebarth*  
## LabA.py  
This file contains all of our code for part 1 of the lab. The classes, functions, and methods are as follows. All are contained within the class Mouse:  
**Mouse class**  
	An overarching class which contains all functions and all other classes. It stores a representation of the maze.  
State class
	A class which stores location, cheese_list, action, steps, and parent, all of which its constructor takes as parameters.  
print_state (method of State class):  
	A simple function that prints the location of the mouse, the location of the cheese/s (in array format) and action taken. This is useful for when we want to test our transition functions.  

transition (method of Mouse class):
Parameters:
1: current_state- Current (x,y) position of mouse
2: action- Expressed in either string format as either “n”, ”s”, “e”, “w”, describing which direction we want the mouse to move.

Our transition method is used to change location of our mouse. We use conditional statements to read our action string into deincremententing or incrementing the (x,y) position of our mouse. Because the top left corner of our map will be (0,0), in order to move up, we would decrement our Y position by 1. If we want to move down, we increment Y position by 1. If we want to move right, we increment X position by 1, and if we want to move left we deincremenet our X position by 1. We also have a final else statement that throws a value error if we are given an action other than “n”, ”s”, “e”, “w”. This function automatically tests to see if mouse’s new (x, y) position is the same as any cheese’s (x, y) position, and removes cheese from list.

print_maze (method of Mouse class)
	A simple function to print a representation of the maze.

init_maze (method of Mouse class)
	A function which parses a text file into a maze representation and an initial state, both of which are stored in the Mouse class as maze_arr and initial_state.

goal_test (method of Mouse class)
	To see if goal test is complete, use if self.Goal_Test(state)==True.

End program with control + c (cmd+c for MacOS)