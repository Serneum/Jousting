import random

D2 = 2
D3 = 3
D4 = 4
D5 = 5
D6 = 6
D7 = 7
D8 = 8
D10 = 10
D12 = 12
D14 = 14
D16 = 16
D20 = 20
D24 = 24
D30 = 30
D34 = 34
D50 = 50
D60 = 60
D100 = 100

# Roll a set of dice and get the total value after being adjusted by a modifier
# die: The die to roll
# count: The number of dice to roll
# modifier: The amount to add (or remove) from the dice roll value
# Returns the value determined by rolling the dice. Ex: roll(2, Dice.D6, -3) will return a value between -1 and 9
def roll(die, count=1, modifier=0):
    total = 0
    for x in range(count):
        total += random.randint(1, die)
    total += modifier
    return total