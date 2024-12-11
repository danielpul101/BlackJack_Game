import random

SUIT = 0
NUMBER = 1
VALUE = 2

class EmptyDeck(Exception):
    pass

class BlackJack:
    def __init__(self):
        """makes a deck of cards, and sets both hands and the discard pile to an empty list"""
        self._deck = [("Spades", 1, 11), ("Spades", 2, 2), ("Spades", 3, 3), ("Spades", 4, 4), ("Spades", 5, 5), ("Spades", 6, 6), ("Spades", 7, 7), ("Spades", 8, 8), ("Spades", 9, 9), ("Spades", 10, 10), ("Spades", 11, 10), ("Spades", 12, 10), ("Spades", 13, 10),
                      ("Clubs", 1, 11), ("Clubs", 2, 2), ("Clubs", 3, 3), ("Clubs", 4, 4), ("Clubs", 5, 5), ("Clubs", 6, 6), ("Clubs", 7, 7), ("Clubs", 8, 8), ("Clubs", 9, 9), ("Clubs", 10, 10), ("Clubs", 11, 10), ("Clubs", 12, 10), ("Clubs", 13, 10),
                      ("Diamonds", 1, 11), ("Diamonds", 2, 2), ("Diamonds", 3, 3), ("Diamonds", 4, 4), ("Diamonds", 5, 5), ("Diamonds", 6, 6), ("Diamonds", 7, 7), ("Diamonds", 8, 8), ("Diamonds", 9, 9), ("Diamonds", 10, 10), ("Diamonds", 11, 10), ("Diamonds", 12, 10), ("Diamonds", 13, 10),
                      ("Hearts", 1, 11), ("Hearts", 2, 2), ("Hearts", 3, 3), ("Hearts", 4, 4), ("Hearts", 5, 5), ("Hearts", 6, 6), ("Hearts", 7, 7), ("Hearts", 8, 8), ("Hearts", 9, 9), ("Hearts", 10, 10), ("Hearts", 11, 10), ("Hearts", 12, 10), ("Hearts", 13, 10)]

        self._dealer_hand = []
        self._player_hand = []
        self._discard_pile = []

    def p_hand(self):
        """returns the player's hand"""
        return self._player_hand

    def d_hand(self):
        """returns the dealer's hand"""
        return self._dealer_hand

    def true_reset(self):
        """resets the deck completely, and both ands and the discard pile; used when deck finishes"""
        self._deck = [("Spades", 1, 11), ("Spades", 2, 2), ("Spades", 3, 3), ("Spades", 4, 4), ("Spades", 5, 5), ("Spades", 6, 6), ("Spades", 7, 7), ("Spades", 8, 8), ("Spades", 9, 9), ("Spades", 10, 10), ("Spades", 11, 10), ("Spades", 12, 10), ("Spades", 13, 10),
                      ("Clubs", 1, 11), ("Clubs", 2, 2), ("Clubs", 3, 3), ("Clubs", 4, 4), ("Clubs", 5, 5), ("Clubs", 6, 6), ("Clubs", 7, 7), ("Clubs", 8, 8), ("Clubs", 9, 9), ("Clubs", 10, 10), ("Clubs", 11, 10), ("Clubs", 12, 10), ("Clubs", 13, 10),
                      ("Diamonds", 1, 11), ("Diamonds", 2, 2), ("Diamonds", 3, 3), ("Diamonds", 4, 4), ("Diamonds", 5, 5), ("Diamonds", 6, 6), ("Diamonds", 7, 7), ("Diamonds", 8, 8), ("Diamonds", 9, 9), ("Diamonds", 10, 10), ("Diamonds", 11, 10), ("Diamonds", 12, 10), ("Diamonds", 13, 10),
                      ("Hearts", 1, 11), ("Hearts", 2, 2), ("Hearts", 3, 3), ("Hearts", 4, 4), ("Hearts", 5, 5), ("Hearts", 6, 6), ("Hearts", 7, 7), ("Hearts", 8, 8), ("Hearts", 9, 9), ("Hearts", 10, 10), ("Hearts", 11, 10), ("Hearts", 12, 10), ("Hearts", 13, 10)]
        self._dealer_hand = []
        self._player_hand = []
        self._discard_pile = []

    def game_reset(self):
        """resets both hands; used when singular game finishes"""
        self._dealer_hand = []
        self._player_hand = []

    def check_win_or_lose(self, hand: list):
        """checks whether the hand wins, loses, or the score given the hand"""
        hand_copy = hand[:]
        hand_copy.sort(key=lambda y: y[VALUE]) #now goes from least to greatest in value, 2-11
        score = 0

        for x in hand_copy:
            score += x[VALUE]
            if score > 21:
                if x[NUMBER] == 1:
                    score -= 10
                if score > 21:
                    return 'lose'
        if score == 21:
            return 'win'
        else:
            return score

    def deal_player(self):
        """deals one card to the player if possible, else raises an error"""
        if len(self._deck) >= 1:
            random.shuffle(self._deck)
            self._player_hand.append(self._deck.pop(0))
        else:
            raise EmptyDeck

    def deal_dealer(self):
        """deals one card to the dealer if possible, else raises an error"""
        if len(self._deck) >= 1:
            random.shuffle(self._deck)
            self._dealer_hand.append(self._deck.pop(0))
        else:
            raise EmptyDeck

    def score_player(self):
        """returns the score of the player"""
        hand_copy = self._player_hand[:]
        hand_copy.sort(key=lambda z: z[VALUE])  # now goes from least to greatest in value, 2-11
        score = 0

        for x in hand_copy:
            score += x[VALUE]
            if score > 21:
                if x[NUMBER] == 1:
                    score -= 10
        return score

    def score_dealer(self):
        """returns the score of the dealer"""
        hand_copy = self._dealer_hand[:]
        hand_copy.sort(key=lambda a: a[VALUE])  # now goes from least to greatest in value, 2-11
        score = 0

        for x in hand_copy:
            score += x[VALUE]
            if score > 21:
                if x[NUMBER] == 1:
                    score -= 10
        return score

    def display_cards(self, hand: list):
        """displays the cards in the terminal in a fancy way if possible"""
        for x in hand:
            suit = x[SUIT]
            if x[NUMBER] == 1:
                rank = 'A'

            elif x[NUMBER] == 11:
                rank = 'J'

            elif x[NUMBER] == 12:
                rank = 'Q'

            elif x[NUMBER] == 13:
                rank = 'K'

            else:
                rank = f'{x[NUMBER]}'

            suits = {
                "Spades": "♠",
                "Hearts": "♥",
                "Diamonds": "♦",
                "Clubs": "♣"
            }

            # Check if the suit is valid

            # Color for suits
            red_suits = {"Hearts", "Diamonds"}
            suit_symbol = suits[suit]
            color_start = "\033[91m" if x[SUIT] in red_suits else "\033[97m"  # Red for hearts/diamonds, white for others
            color_reset = "\033[0m"

            # Card template
            card = f"""
                ┌───────┐
                │{rank:<2}     │
                │   {suit_symbol}   │
                │     {rank:>2}│
                └───────┘
                """
            print(color_start + card + color_reset)

def compare_hands(game: BlackJack):
    """compares the player and dealer hands"""
    try:
        player_hand = game.check_win_or_lose(game._player_hand)
        dealer_hand = game.check_win_or_lose(game._dealer_hand)

        if player_hand > dealer_hand or (game.score_player() == 21 and game.score_dealer() != 21):
            return 'player'
        elif player_hand < dealer_hand or (game.score_player() != 21 and game.score_dealer() == 21):
            return 'dealer'
        elif player_hand == dealer_hand:
            return 'push'
    except:
        pass

def run():
    game = BlackJack()

    game.deal_player()
    game.deal_player()

    game.deal_dealer()
    game.deal_dealer()

    turn = 0

    while True:
        player_hand = game.p_hand()
        dealer_hand = game.d_hand()

        print('Your hand:')
        game.display_cards(player_hand)

        print('\n')
        print('Dealer\'s hand:')
        game.display_cards(dealer_hand[:1])
        print(f"""
                ┌───────┐
                │       │
                │       │
                │       │
                └───────┘
                """)

        if game.score_dealer() == 21 and game.score_player() == 21:
            print('Wow! You pushed with a blackjack!')
            game.display_cards(game._player_hand)
            game.display_cards(game._dealer_hand)
            while True:
                play_again = input("Do you want to play again? (y/n)").lower()

                if play_again == 'y':
                    game.true_reset()
                    game.deal_player()
                    game.deal_player()

                    game.deal_dealer()
                    game.deal_dealer()
                    return True
                elif play_again == 'n':
                    return None
                else:
                    print('Invalid input, try again')


        elif game.score_player() == 21:
            print('You won with a blackjack!')
            game.display_cards(game._player_hand)
            while True:
                play_again = input("Do you want to play again? (y/n)").lower()

                if play_again == 'y':
                    game.true_reset()
                    game.deal_player()
                    game.deal_player()

                    game.deal_dealer()
                    game.deal_dealer()
                    return True
                elif play_again == 'n':
                    return None
                else:
                    print('Invalid input, try again')

        elif game.score_dealer() == 21:
            print('Sorry, the dealer won with a blackjack!')
            game.display_cards(game._dealer_hand)
            while True:
                play_again = input("Do you want to play again? (y/n)").lower()

                if play_again == 'y':
                    game.true_reset()
                    game.deal_player()
                    game.deal_player()

                    game.deal_dealer()
                    game.deal_dealer()
                    return True
                elif play_again == 'n':
                    return None
                else:
                    print('Invalid input, try again')

        result = input("Do you want to 'hit' or 'stand'? ").lower()

        if result == 'hit' or result == 'stand':
            if result == 'hit':
                turn += 1
                game.deal_player()
                p_result = game.check_win_or_lose(player_hand)
                if p_result == 'win' or p_result == 'lose':
                    print('Your hand:')
                    game.display_cards(game._player_hand)
                    print()

                    if p_result == 'win':
                        d_result = game.check_win_or_lose(dealer_hand)
                        if d_result == 'win':
                            print('Wow, you both had 21 and pushed!')
                        else:
                            print(f'You had {game.score_player()} points, while the dealer had {game.score_dealer()} points.')
                            print('You won!')

                    elif p_result == 'lose':
                        print(f'You had {game.score_player()} points, while the dealer had {game.score_dealer()} points.')
                        print('You lost!')

                    while True:
                        play_again = input("Do you want to play again? (y/n)").lower()

                        if play_again == 'y':
                            game.true_reset()
                            game.deal_player()
                            game.deal_player()

                            game.deal_dealer()
                            game.deal_dealer()
                            return True
                        elif play_again == 'n':
                            return None
                        else:
                            print('Invalid input, try again')

            elif result == 'stand':
                turn += 1
                while game.check_win_or_lose(dealer_hand) < 17:
                    print('Dealer\'s hand:')
                    game.display_cards(game._dealer_hand)
                    game.deal_dealer()

                    if type(game.check_win_or_lose(dealer_hand)) != int:
                        print('Dealer\'s hand:')
                        game.display_cards(game._dealer_hand)
                        break

                outcome = compare_hands(game)
                print(f'You had {game.score_player()} points, while the dealer had {game.score_dealer()} points.')
                if turn == 1:
                    game.display_cards(game._dealer_hand)
                if outcome == 'player' or game.score_dealer() > 21:
                    print('You won!')
                elif outcome == 'dealer':
                    print('You lost!')
                elif outcome == 'push':
                    print('You pushed!')


                while True:
                    play_again = input("Do you want to play again? (y/n)").lower()

                    if play_again == 'y':
                        game.true_reset()
                        game.deal_player()
                        game.deal_player()

                        game.deal_dealer()
                        game.deal_dealer()
                        return True
                    elif play_again == 'n':
                        return None
                    else:
                        print('Invalid input, try again')


        else:
            print('Invalid input, try again')

if __name__ == '__main__':
     play = run()
     while play:
         play = run()