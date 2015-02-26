SHIELD = 0
COUNTER = 1
LUNGE = 2

# Return 1 if p1 wins, 0 for a tie, or 2 if p2 wins
def judge(p1_choice, p2_choice):
    diff = p1_choice - p2_choice
    return (diff + 3) if diff < 0 else diff