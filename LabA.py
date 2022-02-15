from posixpath import split
import numpy as np
from numpy import array


def print_maze(file):
    read_file=open(file, "r")
    lines=read_file.readlines()
    width=len(lines[0])-1 #-1 for new line
    height=len(lines)
    for line in lines:
        print(line)

def init_maze(file):
    read_file=open(file, "r")
    lines=read_file.readlines()
    width=len(lines[0])-1 #-1 for new line
    height=len(lines)
    print("Width of maze: "+str(width)+" Height of maze: "+str(height))
    maze_arr=[]
    for line in lines:
        row=[]
        
        split_str=line.split("\n")
        row.append(list(split_str[0]))
        maze_arr.append(row)
    numpy_maze = np.array(maze_arr)
    mouse_location=np.where(numpy_maze=="P")
    cheese_location=np.where(numpy_maze==".")
    print(mouse_location)
    print(cheese_location)

init_maze("/Users/egray/Desktop/SCHOOL2022/AI/1prize-medium.txt")
#print_maze("/Users/egray/Desktop/SCHOOL2022/AI/1prize-medium.txt")

