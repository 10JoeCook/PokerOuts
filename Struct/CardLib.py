import random
from functools import cmp_to_key


class Card:
	def __init__(self, suit: int, rank: int) -> None:
		self.suit = suit
		self.rank = rank

	def __str__(self) -> str:
		return self.get_rank() + " of " + self.get_suit()

	def __int__(self) -> int:
		return (self.rank * 13) + self.rank

	def get_suit_no(self) -> int:
		return self.suit

	def get_rank_no(self) -> int:
		return self.rank

	def get_suit(self) -> str:
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

	def get_rank(self) -> str:
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
	def __init__(self) -> None:
		self. cards = []

	def generate_standard_deck(self) -> None:
		for i in range(0, 4):
			for j in range(0, 13):
				self.cards.append(Card(i, j))

	def shuffle(self) -> None:
		random.shuffle(self.cards)

	def draw(self) -> Card:
		return self.cards.pop()

	def deal(self, no_players: int, no_cards: int) -> [[Card]]:
		# hands
		hs = []
		for i in range(no_players):
			# hand
			h = []
			for j in range(no_cards):
				h.append(self.draw())
			hs.append(h)
		return hs

	def setup(self, no_players: int, no_cards: int) -> [[Card]]:
		self.generate_standard_deck()
		self.shuffle()
		return self.deal(no_players, no_cards)


class HandRanker:
	@staticmethod
	def rank_hand(hand: [Card]):
		if HandRanker.is_royal_flush(hand):
			print("Royal Flush")
			return 0
		elif HandRanker.are_consecutive(hand) and HandRanker.share_suit(hand):
			print("Straight Flush")
			return 1
		# quads
		# full house
		elif HandRanker.share_suit(hand):
			print("Flush")
		elif HandRanker.are_consecutive(hand):
			print("straight")

	@staticmethod
	def are_consecutive(cards: [Card]) -> bool:
		crds = sorted(cards, key=cmp_to_key(lambda item1, item2: item1.get_rank_no() - item2.get_rank_no()))
		for i in range(len(cards) - 1):
			if not(crds[i].get_rank_no() + 1 == crds[i + 1].get_rank_no() or (crds[i].get_rank_no() == 3 and crds[i + 1].get_rank_no() == 12)):
				return False
		return True

	@staticmethod
	def share_suit(cards: [Card]) -> bool:
		s = cards[0].get_suit_no()
		for i in range(len(cards)):
			if cards[i].get_suit_no() != s:
				return False
		return True

	@staticmethod
	def is_royal_flush(cards: [Card]) -> bool:
		if HandRanker.are_consecutive(cards) and HandRanker.share_suit(cards):
			if sorted(cards, key=cmp_to_key(lambda item1, item2: item1.get_rank_no() - item2.get_rank_no()))[0].get_rank_no() == 8:
				return True
		return False
