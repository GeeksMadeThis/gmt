import random

class GuessBoard:
    def __init__(self, min, max, target):
        self.min = min
        self.max = max
        self.target = target


class GuessRuleBook:

    def GetNewBoard():
        min = 1
        max = 6

        if not isinstance(min, int): raise ValueError(f"The minimum value must be a whole number: {min}")
        if not isinstance(max, int): raise ValueError(f"The maximum value must be a whole number: {max}")
        if min > max: raise ValueError(f"The minimum value:{min} must not be greater than maximum value:{max}")
        target = random.randint(min, max)
        return GuessBoard(min, max, target)


print("Let's Play!")

ruleBook = GuessRuleBook
board = ruleBook.GetNewBoard()

print(board.target)
