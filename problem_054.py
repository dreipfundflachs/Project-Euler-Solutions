#################################
#  PROJECT EULER - PROBLEM 054  #
#################################
import time


def get_card_values(hand: list[str]) -> tuple:
    """ Given a hand, return a tuple of the card values (2 <= value <= 14) in
    it, sorted in decreasing order. For example, for the hand 9D 6S QH 6H QC,
    the function returns (12, 12, 9, 9, 6). (Note that a Queen's value is 12).
    """
    cards = []
    for string in hand:
        cards.append(string[0])
    return tuple(reversed(sorted([VALUES[card] for card in cards])))


def get_weighted_card_values(hand: list[str]) -> tuple:
    """ To be able to compare two hands, we would like to sort the card values
    in a given hand in decreasing order by number of occurrences, and for two
    cards which occur the same number of times, the one with the highest value
    should appear first. Because this is not easy to implement, we instead sort
    in decreasing order by _weighted_ card values, where the weighted card
    value of a card is given by:
        value of the card + 15 * (# times it occurs - 1)
    In the end, this achieves the same result as intended originally. For
    example, for the hand 9D 6S QH 6H QC, the function returns
        (27, 27, 21, 21, 9) = (12 + 15, 12 + 15, 6 + 15, 6 + 15, 9).
    (Note that a Queen's value is 12). """
    cards = []
    for string in hand:
        cards.append(string[0])
    return tuple(reversed(sorted([VALUES[card] + 15 * (cards.count(card) - 1)
                 for card in cards])))


def get_card_frequencies(hand: list[str]) -> tuple:
    """ Given a hand, returns the card frequencies as a tuple sorted in
    decreasing order. For example, for the hand 9D 6S QH 6H QC,
    the function returns (2, 2, 1). This function will be used to check if a
    hand has one pair, two pairs, etc... """
    cards = []
    for string in hand:
        cards.append(string[0])
    return tuple(reversed(sorted([cards.count(card) for card in set(cards)])))


def are_all_of_the_same_suit(hand: list[str]) -> bool:
    """ Given a hand, decides if all cards in the hand are of the same suit.
    This will be used to check if we have a (straight, royal) flush."""
    suits = set()
    for string in hand:
        suits.add(string[1])
    if len(suits) == 1:
        return True
    else:
        return False


def are_consecutive_values(hand: list[str]) -> bool:
    """ Given a hand, decides if its cards are of consecutive values. """
    card_values = get_card_values(hand)
    for k in range(len(card_values) - 1):
        if card_values[k] != card_values[k + 1] + 1:
            return False
    return True


def get_hand_score(hand: list[str]) -> int:
    """ Given a hand, assigns a score between 1 and 10 to it, corresponding to
    the ten 'ranks' described in the problem statement. (A higher score is
    better than a lower score). """
    card_frequencies = get_card_frequencies(hand)
    card_values = get_card_values(hand)
    score = 1

    if card_frequencies == (2, 1, 1, 1):
        score = 2
    if card_frequencies == (2, 2, 1):
        score = 3
    if card_frequencies == (3, 1, 1):
        score = 4
    if card_frequencies == (3, 2):
        score = 7
    if card_frequencies == (4, 1):
        score = 8
    if are_consecutive_values(hand) and score < 5:
        score = 5
    if are_all_of_the_same_suit(hand):
        if score < 6:
            score = 6
        if are_consecutive_values:
            score = 9
            if card_values == (14, 13, 12, 11, 10):
                score == 10
    return score


def tie_break(hand_1: list[str], hand_2: list[str]) -> int:
    """ If two hands have the same score, this function breaks the tie. """
    if get_weighted_card_values(hand_1) > get_weighted_card_values(hand_2):
        return 1
    return 0


start = time.time()

VALUES = {card: value for value, card in enumerate('23456789TJQKA', 2)}

# Extract the hands of both players and store them in a list.
hands_player_1: list[list[str]] = []
hands_player_2: list[list[str]] = []
with open('p054_poker.txt') as file_object:
    for line in file_object:
        cards = line.rstrip().split(' ')
        hands_player_1.append(cards[:5])
        hands_player_2.append(cards[5:])


# Calculate player 1's score.
total_score_player_1 = 0
for (hand_1, hand_2) in zip(hands_player_1, hands_player_2):
    if get_hand_score(hand_1) > get_hand_score(hand_2):
        total_score_player_1 += 1
    elif get_hand_score(hand_1) == get_hand_score(hand_2):
        total_score_player_1 += tie_break(hand_1, hand_2)

print(total_score_player_1)

end = time.time()
print(f"Program runtime: {end - start} seconds")
