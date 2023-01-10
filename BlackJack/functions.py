def hit_or_stay():
    '''
    This function is responsible for choosing the move
    '''
    while True:
        choose = input('\nChoose a move - Hit or Stay: ')
        if choose in ('Hit', 'Stay'):
            break
        else:
            print('There is no such move')
            continue

    if choose == 'Hit':
        return True
    elif choose == 'Stay':
        return False


def hit(deck, hand):
    '''
    This function is responsible for the move Hit
    '''
    hand.add_card(deck.deal())


def player_lose(points):
    '''
    If player lose
    '''
    print(f"Your points: {points} . That's more than 21. Unfortunately, you lost")


def player_win():
    '''
    If player win
    '''
    print("Congratulations, you have won!!!")


def dealer_lose(points):
    '''
    If dealerlose
    '''
    print(f"Dealer points: {points} . That's more than 21. He lost, you win :)")


def dealer_win():
    '''
    If dealer lose
    '''
    print('The dealer won')