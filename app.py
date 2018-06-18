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
    
