import os
def read_inputs():
    with open(os.path.abspath("./input/called_numbers.csv"), newline='') as f:
        called_numbers = f.readlines()[0].split(",")
    called_numbers = [int(c) for c in called_numbers]
        
    with open(os.path.abspath("./input/boards.txt"), newline="\n") as f:
        boards_raw = f.read().splitlines()
        
    boards = []
    board_being_built = [] # will be a list of lists, each sub-list is a row
    for row in boards_raw:
        row = [int(c) for c in row.split() if c.isdigit()]
        
        if len(row) > 0: #blank rows are the spacers between boards
            board_being_built.append(row)
        else:
            boards.append(board_being_built)
            board_being_built = []
            
    boards.append(board_being_built) #get the last board
    return boards, called_numbers
    
def main(boards, called_numbers):
    winners = {}
    # for each boards, determine if it gets bingo
    for board in boards: #board is a 2D array, list of lists board[row][column]
        score, idx = best_score_for_board(board, called_numbers)
        
        if idx in winners:
            winners[idx] = max(score, winners[idx])
        else:
            winners[idx] = score


    best_score = winners[min(winners)]
    print(f"the best score for this exercise is {best_score}")
    return winners

def best_score_for_board(board, called_numbers):
    potential_bingo = []   
    for idx in range(5,len(called_numbers)): #pull a bingo ball, only need to start checking for winners after the first 5 are called
        potential_bingo = bingo_check(board, called_numbers[:idx])
        # if it gets bingo, how many numbers did it take to get bingo
        if len(potential_bingo) > 0: #bingo has been found
        # calculate board score
            unused_numbers = set()
            for row in board: unused_numbers.update(row)
            for winning_number in called_numbers[:idx]: unused_numbers.discard(winning_number)
            score = sum(unused_numbers) * called_numbers[idx-1]
            
            return score, idx
        
    return 0,float('inf')

def bingo_check(board, numbers_so_far):
    empty_bingo = [] #default state
    
    board_cols = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
    possible_bingos = board + board_cols
    for potential_bingo in possible_bingos:
        bingo_status = all([num in numbers_so_far for num in potential_bingo])
        if bingo_status:
            return potential_bingo
    
    return empty_bingo

if __name__ == '__main__':
    boards, called_numbers = read_inputs()

    winners = main(boards, called_numbers)