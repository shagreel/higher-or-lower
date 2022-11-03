import random
import logging


def game():
    deck = random.sample(range(1, 11), 10)
    logging.debug("Initial Deck : %s", deck)
    previous_card = deck.pop()
    logging.debug("Picked : %s", previous_card)

    winner = True

    while deck and winner:
        higher = choose(previous_card, deck)
        if higher:
            logging.debug("Chose : Higher")
        else:
            logging.debug("Chose : Lower")
        card = deck.pop()
        logging.debug("Picked : %s", card)
        if higher and previous_card < card:
            previous_card = card
        elif not higher and previous_card > card:
            previous_card = card
        else:
            winner = False

    return winner


def choose(test, deck):
    lower = 0
    higher = 0
    for card in deck:
        if card < test:
            lower += 1
        if card > test:
            higher += 1

    if lower == higher:
        if random.randint(0, 1):
            higher += 1
        else:
            lower += 1

    return higher > lower


# logging.basicConfig(level=logging.DEBUG)
wins = 0
losses = 0
for i in range(10000000):
    won = game()
    if won:
        wins += 1
        logging.debug("You won")
    else:
        losses += 1
        logging.debug("You lost")

    # inp = "o"
    # while inp not in ['Y', 'y', 'N', 'n']:
    #     inp = input("Want to continue? (Y/N): ")
    # if inp in ['N', 'n']:
    #     break
    # else:
    #     logging.debug("Start of new game.")

print("Wins  : " + str(wins))
print("Losses: " + str(losses))
print("Total : " + str(wins + losses))
print("Win%  : " + str((wins/(wins+losses))*100) + "%")