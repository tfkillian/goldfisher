import itertools
import random
import math
# import numpy as np

def createDeck():
    """
    This creates a single list containing tuples which have the values
    """
    deck = ["Forest","Forest","Forest","Forest","Forest","Forest","Forest","Forest","Forest","Forest","Forest",
            "Forest","Forest","Forest","Forest","Forest","Forest","Forest","Fog","Fog","Root Maze",
            "Utopia Sprawl","Utopia Sprawl","Utopia Sprawl","Utopia Sprawl","Elvish Mystic","Elvish Mystic",
            "Elvish Mystic","Elvish Mystic","Arbor Elf","Arbor Elf","Arbor Elf","Arbor Elf","Overgrowth",
           "Overgrowth","Overgrowth","Overgrowth","Eternal Witness","Eternal Witness","Eternal Witness",
           "Stampeding Serow","Stampeding Serow","Creeping Mold","Creeping Mold","Creeping Mold","Creeping Mold",
           "Bramble Crush","Bramble Crush","Bramble Crush","Bramble Crush","Plow Under","Plow Under","Plow Under",
           "Acidic Slime","Acidic Slime","Primal Command","Primal Command","Primal Command","Primal Command",]
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
# print(len(theDeck))

print("Opening hand")
print(theHand)
print("First five cards")
print(theDraw)
