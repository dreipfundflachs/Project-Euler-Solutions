#################################
#  PROJECT EULER - PROBLEM 084  #
#################################
import time
import random


# The idea of the solution is to simulate a sufficiently large number of moves
# of a player and to count the number of times that each square is visited.
# Thus, the resulting answer is only statistically probable, not absolutely
# certain.

class Die:
    """ Models a die. """
    def __init__(self, sides=4):
        self.sides = sides

    def roll(self) -> int:
        return random.randint(1, self.sides)


class CardDeck:
    """ Models a deck of cards. """
    def __init__(self, number_of_cards=16):
        self.number_of_cards = number_of_cards
        self.cards = list(range(1, self.number_of_cards + 1))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self) -> int:
        drawn_card = self.cards.pop(0)
        self.cards.append(drawn_card)
        return drawn_card


class Monopoly:
    """ Emulates a single player in monopoly. """
    def __init__(self):
        self.square = 0
        self.consecutive_doubles = 0

    def next_move(self):
        roll_1 = first_die.roll()
        roll_2 = second_die.roll
        result = first_die.roll() + second_die.roll()
        self.square = (self.square + result) % 40

        # Consecutive double?
        if roll_1 == roll_2:
            self.consecutive_doubles += 1
            if self.consecutive_doubles == 3:
                self.consecutive_doubles == 0
                self.square = 10
        else:
            pass

        # Go To Jail square:
        if self.square == 30:
            self.square = 10

        # Community Chest squares:
        elif self.square == 2 or self.square == 17 or self.square == 33:
            drawn_card = CC_deck.draw_card()
            if drawn_card == 1:
                self.square = 0
            elif drawn_card == 2:
                self.square = 10
            else:
                pass

        # Chance squares:
        elif self.square in (7, 22, 36):
            drawn_card = CH_deck.draw_card()
            if drawn_card == 1:
                self.square = 0
            elif drawn_card == 2:
                self.square = 10
            elif drawn_card == 3:
                self.square = 11
            elif drawn_card == 4:
                self.square = 24
            elif drawn_card == 5:
                self.square = 39
            elif drawn_card == 6:
                self.square = 5
            elif drawn_card in (7, 8):
                # Go to next Railway square: 5, 15, 25, 35.
                self.square = 5 + ((self.square + 5) // 10 % 4 * 10)
            elif drawn_card == 9:
                # Go to next Utility square: 12 or 28.
                self.square = 28 if (12 < self.square < 28) else 12
            elif drawn_card == 10:
                self.square -= 3
            else:
                pass


start = time.time()

TRIALS = 2 * 10**5  # Total number of moves.

visits = [0 for k in range(40)]
# visits[k] will hold the number of times that square k is visited.

first_die = Die(4)
second_die = Die(4)

CC_deck = CardDeck(16)  # Deck of Community Chest cards.
CC_deck.shuffle()
CH_deck = CardDeck(16)  # Deck of Chance cards.
CH_deck.shuffle()

game = Monopoly()

for n in range(TRIALS):
    game.next_move()
    visits[game.square] += 1

# Sort the list of squares by the number of visits:
most_visited = sorted(list(range(40)), key=lambda i: visits[i], reverse=True)
# Produce a string from the three most visited squares and print it:
modal_string = "".join([str(square) for square in most_visited[:3]])
print(modal_string)

end = time.time()
print(f"Program runtime: {end - start} seconds")
