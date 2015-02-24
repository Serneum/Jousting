SHIELD = 'Shield'
COUNTER = 'Counter'
LUNGE = 'Lunge'

winning_list = {
    'Shield': {
        'Lunge': True
    },
    'Lunge': {
        'Counter': True
    },
    'Counter': {
        'Shield': True
    }
}

# Return -1 if p1 wins, 0 for a tie, or 1 if p2 wins
def judge(p1_choice, p2_choice):
    if p1_choice == p2_choice:
        return 0
    else:
        # Return False if a value is not in the winning_list dictionary
        p1_win = winning_list[p1_choice].get(p2_choice, False)
        return -1 if p1_win else 1