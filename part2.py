# Advent of Code 2023 Day 4 Part 2
# Code by Github Copilot Chat
# Editing by Bart Massey

import sys
from collections import deque

def calculate_matches(winning_numbers, your_numbers):
    return len([num for num in your_numbers if num in winning_numbers])

def main():
    filename = sys.argv[1]
    cards = []
    with open(filename, 'r') as file:
        for line in file:
            _, numbers = line.split(':')
            winning_numbers, your_numbers = numbers.split('|')
            winning_numbers = set(map(int, winning_numbers.split()))
            your_numbers = list(map(int, your_numbers.split()))
            cards.append((winning_numbers, your_numbers))

    queue = deque(range(len(cards)))  # queue stores indices of cards
    total_cards = len(cards)

    while queue:
        card_index = queue.popleft()
        winning_numbers, your_numbers = cards[card_index]
        matches = calculate_matches(winning_numbers, your_numbers)

        # Add indices of the next cards to the queue
        for next_card_index in range(card_index + 1, min(card_index + 1 + matches, len(cards))):
            queue.append(next_card_index)
            total_cards += 1

    print(total_cards)

if __name__ == "__main__":
    main()
