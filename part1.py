# Advent of Code 2023 Day 4 Part 1
# Code by Github Copilot Chat
# Editing by Bart Massey

import sys

def calculate_score(winning_numbers, your_numbers):
    matches = [num for num in your_numbers if num in winning_numbers]
    if not matches:
        return 0
    else:
        return 2 ** (len(matches) - 1)

def main():
    filename = sys.argv[1]
    total_score = 0
    with open(filename, 'r') as file:
        for line in file:
            winning_numbers, your_numbers = line.split('|')
            winning_numbers = set(map(int, winning_numbers.split()))
            your_numbers = list(map(int, your_numbers.split()))
            total_score += calculate_score(winning_numbers, your_numbers)
    print(total_score)

if __name__ == "__main__":
    main()
