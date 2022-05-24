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
    
def part2(bits):
    #find oxygen generator rating
    remaining_bits = bits.copy()
    for i in range(len(max(bits, key=len))):
        #identify most popular bit
        most_popular_bit = find_most_popular_bit(remaining_bits, i)
        #prune list
        if len(remaining_bits) > 1:
            remaining_bits = [num for num in remaining_bits if most_popular_bit in num[i]]
        
    oxygen_generator_rating = remaining_bits[0]
    
    remaining_bits = bits.copy()
    for i in range(len(max(bits, key=len))):
        most_popular_bit = find_most_popular_bit(remaining_bits, i)
        if len(remaining_bits) > 1:
            remaining_bits = [num for num in remaining_bits if most_popular_bit not in num[i]]
    #find CO2 scrubber rating
    
    co2_scrubber_rating = remaining_bits[0]
    
    life_support_rating = int(oxygen_generator_rating,  2) * int(co2_scrubber_rating, 2)
    
    print(f"life support rating is {life_support_rating}")
    
def find_most_popular_bit(remaining_bits, idx):
    total = 0
    for num in remaining_bits:
        total += int(num[idx])
    
    if (total/len(remaining_bits)) == 0.5:
        most_popular_bit = '1'
    else:
        most_popular_bit = str(round(total/len(remaining_bits)))
    
    return most_popular_bit
    

if __name__=='__main__':
    with open(os.path.abspath("./input/day3_input.txt")) as f:
        bits = f.read().splitlines()
            
    part1(bits)
    part2(bits)