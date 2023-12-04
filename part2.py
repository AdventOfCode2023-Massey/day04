# Advent of Code 2023 Day 4 Part 2
# Code by Github Copilot Chat
# Editing by Bart Massey

import sys
from collections import deque

# Function to calculate the number of matches between winning numbers and your numbers
def calculate_matches(winning_numbers, your_numbers):
    return len([num for num in your_numbers if num in winning_numbers])

def main():
    filename = sys.argv[1]  # Get the filename from the command line arguments
    cards = []  # Initialize an empty list to store the cards

    # Open the file and read its contents
    with open(filename, 'r') as file:
        for line in file:
            _, numbers = line.split(':')  # Split the line into card number and numbers
            winning_numbers, your_numbers = numbers.split('|')  # Split the numbers into winning numbers and your numbers
            winning_numbers = set(map(int, winning_numbers.split()))  # Convert the winning numbers to a set of integers
            your_numbers = list(map(int, your_numbers.split()))  # Convert your numbers to a list of integers
            cards.append((winning_numbers, your_numbers))  # Add the card to the list of cards

    queue = deque(cards)  # Initialize a queue with the original cards
    total_cards = len(cards)  # Initialize the total count of cards with the number of original cards

    # While the queue is not empty
    while queue:
        # Remove a card from the queue
        winning_numbers, your_numbers = queue.popleft()

        # Calculate the number of matches the card has
        matches = calculate_matches(winning_numbers, your_numbers)

        # For each match, if there are cards left in the queue
        for _ in range(matches):
            if queue:  # if there are cards left in the queue
                queue.append(queue[0])  # copy the next card
                total_cards += 1  # Increase the total count by 1

    print(total_cards)  # Print the total count of cards

if __name__ == "__main__":
    main()
