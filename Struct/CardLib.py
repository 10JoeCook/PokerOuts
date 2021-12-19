import random
from collections import Counter
from functools import cmp_to_key


class Card:
	"""Class to represent a playing card
	Comparison operators have been implemented for sorting
	"""
	def __init__(self, suit: int, rank: int) -> None:
		self.suit = suit
		self.rank = rank

	def __str__(self) -> str:
		"""Return human-readable card name
		:return: card name in format "<rank> of <suit>"
		"""
		return self.get_rank() + " of " + self.get_suit()

	def __int__(self) -> int:
		""""Return the card number
		cards are ordered by rank, sub-ordered by suit
		"""
		return (self.rank * 4) + self.suit

	def __eq__(self, other) -> bool:
		return (self.rank, self.suit) == (other.rank, other.suit)

	def __ne__(self, other) -> bool:
		return (self.rank, self.suit) != (other.rank, other.suit)

	def __lt__(self, other) -> bool:
		return (self.rank, self.suit) < (other.rank, other.suit)

	def __le__(self, other) -> bool:
		return (self.rank, self.suit) <= (other.rank, other.suit)

	def __gt__(self, other) -> bool:
		return (self.rank, self.suit) > (other.rank, other.suit)

	def __ge__(self, other) -> bool:
		return (self.rank, self.suit) <= (other.rank, other.suit)

	def __repr__(self):
		return "%i %i" % (self.rank, self.suit)

	def get_suit_no(self) -> int:
		return self.suit

	def get_rank_no(self) -> int:
		return self.rank

	def get_suit(self) -> str:
		return CardUtils.suit_no_to_name(self.suit)

	def get_rank(self) -> str:
		return CardUtils.rank_no_to_name(self.rank)


class Deck:
	"""Class to represent a deck of playing cards
	"""
	def __init__(self) -> None:
		self. cards = []

	def generate_standard_deck(self) -> None:
		"""Generate a standard deck of playing cards
		🃑 < 🃁 < 🂱 < 🂡
		"""
		for rank in range(0, 13):
			for suit in range(0, 4):
				self.cards.append(Card(rank, suit))

	def shuffle(self) -> None:
		"""Shuffle the Deck
		"""
		random.shuffle(self.cards)

	def draw(self) -> Card:
		"""Draw a card from the deck
		:return: the drawn card
		"""
		return self.cards.pop()

	def draw_x(self, x: int) -> [Card]:
		ret = []
		for i in range(x):
			ret.append(Deck.draw(self))
		return ret

	def deal(self, no_hands: int, no_cards: int) -> [[Card]]:
		"""Deal hands of x size to y players
		:param no_hands: number of hands to deal
		:param no_cards: number of cards in each hand
		:return: list of hands
		"""
		hands = []
		for i in range(no_hands):
			hands.append(Deck.draw_x(self, no_cards))
		return hands

	def setup(self, no_players: int, no_cards: int) -> [[Card]]:
		"""Generate a standard deck, shuffle it then deal
		:param no_players: number of players to deal hands to
		:param no_cards: number of cards in each hand
		:return: dealt cards
		"""
		self.generate_standard_deck()
		self.shuffle()
		return self.deal(no_players, no_cards)


class CardUtils:
	@staticmethod
	def rank_no_to_name(rank_no: int) -> str:
		"""Converts from rank number to a string name
		This function is the only thing that defines the order of the ranks
		It alone controls which suit number corresponds to which of the playing card ranks
		i.e Chinese card games often use 2 as the highest card
		:param rank_no: the rank number used in Card
		:return: The name of the corresponding rank
		:raises: Value error: rank no is not valid
		"""
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
		"""Converts from suit number to a string name
		This function is the only thing that defines the order of the suits
		It alone controls which suit number corresponds to which of the playing card suits
		:param suit_no: the suit number used in Card
		:return: The name of the corresponding suit
		:raises: Value error: suit no is not valid
		"""
		if suit_no == 0:
			return "clubs"
		if suit_no == 1:
			return "diamonds"
		if suit_no == 2:
			return "hearts"
		if suit_no == 3:
			return "spades"
		raise ValueError("Invalid suit_no")

	@staticmethod
	def find_highest(cards: [Card]) -> Card:
		"""Return the highest card from a list
		Currently uses O(n) linear search as collections will be small
		Also cards could be unsorted, if cards were always sorted O(1) search could be used
		:param cards: Cards to be searched
		:return: highest card from the collection
		"""
		highest_card = cards[0]
		for card in cards:
			if card > highest_card:
				highest_card = card
		return highest_card

	@staticmethod
	def find_highest_x(cards: [Card], x: int) -> [Card]:
		"""Find the highest x cards from the list of cards
		:param cards: list of cards to search
		:param x: number of cards to find
		:return: list containing the highest x cards
		"""
		highest_x = []
		cards_cpy = cards.copy()
		for i in range(x):
			hc = CardUtils.find_highest(cards_cpy)
			cards_cpy.remove(hc)
			highest_x.append(hc)
		return highest_x


class HandUtils:
	@staticmethod
	def rank_hand(hand: [Card]):
		"""Rank a 5 card poker hand
		cards are rated on a multitude of factors for further ranking
		where stated multiple kickers are in descending order
		e.g. three aces beat 3 kings
		Ranking is as follows:
		Hand           |Ranking |Extra Factors(in precedence order)
		---------------|--------|----------------------------------
		Royal Flush    |0       |Suit
		Straight Flush |1       |Highest card in straight
		Four of a kind |2       |Kicker
		Full House     |3       |Highest toak, highest pair
		Flush          |4       |Highest card in flush
		Straight       |5       |Highest card in straight
		Three of a kind|6       |Highest toak, 1st, 2nd kickers
		Two Pair       |7       |Highest 1st Pair, Highest 2nd Pair, kicker
		Pair           |8       |Highest Pair, 1st, 2nd, 3rd kickers
		High Card      |9       |ordered ranks
		:param hand: 5 card hand to rank
		:return: tuple containing hand rank and extra factors ordered as per table
		"""
		if hand:
			hand_cpy = hand.copy()
			if HandUtils.is_royal_flush(hand_cpy):
				return 0, hand_cpy[0].get_suit_no()
			if HandUtils.are_consecutive(hand_cpy) and HandUtils.share_suit(hand_cpy):
				highest_card = CardUtils.find_highest(hand_cpy)
				return 1, highest_card.get_rank_no()
			groups = HandUtils.find_groups(hand_cpy)
			if len(groups) == 1 and groups[0][0] == 4:
				HandUtils.__remove_group(hand_cpy, groups[0])
				highest_card = CardUtils.find_highest(hand_cpy)
				return 2, groups[0][1], highest_card.get_rank_no()
			# possible optimisation?
			if len(groups) == 2 and ((groups[0][0] == 3 and groups[1][0] == 2) or (groups[0][0] == 2 and groups[1][0] == 3)):
				return 3, groups[0][1], groups[1][1]
			if HandUtils.share_suit(hand_cpy):
				highest_card = CardUtils.find_highest(hand_cpy)
				return 4, highest_card.get_rank_no()
			if HandUtils.are_consecutive(hand_cpy):
				highest_card = CardUtils.find_highest(hand_cpy)
				return 5, highest_card.get_rank_no()
			if len(groups) == 1 and groups[0][0] == 3:
				HandUtils.__remove_group(hand_cpy, groups[0])
				highest_cards = CardUtils.find_highest_x(hand_cpy, 2)
				return 6, groups[0][1], highest_cards[0].get_rank_no(), highest_cards[1].get_rank_no()
			if len(groups) == 2 and groups[0][0] == 2 and groups[1][0] == 2:
				HandUtils.__remove_group(hand_cpy, groups[0])
				HandUtils.__remove_group(hand_cpy, groups[1])
				highest_card = CardUtils.find_highest(hand_cpy)
				return 7, groups[0][1], groups[1][1], highest_card.get_rank_no()
			if len(groups) == 1:
				HandUtils.__remove_group(hand_cpy, groups[0])
				highest_cards = CardUtils.find_highest_x(hand_cpy, 3)
				return 8, groups[0][1], highest_cards[0].get_rank_no(), highest_cards[1].get_rank_no(), highest_cards[2].get_rank_no()
			# if no hands are found, return 9 representing a high card
			highest_cards = CardUtils.find_highest_x(hand_cpy, 5)
			return 9, highest_cards[0].get_rank_no(), highest_cards[1].get_rank_no(), highest_cards[2].get_rank_no(), highest_cards[3].get_rank_no(), highest_cards[4].get_rank_no()
		return ()

	@staticmethod
	def are_consecutive(cards: [Card]) -> bool:
		"""Check if a list cards are consecutive
		Ace can be used at start or end but cannot wraparound
		:param cards: cards to check
		:return: True if cards are consecutive, false otherwise
		"""
		sorted_cards = sorted(cards, key=cmp_to_key(lambda card1, card2: card1.get_rank_no() - card2.get_rank_no()))
		for i in range(len(sorted_cards) - 1):
			if not(sorted_cards[i].get_rank_no() + 1 == sorted_cards[i + 1].get_rank_no() or (sorted_cards[i].get_rank_no() == 3 and sorted_cards[i + 1].get_rank_no() == 12)):
				return False
		return True

	@staticmethod
	def share_suit(cards: [Card]) -> bool:
		"""Check if a list of cards shares a suit
		:param cards: cards to check
		:return: True if cards share suit, false otherwise
		"""
		suit = cards[0].get_suit_no()
		for i in range(len(cards)):
			if cards[i].get_suit_no() != suit:
				return False
		return True

	@staticmethod
	def is_royal_flush(cards: [Card]) -> bool:
		"""Check if cards form a royal flush
		:param cards: cards too check
		:return: true if cards from a royal flush, false otherwise
		"""
		if HandUtils.are_consecutive(cards) and HandUtils.share_suit(cards):
			if sorted(cards, key=cmp_to_key(lambda item1, item2: item1.get_rank_no() - item2.get_rank_no()))[0].get_rank_no() == 8:
				return True
		return False

	@staticmethod
	def find_groups(cards: [Card]) -> [(chr, int)]:
		"""Find groups of cards within a list of cards
		Possible groups are:
		Four of a kind
		Three of a kind
		Pair
		:param cards: List of cards to search
		:return: list containing the groups present in the list of cards
		"""
		ranks = []
		groups = []
		for card in cards:
			ranks.append(card.get_rank_no())
		card_counter = Counter(ranks)
		ranks = list(dict.fromkeys(card_counter.elements()))
		for rank in ranks:
			if card_counter[rank] == 2:
				groups.append((2, rank))
			elif card_counter[rank] == 3:
				groups.append((3, rank))
			elif card_counter[rank] == 4:
				groups.append((4, rank))
		return groups

	@staticmethod
	def make_group_hand(cards: [Card]) -> [(chr, int)]:
		"""Form a five card hand from a set of 7 cards (hand + table cards) that contains groups
		:param cards: 7 cards (hand + table)
		:param groups: groups present within the cards
		:return: 5 card hand with the best groups
		"""
		hand = []
		cards_cpy = cards.copy()
		groups = HandUtils.find_groups(cards_cpy)
		sorted_groups = list(reversed(sorted(groups, key=lambda x: x[0])))
		if len(sorted_groups) != 0:
			# quads
			if sorted_groups[0][0] == 4:
				hand += HandUtils.__remove_group(cards_cpy, sorted_groups[0])
				hand.append(CardUtils.find_highest(cards_cpy))
			# trips
			if sorted_groups[0][0] == 3:
				# pick best three of a kind
				if len(sorted_groups) == 1:
					hand += HandUtils.__remove_group(cards_cpy, sorted_groups[0])
					hand += CardUtils.find_highest_x(cards_cpy, 2)
				elif len(sorted_groups) == 2 and sorted_groups[1] == 3:
					if sorted_groups[0][1] > sorted_groups[1][1]:
						hand += HandUtils.__remove_group(cards_cpy, sorted_groups[0])
						hand += HandUtils.__remove_group(cards_cpy, sorted_groups[1])
					else:
						hand += HandUtils.__remove_group(cards_cpy, sorted_groups[1])
						hand += HandUtils.__remove_group(cards_cpy, sorted_groups[0])
					hand.remove(hand[-1])
				elif len(sorted_groups) == 2:
					hand += HandUtils.__remove_group(cards_cpy, sorted_groups[0])
					hand += HandUtils.__remove_group(cards_cpy, sorted_groups[1])
				elif len(sorted_groups) == 3 and sorted_groups[1][0] == 2 and sorted_groups[2][0] == 2:
					hand += HandUtils.__remove_group(cards_cpy, sorted_groups[0])
					if sorted_groups[1][1] > sorted_groups[2][1]:
						hand += HandUtils.__remove_group(cards_cpy, sorted_groups[1])
					else:
						hand += HandUtils.__remove_group(cards_cpy, sorted_groups[2])
		return hand

	@staticmethod
	def __remove_group(cards: [Card], group: ()) -> [Card]:
		"""private function to remove cards contained in a group from a list of cards
		:param cards: cards to remove from
		:param group: group to remove
		:return: list of cards with cards in the group removed
		"""
		ret = []
		i = 0
		while i < len(cards):
			if cards[i].get_rank_no() == group[1]:
				ret.append(cards[i])
				cards.remove(cards[i])
				i -= 1
			i += 1
		return ret

	@staticmethod
	def make_straight_hand(cards: [Card]) -> [Card]:
		cards_cpy = list(sorted(cards.copy(), key=lambda x: int(x)))
		cards_cpy = HandUtils.remove_duplicate_ranks(cards_cpy)
		if len(cards_cpy) >= 5:
			possible_straights = [0] * (len(cards_cpy) - 4)
			for i in range(len(possible_straights)):
				if HandUtils.are_consecutive(cards_cpy[0 + i:5 + i]):
					possible_straights[i] = 1
			for i in range(len(possible_straights) - 1, -1, -1):
				if possible_straights[i] == 1:
					return cards_cpy[0 + i:5 + i]
		return []

	@staticmethod
	def most_common_suit(cards: [Card]) -> (int, int):
		ret = 0
		suits = [0, 0, 0, 0]
		for card in cards:
			suits[card.get_suit_no()] += 1
		most_common = suits[ret]
		for i in range(len(suits)):
			if suits[i] > most_common:
				ret = i
				most_common = suits[i]
		return ret, most_common

	@staticmethod
	def remove_duplicate_ranks(cards: [Card]) -> [Card]:
		i = 0
		cards_cpy = cards.copy()
		straight_flush_suit = HandUtils.most_common_suit(cards_cpy)[0]
		while i < len(cards_cpy) - 2:
			if cards_cpy[i].get_rank_no() == cards_cpy[i + 1].get_rank_no():
				if cards_cpy[i].get_suit_no() == straight_flush_suit:
					cards_cpy.remove(cards_cpy[i + 1])
				else:
					cards_cpy.remove(cards_cpy[i])
				i -= 1
			i += 1
		return cards_cpy

	@staticmethod
	def make_flush_hand(cards: [Card]) -> [Card]:
		hand = []
		cards_cpy = cards.copy()
		flush_suit = HandUtils.most_common_suit(cards_cpy)[0]
		i = 0
		while i < len(cards_cpy):
			if cards_cpy[i].get_suit_no() != flush_suit:
				cards_cpy.remove(cards_cpy[i])
				i -= 1
			i += 1
		if len(cards_cpy) >= 5:
			cards_cpy = list(sorted(cards_cpy, key=lambda x: (x.get_suit_no() * 13) + x.get_rank_no()))
			for i in range(0, 5):
				hand.append(cards_cpy[i])
		return hand

	@staticmethod
	def make_hand(cards: [Card]) -> [Card]:
		hands = [HandUtils.make_straight_hand(cards), HandUtils.make_flush_hand(cards), HandUtils.make_group_hand(cards)]
		ranks = []
		top_rank = (999, 999)
		for hand in hands:
			rank = HandUtils.rank_hand(hand)
			ranks.append(rank)
			if rank != () and rank < top_rank:
				top_rank = rank
		if top_rank != (999, 999):
			for i in range(len(ranks)):
				if ranks[i] == top_rank:
					return hands[i]
		return list(reversed(sorted(cards.copy(), key=lambda x: int(x))))[0:5]
