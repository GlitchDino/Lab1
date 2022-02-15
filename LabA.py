from posixpath import split
import numpy as np
class Mouse:
    mouse_pos=(0,0)
    cheese_location=[]

    def print_maze(self, file):
        read_file=open(file, "r")
        lines=read_file.readlines()
        width=len(lines[0])-1 #-1 for new line
        height=len(lines)
        for line in lines:
            print(line)

    def init_maze(self, file):
        read_file=open(file, "r")
        lines=read_file.readlines()
        width=len(lines[0])-1 #-1 for new line
        height=len(lines)
        print("Width of maze: "+str(width)+" Height of maze: "+str(height))
        maze_arr=[]
        row_index=0

        for line in lines:
            row=[]
            split_str=line.split("\n")
            row.append(list(split_str[0]))
            maze_arr.append(row)
            if "." in row:
                print("WOOP")
            #for character in row:
            #    if character=='.':
            #        print("CHEESE FOUND!!!")
            row_index+=1
        numpy_maze = np.array(maze_arr)
        mouse_location=np.where(numpy_maze=="P")
        cheese_location=np.where(numpy_maze==".") #Only manages location of 1 cheese
        print(mouse_location)
        self.mouse_pos=(mouse_location[0][0], mouse_location[2][0])
        print(self.mouse_pos)
        print(cheese_location)

test=Mouse()
test.init_maze("/Users/egray/Desktop/SCHOOL2022/AI/1prize-medium.txt")
#print_maze("/Users/egray/Desktop/SCHOOL2022/AI/1prize-medium.txt")

