def part1(sonar_readings):
    with open(r"C:\Users\megap\Documents\Code\advent2021\input\day1_input.txt") as f:
        lines = f.read().splitlines()
    sonar_readings = [int(c) for c in lines]

    result = 0
    for idx in range(1,len(sonar_readings)):
        if sonar_readings[idx] > sonar_readings[idx-1]: result += 1

    print(f"part 1: number of increasing readings: {result}")


def part2(sonar_readings, window_size):
    result = 0
    for idx in range(1,len(sonar_readings)-window_size+1):
        previous_window_total = sum(sonar_readings[idx-1:idx+window_size-1])
        window_total = sum(sonar_readings[idx:idx+window_size])
        if window_total > previous_window_total: result += 1

    print(f"part 2: number of increasing readings with a window size of {window_size}: {result}")


if __name__=='__main__':
    with open(r"C:\Users\megap\Documents\Code\advent2021\input\day1_input.txt") as f:
        lines = f.read().splitlines()
    sonar_readings = [int(c) for c in lines]
    part1(sonar_readings)
    part2(sonar_readings, window_size=3)