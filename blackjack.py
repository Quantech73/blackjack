import random
suits = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
values = {'Ace': 11, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
bet = ('25', '50', '100', '500')
chip_values = {'25': 25, '50': 50, '100': 100, '500': 500}

class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal(self):
        return self.all_cards.pop()

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit

class Player:

    def __init__(self, name):
        self.player_name = name
        self.player_hand = []
        self.hand_value = 0
        
    def __str__(self):
        return self.player_name + "'s current hand is:"
    
    def show_hand(self, hand):
        print(*hand, sep=', ')

class Chip:
    def __init__(self, player_bet):
        self.bet_val = chip_values[player_bet]
        self.winnings = 0
    
    def __str__(self):
        return 'Your winnings are: ' + str(self.winnings)

def add_value(player):
    if player.player_hand[-1].rank == "Ace":
        print('Would you like your Ace to be 1 or 11?')
        reply = input()
        if reply == '1':
            player.hand_value += 1
        else:
            player.hand_value += 11
    else:
        player.hand_value += player.player_hand[-1].value

def display_hand_value(player):
    print(str(player.player_name) + "\'s current hand value is: " + str(player.hand_value))
    
# computer's turn
def comp_turn():
    print('\n' + "It is now bob\'s turn.")
    if bob.hand_value < 18 or player1.hand_value == 20:
        print("Bob draws a card.")
        bob.player_hand.append(deck1.deal())
        print('\n' + str(bob.player_name) + "\'s current hand is:")
        bob.show_hand(bob.player_hand)
        add_value(bob)
        display_hand_value(bob)
    else:
        print("Bob choses not to hit.")

def win(player):
    print('\n' + str(player.player_name) + " wins the game!")
    player_bet.winnings += player_bet.bet_val
    print('Total winnings: ' + '+' + str(player_bet.winnings))

def sudden_death():
    print('\n' + "!!!SUDDEN DEATH!!!")
    print("Each player will draw one additional card. The hand with the highest value wins!")
    # deal cards
    player1.player_hand.append(deck1.deal())
    bob.player_hand.append(deck1.deal())
    # show cards
    print('\n' + 'Your current hand is:')
    player1.show_hand(player1.player_hand)
    add_value(player1)
    display_hand_value(player1)
    
    print('\n' + str(bob.player_name) + "\'s current hand is:")
    bob.show_hand(bob.player_hand)
    add_value(bob)
    display_hand_value(bob)
    # check win condition
    if bob.hand_value > player1.hand_value:
        print('\n' + str(bob.player_name) + " wins the game!")
        player_bet.winnings -= player_bet.bet_val
        print('Total winnings: ' + str(player_bet.winnings))
    else:
        win(player1)

# Deck Creation
deck1 = Deck()
deck1.shuffle()
# control the flow of the game
play_again = True
game_on = True
#Welcome Page
print("~o~ WELCOME TO BLACKJACK! ~o~")
# player creation
player1 = Player(input("What is your player name: "))
# game loop
while play_again:
# bet input
    print('\n' + 'How much would you like to bet?')
    print('25, 50, 100, or 500')
    player_bet = Chip(input("Bet: "))
# deal two cards to player
    player1.player_hand.append(deck1.deal())
    player1.player_hand.append(deck1.deal())  
# show player's hand
    print('\n' + str(player1))
    player1.show_hand(player1.player_hand)   
# calculate and show total hand value
    for card in player1.player_hand:
        player1.hand_value += card.value
    display_hand_value(player1)
# computer creation
    bob = Player('Bob')
# deal two cards to computer
    bob.player_hand.append(deck1.deal())
    bob.player_hand.append(deck1.deal()) 
# show bob's hand
    print('\n' + str(bob))
    bob.show_hand(bob.player_hand)
# calculate and show total hand value
    for card in bob.player_hand:
        bob.hand_value += card.value
    display_hand_value(bob)
# check for blackjack hand
    if player1.hand_value == 21 and bob.hand_value < 21:
        win(player1)
# play again?
        print('\n' + "Would you like to play again?")
        user_input = input("Yes or No: ")
        if user_input.lower() == 'yes':
            continue
        else:
            break
    elif player1.hand_value < 21 and bob.hand_value == 21:
        win(bob)
# play again?
        print('\n' + "Would you like to play again?")
        user_input = input("Yes or No: ")
        if user_input.lower() == 'yes':
            continue
        else:
            break
    elif player1.hand_value == bob.hand_value:
        sudden_death()
# play again?
        print('\n' + "Would you like to play again?")
        user_input = input("Yes or No: ")
        if user_input.lower() == 'yes':
            continue
        else:
            play_again = False
            game_on = False   
    while game_on:
# player's turn to draw card
        print('\n' + 'Would you like to hit?')
        user_input = input("Yes or No: ")
        if user_input.lower() == 'yes':
            player1.player_hand.append(deck1.deal())
            print('\n' + 'Your current hand is:')
            player1.show_hand(player1.player_hand)
            add_value(player1)
            display_hand_value(player1)
# check win condition
            if player1.hand_value > 21:
                player_bet.winnings -= player_bet.bet_val
                print("You Lose!")
                print(str(player_bet.winnings))
                break
            if player1.hand_value == 21:
                win(player1)
                break
            continue
        elif user_input.lower() == 'no':
            print('Your turn ends here.')
# computer's turn
            comp_turn()
# check win condition
            if bob.hand_value > 21 or bob.hand_value < player1.hand_value:
                win(player1)
                break
            elif bob.hand_value == player1.hand_value:
                sudden_death()
                break
            else:
                print('\n' + str(bob.player_name) + " wins the game!")
                player_bet.winnings -= player_bet.bet_val
                print('Total winnings: ' + str(player_bet.winnings))
                break
        else:
            print('Please enter \'yes\' or \'no\'')
            continue
# play again?
    print('\n' + "Would you like to play again?")
    user_input = input("Yes or No: ")
    if user_input.lower() == 'yes':
        player1.player_hand = []
        player1.hand_value = 0
        continue
    else:
        print("Thank you for playing and see you next time!")
        play_again = False