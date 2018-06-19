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
    
    # Method to add a card to the players hand
    def add_card(self, card):
        pass

    # Method for adjusting hand value for aces
    def adjust_for_ace(self):
        pass




    
