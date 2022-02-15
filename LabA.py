from posixpath import split


class Mouse:
    mouse_pos=(0,0)
    cheese_locations=[]
    maze_arr=[]
    initial_state=None
    class State:
        def __init__(self, location, cheese_list, action, steps):
            self.location = location
            self.cheese_list = cheese_list
            self.action = action
            self.steps = steps
            
        def print_state(self):
            print("Location: " + location)
            print("Cheese list: " + cheese_list)
            print("Action: " + action)
        

        def transition (current_state, action):
            if action == "n":
                new_location=(current_state.location[0], current_state.location[0]-1)
            elif action == "e":
                new_location=(current_state.location[0]+1, current_state.location[0])
            elif action == "w":
                new_location=(current_state.location[0]-1, current_state.location[0])
            elif action == "s":
                new_location=(current_state.location[0], current_state.location[0]+1)
            else:
                raise ValueError("Action is not possible.")
            new_cheese_list=copy.deepcopy(current_state.cheese_list)
            for i in range(len(new_cheese_list)):
                if new_location==new_cheese_list[i]:
                    del new_cheese_list[i] #remove cheese from new list
            return State(new_location, new_cheese_list, action, current_state.steps+1)


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
            for item in lists:
                if(item=="."):
                    print("CHEESE FOUND!!!")
                    cheese_location=(lists.index(item), row_index)
                    self.cheese_locations.append(cheese_location)
                if(item=="P"):
                    print("MOUSE FOUND!!!")
                    self.mouse_pos=(lists.index(item), row_index)
            row_index+=1

        print("Mouse: "+str(self.mouse_pos))
        print(cheese_location)
        initial_state= Mouse.State(self.mouse_pos, self.cheese_locations, None, 0)



    def Goal_Test(self, state):
        if state.cheese_list:
        #if cheese remaining in list
            return False
        else:
        #otherwise, return true
            return True


test=Mouse()
test.init_maze("/Users/egray/Desktop/SCHOOL2022/AI/1prize-medium.txt")
#print_maze("/Users/egray/Desktop/SCHOOL2022/AI/1prize-medium.txt")

