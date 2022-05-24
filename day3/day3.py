import os

def part1(bits):
    bit_tracker = {}
    for i in range(len(max(bits, key=len))): # create enough hashmap keys for the longest possible bit. not making any assumptions about uniformity
        bit_tracker[i] = 0 # init hashmap
    for num in bits:
        for idx in range(len(num)):
            bit_tracker[idx] += int(num[idx])
            
    gamma = ''.join([str(round(bit_tracker[key]/1000)) for key in bit_tracker])
    epsilon = ''.join(['1' if char == '0' else '0' for char in gamma])
    
    power_consumption = int(gamma, 2) * int(epsilon, 2)
    
    print(f"gamma is {gamma},\nepsilon is {epsilon},\npower consumption is {power_consumption}")
    
if __name__=='__main__':
    with open(os.path.abspath("./input/day3_input.txt")) as f:
        bits = f.read().splitlines()
    part1(bits)
