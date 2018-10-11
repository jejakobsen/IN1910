"""
A normal playing card is identified by its value and its suit. Let a card be represented 
as a tuple of the value and the suit, where the value should be an integer between 1 and 13, 
and the suit by a single letter. For example, (12, 'C') would represent the queen of clubs.

1) Use nested loops to create a list that contains a normal deck of 52 playing cards.
2) Use random.shuffle to shuffle the deck.
3) fter shuffling, draw 13 cards from the deck.
4) Sort and print the drawn cards out so that they are separated by suit, and shown in
increasing value within each suit.

Hint: To sort a list, you can use the list.sort() method. If you are unfamiliar with this,
you can read this mini how-to:
https://wiki.python.org/moin/HowTo/Sorting
"""
import random
from operator import itemgetter

deck = []
for i in range(1,14,1):
	for j in ('C','S','H','D'):
		deck.append((i,j)) 
# created the deck		

random.shuffle(deck) # shufflin'

draw = [card for card in deck[0:13]] # draw 13 first cards

draw_s = sorted(draw, key=itemgetter(1,0)) # sort for suit, then for value (ascending) 