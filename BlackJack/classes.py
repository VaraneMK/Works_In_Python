class Card:
    '''
    This class stores the suit, rank and value of the card.
    '''

    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} {self.suit}"

    def get_value(self):
        '''
        Returns the weight of the card
        '''
        return self.value


class Deck:
    '''
    This is a class that contains a deck of 52 cards (instances of the Card class)
    '''

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank, values.get(rank)))

    def __str__(self):
        return ', '.join(map(str, self.deck))

    def check_deck(self):
        '''
        Displays the deck
        '''
        for i in range(0, len(self.deck)):
            print(self.deck[i])

    def shuffle(self):
        '''
        Stirs the deck
        '''
        random.shuffle(self.deck)

    def deal(self):
        '''
        Distributes the card
        '''
        card = self.deck[len(self.deck) - 1]
        self.deck.pop(len(self.deck) - 1)
        return card


class Hand:
    '''
    A class that contains cards and chips in the hand
    '''
    points = 0

    def __init__(self, status=0, chips=0, name='Player'):
        self.cards = []
        self.name = name
        self.status = status  # To denote a dealer or a player
        self.chips = chips  # Number of chips
        self.aces = 0  # To take into account the number of aces in the hand

    def add_card(self, card):
        '''
        Gives a new card in hand
        '''
        self.cards.append(card)
        if card.rank == 'Ace':
            self.aces += 1
        self.points += card.get_value()

    def __str__(self):
        return 'Your cards: ' + ', '.join(map(str, self.cards))

    def show_points(self):
        '''
        Show points in cards
        '''
        return self.points

    def show_all_cards(self):
        '''
        Shows all the cards from the hand
        '''
        if self.status == 1:
            print('Player cards: ' + ', '.join(map(str, self.cards)) + f'. Points: {self.points}')
        else:
            print('Dealer cards: ' + ', '.join(map(str, self.cards)) + f'. Points: {self.points}\n')

    def show_some_cards(self):
        '''
        Shows some the cards from the hand
        '''
        if self.status == 1:
            print('Player cards: ' + ', '.join(map(str, self.cards)) + f'. Points: {self.points}')
        else:
            hidden_cards = self.cards.copy()

            hidden_cards.pop()
            # hidden_cards.reverse()
            last_card_point = self.cards[len(self.cards) - 1].get_value()
            hidden_points = self.points - last_card_point

            print('Dealer cards: ' + ', '.join(
                map(str, hidden_cards)) + ' and 1 more hidden card.' + f'. Points: {hidden_points}\n')

    def take_bet(self):
        '''
        Function for accepting a bet
        '''
        while True:
            try:
                print('Your balance: {}'.format(self.chips))
                result = int(input(f'{self.name}, please, place a bet: '))
            except ValueError:
                print('You entered an incorrect value')
                continue
            else:
                if self.chips - result < 0:
                    print("You don't have enough chips")
                    continue
                else:
                    print(f'\nThe bid is accepted! Your new balance: {self.chips} - {result} = {self.chips - result}\n')
                    self.chips -= result
                    break

    def check_aces(self):
        '''
        If there are aces in the hand, we can change the number of points from 11 to 1 per card
        '''
        if self.aces > 0:
            self.points-=10
        # while True:
        #     answer = input(f'\nYou have too many points. But you have an ace. Do you want to change its score value from 11 to 1? (Yes or No)\nYour points will change from {self.points} to {self.points - 10} ')
        #     if answer == 'Yes':
        #         self.points -= 10
        #         break
        #     elif answer == 'No':
        #         break