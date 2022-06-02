import os

def read_inputs(input_paths):
    with open(input_paths, newline="") as f:
        inputs = f.read().splitlines() #enters each line as an entry in a list, without \n char
    all_lines = []
    for line in inputs:
        this_line = []
        coord_string_list = line.split(' -> ') # splits the text input into a list of 2 strings, 'x1,y1' and 'x2,y2'
        for coord_string in coord_string_list:
            point = [int(c) for c in coord_string.split(',')] #converts from a string of 2 numbers to 2 ints "124,125" -> (124,125)
            this_line.append(point)
        all_lines.append(this_line)


    #inputs = [c.split(' -> ') for c in inputs] # splits the text input into a list of 2 strings, 'x1,y1' and 'x2,y2' 
    #inputs = [string_to_coord_list(sub_point) for point in inputs]
    return all_lines

def main(inputs):
    """determine how many points have at least 2 overlapping lines. Inputs are in the form of coordinate tuples that denote the beginning and end point of each line (x1,y1),(x2,y2)"""
    print(inputs)
    #init grid, hashmap
    grid = {}
    # for each line
        # initial coordinate
        # add 1 to total at coords
        # find 'next' coord based on lined

if __name__=="__main__":
    inputs = read_inputs(os.path.abspath("./input/day5_input.txt"))
    main(inputs)