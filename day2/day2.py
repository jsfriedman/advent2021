import os

def part1(instructions):
    direction_totals = {'down':0, 'forward':0, 'up':0}
    for instruction in instructions:
        direction, val = instruction.split(" ")
        direction_totals[direction] += int(val)

    final_x_position = direction_totals['forward']
    final_depth = direction_totals['down'] - direction_totals['up']
    print(f"final position (x, depth): ({final_x_position},{final_depth})")
    print(f"multiplied area is: {final_x_position*final_depth}")

if __name__ =='__main__':
    with open(os.path.abspath(".\input\day2_input.txt")) as f:
        instructions = f.read().splitlines()
    part1(instructions)