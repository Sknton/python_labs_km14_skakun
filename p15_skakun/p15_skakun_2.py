lst_of_cards = ['A', *range(2, 11), 'J', 'Q', 'K']
lst_of_suit = ['diamonds', 'clubs', 'hearts', 'spades']
def card_suit():
    for suit in lst_of_suit:
        for card in lst_of_cards:
            yield str(card) + ' ' + suit

card_ord = card_suit()
while 1:
    print(next(card_ord))