import random

def select_random_card(chosen_cards):
    r = random.randint(0, 52)
    selected = chosen_cards.get(r)
    if selected != None:
        return select_random_card(chosen_cards)
    return r

def get_ascending_card_range(n: int):
    m = 12
    k = n % m
    opts = map(lambda i: k + (12 * i) + 1, range(4))
    return set(opts)

def check_asc_cards(chosen_cards: list):
    for i in range(len(chosen_cards)):
        if (i == len(chosen_cards) - 1):
            return True
        
        current = chosen_cards[i]
        next = chosen_cards[i+1]
        next_asc_range = get_ascending_card_range(current)
        if (next not in next_asc_range):
            return False
        
# Select 5 cards at random
# returns True if cards are in ascending order
def sim():
    chosen_cards = dict()
    card_order = 13

    for s in range(5):
        r = random.randint(0, card_order - 1)
        card = select_random_card(chosen_cards)
        chosen_cards[s] = card
        
    is_ascending = check_asc_cards(chosen_cards)
    return is_ascending

def multi_sim(sample_size = 100):
    count = 0
    for n in range(sample_size):
        outcome = sim()
        if outcome:
            count = count + 1
            avg = 100 * (count / (n + 1))
            print(f"n: {n}, avg: {avg}")

    avg = 100 * (count / (n + 1))
    return (count, avg)

# output given 5m run:
# n: 5000000, count: 143, avg: 0.00286
def main():
    sample_size = 5_000_000
    (count, avg) = multi_sim(sample_size)
    print(f"n: {sample_size}, count: {count}, avg: {avg}")

if __name__ == '__main__':
    main()
