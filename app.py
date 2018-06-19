# Imports the random library
import random

# A tuple that holds the four different suits in a deck of cards
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

# A tuple that holds each of the 13 card ranks in one suit
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')

# A dictionary that contains each card rank and the corresponding value in a game of blackjack
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

playing = True

# Creating the class for each individual card
class Card:
    # Initialize card class properties
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Tests the card class to make sure it works
# card = Card("Hearts", "Two")
# print(card)

#Creating the class for a full deck of cards
class Deck:
    # Initial deck conditions
    def __init__(self):
        self.deck = [] # starts with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    # Special print method to show the deck has all 52 cards
    def __str__(self):
        deck_full = ''
        for card in self.deck:
            deck_full += f"\n {card.__str__()}"
        return f'The deck has: {deck_full}'
    # Shuffle method to rearrange the deck
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        return self.deck.pop()

    

# Testing out the Deck class to make it is creating all 52 cards
# test_deck = Deck()
# print(test_deck)

# Testing the deal method attached 
# print(test_deck.deal())

# Testing the shuffle method
# test_deck.shuffle()
# print(test_deck.deal())

# Class for the hands of the player and the computer
class Hand:
    def __init__(self):
        self.cards = [] # Start with an empty hand
        self.value = 0 # Hand value begins at zero
        self.aces = 0 # Number of Aces in hand starts at zero

    def __str__(self):
        hand_full = ''
        for card in self.cards:
            hand_full += f"\n {card.__str__()}"
        return f'Your hand has: {hand_full}' + f'\n Your hand value is {self.value}' + f'\n Your hand has {self.aces} aces'
    
    # Method to add a card to the players hand
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1 # add to self.aces

    # Method for adjusting hand value for aces
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# Tests for the Hand class
# my_hand = Hand()
# Add a card to hand, check the values, check the ace count and make sure adjust for ace is working
# my_hand.add_card(Card("Diamonds", "Queen"))
# my_hand.add_card(Card("Hearts", "Ace"))
# my_hand.add_card(Card("Spades", "Two"))
# print(my_hand)
# my_hand.adjust_for_ace()
# print(my_hand)

# Creating a chips class to track player wins, bets and starting bank
class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
    
    # Method for win results
    def win_bet(self):
        self.total += self.bet
    
    # Method for lost results
    def lose_bet(self):
        self.total -= self.bet


# Function for taking in user bets
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet?"))
        except ValueError:
            print("Sorry, bet must be an integer!")
        else:
            if chips.bet > chips.total:
                print(f"Bet cannot exceed {chips.total}")
            else:
                break

# Test to make sure take bet function works
# user_chips = Chips()
# take_bet(user_chips)

# Function that allows the user to take a hit from the dealer
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

# Test hit function
# new_deck = Deck()
# new_deck.shuffle()
# user_hand = Hand()
# hit(new_deck, user_hand)
# print(user_hand)
# hit(new_deck, user_hand)
# print(user_hand)
# hit(new_deck, user_hand)
# print(user_hand)

# Function that determines the users desired move
def hit_or_stand(deck, hand):
    global playing

    while True:
        user_decision = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if user_decision[0].lower() == 'h':
            hit(deck,hand)
        elif user_decision[0].lower() == 's':
            print("Player stands. Dealer is playing")
            playing - False
        else:
            print("Sorry, please use a different input")
            continue
        break

# Testing hit or stand function

# new_deck = Deck()
# new_deck.shuffle()
# user_hand = Hand()
# hit_or_stand(new_deck, user_hand)
# print(user_hand)

# Function that shows some of the cards in the dealers hand and all in the users hand

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    try:
        print('',dealer.cards[1])  
    except:
        print('Dealer only has one card')
    finally:
        print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

# Testing the show_some and show_all function

# new_deck = Deck()
# new_deck.shuffle()
# user_hand = Hand()
# dealer_hand = Hand()
# hit(new_deck, user_hand)
# hit(new_deck, user_hand)
# hit(new_deck, dealer_hand)
# hit(new_deck, dealer_hand)

# Calling show_some function
# show_some(user_hand, dealer_hand)
# Calling show_all function
# show_all(user_hand, dealer_hand)

# Function to call if the dealer wins
def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()

# Function to call if the dealer busts
def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()

# Function to call if the player wins
def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()

# Function to call if the player busts
def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lost_bet()

# Function to call if the game ends tied
def push(player, dealer):
    print("Player and Dealer Tie!")















    
