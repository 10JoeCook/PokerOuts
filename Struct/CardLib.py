import random

class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.get_rank() + " of " + self.get_suit()

	def __int__(self):
		return (self.rank * 13) + self.rank

	def get_suit_no(self):
		return self.suit

	def get_rank_no(self):
		return self.rank

	def get_suit(self):
		if self.suit == 0:
			return "clubs"
		elif self.suit == 1:
			return "diamonds"
		elif self.suit == 2:
			return "hearts"
		elif self.suit == 3:
			return "spades"
		else:
			return "Error"

	def get_rank(self):
		if self.rank == 0:
			return "two"
		elif self.rank == 1:
			return "three"
		elif self.rank == 2:
			return "four"
		elif self.rank == 3:
			return "five"
		elif self.rank == 4:
			return "six"
		elif self.rank == 5:
			return "seven"
		elif self.rank == 6:
			return "eight"
		elif self.rank == 7:
			return "nine"
		elif self.rank == 8:
			return "ten"
		elif self.rank == 9:
			return "jack"
		elif self.rank == 10:
			return "queen"
		elif self.rank == 11:
			return "king"
		elif self.rank == 12:
			return "ace"


class Deck:
	def __init__(self):
		self. cards = []

	def generate_standard_deck(self):
		for i in range(0, 4):
			for j in range(0, 13):
				self.cards.append(Card(i, j))

	def shuffle(self):
		random.shuffle(self.cards)

	def draw(self):
		return self.cards.pop()
