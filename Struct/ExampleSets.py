from Struct.CardLib import Card

# Five Card Hands
high_card =     [Card(0, 9), Card(1, 5), Card(0, 3), Card(3, 6), Card(2, 12)]
pair =          [Card(0, 9), Card(1, 9), Card(0, 3), Card(3, 6), Card(2, 12)]
two_pair =      [Card(0, 3), Card(1, 3), Card(0, 9), Card(1, 9), Card(2, 12)]
trips =         [Card(0, 9), Card(1, 9), Card(2, 9), Card(3, 6), Card(2, 12)]
straight =      [Card(0, 5), Card(1, 6), Card(2, 7), Card(3, 8), Card(2, 8)]
flush =         [Card(0, 5), Card(0, 6), Card(0, 7), Card(0, 9), Card(0, 10)]
full_house =    [Card(0, 9), Card(1, 9), Card(2, 9), Card(3, 5), Card(2, 5)]
quads =         [Card(0, 9), Card(1, 9), Card(2, 9), Card(3, 9), Card(2, 12)]

# Seven card sets
high_card_7 =   [Card(0, 9), Card(1, 5), Card(0, 3), Card(3, 6), Card(2, 12), Card(1, 8), Card(3, 4)]
straight_7 =    [Card(0, 5), Card(1, 6), Card(2, 7), Card(3, 8), Card(2, 9), Card(1, 8), Card(3, 6)]
flush_7 =       [Card(0, 5), Card(0, 6), Card(0, 7), Card(0, 9), Card(0, 10), Card(1, 8), Card(3, 6)]
full_house_7 =  [Card(0, 9), Card(1, 9), Card(2, 9), Card(3, 5), Card(2, 5), Card(1, 8), Card(3, 6)]


quads_pair = [Card(0, 9), Card(1, 9), Card(2, 9), Card(3, 9), Card(3, 5), Card(2, 5), Card(2, 12)]
