from posixpath import split
import numpy as np
class Mouse:
    mouse_pos=(0,0)
    cheese_locations=[]
    maze_arr=[]

    def print_maze(self, file):
        read_file=open(file, "r")
        lines=read_file.readlines()
        width=len(lines[0])-1 #-1 for new line
        height=len(lines)
        for line in lines:
            print(line)

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

test=Mouse()
test.init_maze("/Users/egray/Desktop/SCHOOL2022/AI/1prize-medium.txt")
#print_maze("/Users/egray/Desktop/SCHOOL2022/AI/1prize-medium.txt")

