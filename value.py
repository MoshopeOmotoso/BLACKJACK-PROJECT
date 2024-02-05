def card_value(card_rank):
  if card_rank > 13 or card_rank < 1:
    return None

  if card_rank == 11 or card_rank == 12 or card_rank == 13:
    return 10
  elif card_rank == 1:
    return 11
  else:
    return card_rank
