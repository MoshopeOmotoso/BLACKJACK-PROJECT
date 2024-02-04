from random import randint
from end_status import blackjack_or_bust
from value import card_value
from name import draw
# Write all of your part 2A code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
def play_dealer_turn():
  starting_hand = 0
  for i in range(2):
    random_card = randint(1, 13)
    print(draw(random_card))
    starting_hand += card_value(random_card)

  if starting_hand < 17:
    while starting_hand < 17:
      print(f'Dealer has {starting_hand}.')
      random_card = randint(1, 13)
      starting_hand += card_value(random_card)
      print(draw(random_card))
  else:
    pass
  print(f'Final hand: {starting_hand}.')
  if starting_hand >= 21:
    print(blackjack_or_bust(starting_hand))
