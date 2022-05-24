import os

def part1(instructions):
    direction_totals = {'down':0, 'forward':0, 'up':0}
    for instruction in instructions:
        direction, val = instruction.split(" ")
        direction_totals[direction] += int(val)

    final_x_position = direction_totals['forward']
    final_depth = direction_totals['down'] - direction_totals['up']
    print(f"part 1, final position (x, depth): ({final_x_position},{final_depth})")
    print(f"part 1, multiplied area is: {final_x_position*final_depth}")
    
def part2(instructions):
    x_position, depth_position, aim = [0]*3
    for instruction in instructions:
        direction, val = instruction.split(" ")
        val = int(val)
        if 'forward' in direction:
            x_position += val
            depth_position += aim*val
        elif 'down' in direction: aim += val
        elif 'up' in direction: aim -= val
            
    print(f"part 2, final position (x, depth): ({x_position},{depth_position})")
    print(f"part 2, multiplied area is: {x_position*depth_position}")

if __name__ =='__main__':
    with open(os.path.abspath(".\input\day2_input.txt")) as f:
        instructions = f.read().splitlines()
    part1(instructions)
    part2(instructions)