import random
from collections import Counter
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
		return CardUtils.suit_no_to_name(self.suit)

	def get_rank(self) -> str:
		return CardUtils.rank_no_to_name(self.rank)


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


class CardUtils:
	@staticmethod
	def rank_no_to_name(rank_no: int) -> str:
		if rank_no == 0:
			return "two"
		elif rank_no == 1:
			return "three"
		elif rank_no == 2:
			return "four"
		elif rank_no == 3:
			return "five"
		elif rank_no == 4:
			return "six"
		elif rank_no == 5:
			return "seven"
		elif rank_no == 6:
			return "eight"
		elif rank_no == 7:
			return "nine"
		elif rank_no == 8:
			return "ten"
		elif rank_no == 9:
			return "jack"
		elif rank_no == 10:
			return "queen"
		elif rank_no == 11:
			return "king"
		elif rank_no == 12:
			return "ace"
		raise ValueError('invalid rank_no')

	@staticmethod
	def suit_no_to_name(suit_no: int) -> str:
		if suit_no == 0:
			return "clubs"
		if suit_no == 1:
			return "diamonds"
		if suit_no == 2:
			return "hearts"
		if suit_no == 3:
			return "spades"
		raise ValueError("Invalid suit_no")


class HandUtils:
	@staticmethod
	def rank_hand(hand: [Card]):
		if HandUtils.is_royal_flush(hand):
			print("Royal Flush")
			return 0
		if HandUtils.are_consecutive(hand) and HandUtils.share_suit(hand):
			print("Straight Flush")
			return 1
		gs = HandUtils.find_groups(hand)
		# quads
		if len(gs) == 1 and gs[0][0] == 'q':
			print("Quads")
			return 2
		# full house
		if len(gs) == 2 and (gs[0][0] == 't' and gs[1][0] == 'p' or gs[0][0] == 'p' and gs[1][0] == 't'): # possible optimiasation
			print("Full house")
			return 3
		if HandUtils.share_suit(hand):
			print("Flush")
			return 4
		if HandUtils.are_consecutive(hand):
			print("Straight")
			return 5
		if len(gs) == 1 and gs[0][0] == 't':
			print("Trips")
			return 6
		if len(gs) == 2 and gs[0][0] == 'p' and gs[1][0] == 'p' :
			print("Two Pair")
			return 7
		if len(gs) == 1:
			print("Pair")
			return 8
		print("High Card")
		return 9

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
		if HandUtils.are_consecutive(cards) and HandUtils.share_suit(cards):
			if sorted(cards, key=cmp_to_key(lambda item1, item2: item1.get_rank_no() - item2.get_rank_no()))[0].get_rank_no() == 8:
				return True
		return False

	@staticmethod
	def find_groups(cards: [Card]) -> [(chr, int)]:
		# ranks
		r = []
		# groups
		g = []
		for card in cards:
			r.append(card.get_rank_no())
		c = Counter(r)
		tl = list(dict.fromkeys(c.elements()))
		# i = rank
		# c[i] = count
		for i in tl:
			if c[i] == 2:
				g.append((2, i))
			elif c[i] == 3:
				g.append((3, i))
			elif c[i] == 4:
				g.append((4, i))
		return g
