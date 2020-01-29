import itertools
import random
import math

"""
this is a short python script to simulate mtg goldfishing
it will read a simple text file with card names and read the file line by line
it will then deal you 7 cards and show you the first 5 cards you would draw
"""

## mono green control
current_file = "mgc"

def createDeck():
    """
    This creates a single list containing tuples which have the values
    """
    deck = []
    my_file = open(current_file)
    all_the_lines = my_file.readlines()
    deck = []
    for i in all_the_lines:
        deck.append(i.strip())
    my_file.close()
    random.shuffle(deck)
    return deck

def dealHand(deck):
    """
    draws 7 cards and modifies the deck.
    I was told to instead use indexing to draw, instead of modifying the list
    """
    hand = [] 
    for i in range(7): 
        hand.append(deck.pop())
    return hand

def dealDraw(deck):
    """
    draws 5 cards and modifies the deck.
    I was told to instead use indexing to draw, instead of modifying the list
    """
    hand = [] 
    for i in range(5): 
        hand.append(deck.pop())
    return hand

theDeck = createDeck()
theHand = dealHand(theDeck)
theDraw = dealDraw(theDeck)

print("Opening hand: " + ', '.join(theHand))
#print(', '.join(theHand))
print("First five cards: " + ', '.join(theDraw))
#print(', '.join(theDraw))
