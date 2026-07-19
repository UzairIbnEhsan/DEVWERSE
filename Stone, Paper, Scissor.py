# Step 1: Import the random module
# Why: This allows the computer to make random choices
import random

# Step 2: Define the main game function
# Why: Keeps our code organized and reusable
def rock_paper_scissor():
    
    # Step 3: Display welcome message
    # Why: Good user experience - tells the player how to play
    print("Welcome To Rock Paper Scissor By Uzair Ehsan")
    print("Rock beats Scissor")
    print("Paper beats Rock")
    print("Scissor beats Paper")
    print("Type 'end' at any time to exit the game")
    
    # Step 4: Create a list of valid choices
    # Why: Used for validation and random selection
    choices = ['rock', 'paper', 'scissor']
    
    # Step 5: Create a dictionary for win messages
    # Why: Shows descriptive messages for each win condition
    win_messages = {
        'rock': 'Rock smashes Scissor',
        'paper': 'Paper covers Rock',
        'scissor': 'Scissor cuts Paper'
    }
    
    # Step 6: Start the infinite game loop
    # Why: This keeps the game running until the player types 'end'
    while True:
        
        # Step 7: Get player's input
        # Why: We need to know what the player wants to play
        your_choice = input("\nEnter your move (Rock, Paper, Scissors) or type 'end' to stop: ")
        
        # Step 8: Check if player wants to exit
        # Why: This is the termination condition
        # Check for 'end' in any case (end, End, END)
        if your_choice == 'end':
            print("\nGame over. Thanks for playing!")
            break  # Exit the while loop completely
        
        # Step 9: Validate player's choice
        # Why: Make sure the player typed a valid move
        if your_choice not in choices:
            print("Invalid choice! Please enter Rock, Paper, or Scissor.")
            continue  # Skip to the next loop iteration
        
        # Step 10: Computer makes a random choice
        # Why: The computer needs to pick something to play against you
        # random.choice() picks a random item from the list
        computer_choice = random.choice(choices)
        
        # Step 11: Display both choices
        # Why: Player needs to see what both chose
        # .capitalize() makes first letter uppercase for display
        print(f"\nComputer chose: {computer_choice.capitalize()}")
        print(f"You chose: {your_choice.capitalize()}")
        
        # Step 12: Determine the winner using if/elif/else
        # Why: Need to decide who won this round
        
        # Case 1: Both chose the same thing (Tie)
        if your_choice == computer_choice:
            print("It's a tie!")
        
        # Case 2: Player wins
        # Why: Check if player's choice beats computer's choice
        elif (your_choice == 'rock' and computer_choice == 'scissor') or (your_choice == 'paper' and computer_choice == 'rock') or (your_choice == 'scissor' and computer_choice == 'paper'):
            
            # Show the win message with the action
            print(f"You win! {win_messages[your_choice]}.")
        
        # Case 3: Computer wins (everything else)
        else:
            # Show the loss message
            print(f"Computer wins! {win_messages[computer_choice]}.")

# Step 13: Run the game
# Why: This starts the game when you run the file directly
if __name__ == "__main__":
    rock_paper_scissor()