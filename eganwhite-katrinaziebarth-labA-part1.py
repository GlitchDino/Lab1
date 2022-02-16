
'''Egan White and Katrina Ziebarth
CS365 Lab A Part 1
eganwhite-katrinaziebarth-labA-part1.py'''
import copy
import argparse
import os.path
x="""
add future section to design document (should be clear you understand algorithms solidly)

run test function on several files

test on tools

check design document pdf name (eganwhite-katrinaziebarth-labA-part1-design.pdf)

make tar (tar cvf eganwhite-katrinaziebarth-labA-part1.tar <files>) (design, .py, README.md)

send tar to other person
"""
class Mouse:
    mouse_pos=(0,0)
    cheese_locations=[]
    #stores initial values for state attributes while parsing file
    maze_arr=[]
    initial_state=None
    class State:
        def __init__(self, location, cheese_list, action, steps, parent):
            self.location = location
            self.cheese_list = cheese_list
            self.action = action
            self.steps = steps
            self.parent = parent
            
        def print_state(self):
            print("Location: " + str(self.location))
            print("Cheese list: " + str(self.cheese_list))
            print("Action: " + str(self.action))
        

    def transition (self, current_state, action):
        if action == "n":
            new_location=(current_state.location[0], current_state.location[1]-1)
        elif action == "e":
            new_location=(current_state.location[0]+1, current_state.location[1])
        elif action == "w":
            new_location=(current_state.location[0]-1, current_state.location[1])
        elif action == "s":
            new_location=(current_state.location[0], current_state.location[1]+1)
        else:
            raise ValueError("Action is not possible.")
        new_cheese_list=copy.deepcopy(current_state.cheese_list)
        for i in range(len(new_cheese_list)):
            if new_location==new_cheese_list[i]:
                del new_cheese_list[i] #remove cheese from new list
                break
        return self.State(new_location, new_cheese_list, action, current_state.steps+1, current_state)


    def print_maze(self, file):
        read_file=open(file, "r")
        lines=read_file.readlines()
        width=len(lines[0])-1 #-1 for new line
        height=len(lines)
        for line in lines:
            print(line, end="")

    def init_maze(self, file): #initilizes maze into 2d array, gets (x, y) position of mouse and all cheeses.
        read_file=open(file, "r")
        lines=read_file.readlines()
        width=len(lines[0])-1 #-1 for new line
        height=len(lines)
        row_index=0
        print("Width of maze: "+str(width)+" Height of maze: "+str(height))

        for line in lines: #Creates 2D array for maze
            split_str=line.split("\n")
            self.maze_arr.append(list(split_str[0]))

        for lists in self.maze_arr: #finds location of mouse and cheese
            for i in range(len(lists)):
                if lists[i]==".":
                    print("CHEESE FOUND!!!")
                    cheese_location=(i, row_index)
                    self.cheese_locations.append(cheese_location)
                if(lists[i]=="P"):
                    print("MOUSE FOUND!!!")
                    self.mouse_pos=(i, row_index)
            row_index+=1

        print("Mouse: "+str(self.mouse_pos))
        print(cheese_location)
        self.initial_state= Mouse.State(self.mouse_pos, self.cheese_locations, None, 0, None)


    def test_movement(self, state):
        current_state=state
        while(1==1):
            print("Mouse position: \n")
            
            user_input=input("Which direction would you like to move? (n/s/e/w): ")
            current_state = self.transition(current_state, user_input)
            current_state.print_state()
            if self.goal_test(current_state)==True:
                print("All cheeses collected! Exiting...")
                return

            
            
        #print_state1
    def goal_test(self, state):
        if state.cheese_list:
        #if cheese remaining in list
            return False
        else:
        #otherwise, return true
            return True
    



#print_maze("/Users/egray/Desktop/SCHOOL2022/AI/1prize-medium.txt")
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help='input file path', type=str)
    arguments=parser.parse_args()
    if not os.path.exists(arguments.i):
        raise ValueError("File path is not valid.")
    test=Mouse()
    test.init_maze(arguments.i)
    test.test_movement(test.initial_state)