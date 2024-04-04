import random

print("Welcome to BlackJack!") 

def print_large_card(suit, rank):
    """Displays a single stylized card"""
    print("┌─────────┐")
    print(f"│{rank}       │")  # Top line with rank
    print("│         │")
    print(f"│    {suit}    │")  # Center with suit symbol
    print("│         │")
    print(f"│       {rank}│")  # Bottom line with rank
    print("└─────────┘")

# Example: Display two large cards
print_large_card("♦", "J")  # Example: Jack of Diamonds
print_large_card("♣", "A")  # Example: Ace of Clubs


card_options = "1,2,3,4,5,6,7,8,9,J,Q,K,A"  # J=Jack, Q=Queen, K=King, A=Ace

def starting_round(num_cards=1): 
    """Deals specified number of cards to a player."""
    cards = card_options.split(",")
    random.shuffle(cards)
    return cards[:num_cards]

def calculate_score(cards):
    """Calculates the score of a given hand."""
    score = 0
    has_ace = False
    for card in cards:
        if card in ["J", "Q", "K"]:
            score += 10
        elif card == "A":
            has_ace = True
            score += 11 
        else:
            score += int(card)

    # Adjust for ace if score exceeds 21
    if has_ace and score > 21:
        score -= 10

    return score

def print_round_results(player, cards, score):
    """Prints the current hand and score for a player"""
    print(f"{player}'s cards: {cards}")
    print(f"{player}'s score: {score}")

def game():
    """Plays a single round of Blackjack"""
    starting_cards_user = starting_round(num_cards=2)  
    starting_cards_computer = starting_round(num_cards=2) 

    user_score = calculate_score(starting_cards_user)
    computer_score = calculate_score(starting_cards_computer)

    print_round_results("You", starting_cards_user, user_score)
    print_round_results("Computer", starting_cards_computer[:1], "?")  # Hide computer's second card

    # User's turn
    while True:
        hit = input("Do you want another card? (y/n): ")
        if hit == "n":
            break

        starting_cards_user.extend(starting_round())
        user_score = calculate_score(starting_cards_user)
        print_round_results("You", starting_cards_user, user_score)

        if user_score > 22:
            print("You busted! Computer wins.")
            return

    # Computer's turn
    print("Computer's turn:")  
    while computer_score < 17:
        starting_cards_computer.extend(starting_round())
        computer_score = calculate_score(starting_cards_computer)

    print_round_results("Computer", starting_cards_computer, computer_score)  # Reveal all computer cards

    if computer_score > 21:
        print("Computer busted! You win.")
    elif user_score > 21: 
        print("You busted! Computer wins.")
    elif user_score == computer_score:
        print("It's a tie!")
    elif user_score > computer_score:  # User wins with higher score
        print("You win!")
    else:  # Computer wins by default in remaining cases
        print("Computer wins.") 


if __name__ == "__main__":
    while True:
        play_game = input("Do you want to play Blackjack? (y/n): ")
        if play_game == "n":
            break

        game()
