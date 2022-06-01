import os

def read_inputs(input_paths):
    with open(input_paths, newline="") as f:
        inputs = f.read().splitlines() #enters each line as an entry in a list, without \n char
    result = []
    for line in inputs:
        coord_string_list = line.split(' -> ') # splits the text input into a list of 2 strings, 'x1,y1' and 'x2,y2'
        print(coord_string_list)
        for coord_string in coord_string_list:
            coords = string_to_coord_list(coord_string)
            result.append(coords)


    #inputs = [c.split(' -> ') for c in inputs] # splits the text input into a list of 2 strings, 'x1,y1' and 'x2,y2' 
    #inputs = [string_to_coord_list(sub_point) for point in inputs]
    return result


def string_to_coord_list(to_convert):
    """convert from string to a list of ints"""
    return [int(c) for c in to_convert.split(',')]

def main(inputs):
    """determine how many points have at least 2 overlapping lines. Inputs are in the form of coordinate tuples that denote the beginning and end point of each line (x1,y1),(x2,y2)"""
    #print(inputs)

if __name__=="__main__":
    inputs = read_inputs(os.path.abspath("./input/day5_input.txt"))
    main(inputs)