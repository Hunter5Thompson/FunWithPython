import random


ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
#suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

# Kartendeck erstellen
deck = []
for rank in ranks:
    card = {"rank": rank}


    deck.append(card)

# Karten austeilen
def deal_cards():
    player_hand = []
    dealer_hand = []

    # Zwei Karten an den Spieler
    player_hand.append(random.choice(deck))
    player_hand.append(random.choice(deck))

    # Zwei Karten an den Dealer, eine aufgedeckt, eine verdeckt
    dealer_hand.append(random.choice(deck))
    dealer_hand.append(random.choice(deck))

    return player_hand, dealer_hand

# Eine Karte des Dealers aufdecken
def show_one_card(dealer_hand):
    print("Dealer's Hand:")
    print(" <card hidden>")
    print("", dealer_hand[1])

# Karten des Spielers zeigen
def show_players_card(players_hand):
    print("Players Hand:")
    print(players_hand[0],players_hand[1])


def calculate_hand_value(hand):
    """Calculates the value of a given hand"""
    value = 0
    ace_count = 0
    for card in hand:
        if card["rank"] == "Jack" or card["rank"] == "Queen" or card["rank"] == "King":
            value += 10
        elif card["rank"] == "Two":
            value += 2
        elif card["rank"] == "Three":
            value += 3
        elif card["rank"] == "Four":
            value += 4
        elif card["rank"] == "Five":
            value += 5
        elif card["rank"] == "Six":
            value += 6
        elif card["rank"] == "Seven":
            value += 7
        elif card["rank"] == "Eight":
            value += 8
        elif card["rank"] == "Nine":
            value += 9
        elif card["rank"] == "Ten":
            value += 10
        elif card["rank"] == "Ace":
            ace_count += 1
            value += 11
        elif isinstance(card["rank"],int):
            value +=card["rank"]
        else:
            try:
                value += int(card["rank"])
            except ValueError:
                pass

    # Adjust for Aces
    while ace_count > 0 and value > 21:
        value -= 10
        ace_count -= 1

    # Check if the hand contains aces and the value is still greater than 21
    if ace_count > 0 and value > 21:
        value -= 10
        ace_count -= 1

    return value


# Karte dem Spieler hinzufügen
def player_hit(player_hand):
    player_hand.append(random.choice(deck))

# Karte dem Dealer hinzufügen
def dealer_hit(dealer_hand):
    dealer_hand.append(random.choice(deck))

# Spielzug des Spielers
def player_turn(player_hand):
    while True:
        decision = input("Do you want to hit or stand? ")
        if decision.lower() == "hit":
            player_hit(player_hand)
            print("Player's Hand:")
            for card in player_hand:
                print("", card["rank"])
            if calculate_hand_value(player_hand) > 21:
                print("Bust! You lose.")
                return False
        elif decision.lower() == "stand":
            return True
        else:
            print("Invalid input. Please enter 'hit' or 'stand'.")

def dealer_turn(dealer_hand):
    print("Dealer's Hand:")
    for card in dealer_hand:
        print("", card["rank"])
    while calculate_hand_value(dealer_hand) <= 16:
        print("Dealer hits.")
        dealer_hit(dealer_hand)
        print("Dealer's Hand:")
        for card in dealer_hand:
            print("", card["rank"])
    if calculate_hand_value(dealer_hand) > 21:
        print("Dealer busts. You win!")
        return False
    else:
        print("Dealer stands.")
        return True

# Gameloop
def play_game():
    while True:
        game_over = False
        while not game_over:
            # Deal cards
            player_hand, dealer_hand = deal_cards()

            # Show dealer's face-down card
            show_one_card(dealer_hand)
            # show players cards
            show_players_card(player_hand)

            # Player turn
            player_done = player_turn(player_hand)
            if not player_done:
                game_over = True
                continue

            # Dealer turn
            dealer_done = dealer_turn(dealer_hand)
            if not dealer_done:
                print("You win!")
            else:
                player_value = calculate_hand_value(player_hand)
                dealer_value = calculate_hand_value(dealer_hand)
                if player_value > dealer_value:
                    print("You win!")
                elif dealer_value > player_value:
                    print("Dealer wins.")
                else:
                    print("It's a tie!")

            # Ask player if they want to play again
            play_again = input("Do you want to play again? (y/n) ")
            if play_again.lower() != "y":
                game_over = True
                break
        if play_again.lower() !="y":
            break
    print("Pussy!")


play_game()


