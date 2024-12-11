import unittest
import blackjack
from blackjack import EmptyDeck


class TestBlackjack(unittest.TestCase):
    def setUp(self):
        self._game = blackjack.BlackJack()

    def test_check_win_or_lose(self):
        win_list_one = [("Hearts", 2, 2), ("Clubs", 3, 3), ("Clubs", 5, 5), ("Diamonds", 6, 6), ("Diamonds", 5, 5)]
        win_list_two = [("Spades", 1, 11), ("Clubs", 11, 10)]
        win_list_three = [("Hearts", 2, 2), ("Clubs", 3, 3), ("Clubs", 1, 11), ("Diamonds", 4, 4), ("Spades", 1, 11)]

        self.assertEqual(self._game.check_win_or_lose(win_list_one), 'win')
        self.assertEqual(self._game.check_win_or_lose(win_list_two), 'win')
        self.assertEqual(self._game.check_win_or_lose(win_list_three), 'win')

        lose_list_one = [("Spades", 1, 11), ("Spades", 2, 2), ("Spades", 3, 3), ("Spades", 4, 4), ("Spades", 5, 5), ("Spades", 6, 6), ("Spades", 7, 7)]
        lose_list_two = [("Hearts", 2, 2), ("Clubs", 3, 3), ("Clubs", 1, 11), ("Diamonds", 5, 4), ("Spades", 1, 11), ("Spades", 2, 2), ("Diamonds", 9, 9)]
        lose_list_three = [("Spades", 1, 11), ("Clubs", 11, 10), ("Diamonds", 11, 10), ("Spades", 1, 11)]

        self.assertEqual(self._game.check_win_or_lose(lose_list_one), 'lose')
        self.assertEqual(self._game.check_win_or_lose(lose_list_two), 'lose')
        self.assertEqual(self._game.check_win_or_lose(lose_list_three), 'lose')

        score_list_one = [("Hearts", 2, 2), ("Clubs", 5, 5)]
        score_list_two = [("Hearts", 2, 2), ("Clubs", 3, 3), ("Clubs", 1, 11), ("Spades", 2, 2)]
        score_list_three = [("Hearts", 2, 2), ("Diamonds", 3, 3), ("Spades", 8, 8)]

        self.assertEqual(self._game.check_win_or_lose(score_list_one), 7)
        self.assertEqual(self._game.check_win_or_lose(score_list_two), 18)
        self.assertEqual(self._game.check_win_or_lose(score_list_three), 13)

    def test_game_reset(self):
        self._game._dealer_hand = [("Hearts", 2, 2), ("Clubs", 3, 3), ("Clubs", 5, 5), ("Diamonds", 6, 6), ("Diamonds", 5, 5)]
        self._game._player_hand = [("Spades", 1, 11), ("Clubs", 11, 10)]

        self._game.game_reset()

        self.assertEqual(self._game._dealer_hand, [])
        self.assertEqual(self._game._player_hand, [])

    def test_true_reset(self):
        self._game._dealer_hand = [("Clubs", 3, 3), ("Clubs", 5, 5), ("Diamonds", 6, 6), ("Diamonds", 5, 5)]
        self._game._player_hand = [("Spades", 1, 11), ("Clubs", 11, 10)]
        self._discard_pile = [("Spades", 1, 11), ("Spades", 2, 2), ("Spades", 3, 3), ("Spades", 4, 4), ("Spades", 5, 5), ("Spades", 6, 6), ("Spades", 7, 7)]

        self._game.true_reset()

        self.assertEqual(self._game._dealer_hand, [])
        self.assertEqual(self._game._player_hand, [])
        self.assertEqual(self._game._discard_pile, [])
        self.assertEqual(self._game._deck, [("Spades", 1, 11), ("Spades", 2, 2), ("Spades", 3, 3), ("Spades", 4, 4), ("Spades", 5, 5), ("Spades", 6, 6), ("Spades", 7, 7),
                      ("Spades", 8, 8), ("Spades", 9, 9), ("Spades", 10, 10), ("Spades", 11, 10), ("Spades", 12, 10), ("Spades", 13, 10),
                      ("Clubs", 1, 11), ("Clubs", 2, 2), ("Clubs", 3, 3), ("Clubs", 4, 4), ("Clubs", 5, 5), ("Clubs", 6, 6),
                      ("Clubs", 7, 7), ("Clubs", 8, 8), ("Clubs", 9, 9), ("Clubs", 10, 10), ("Clubs", 11, 10), ("Clubs", 12, 10),
                      ("Clubs", 13, 10),
                      ("Diamonds", 1, 11), ("Diamonds", 2, 2), ("Diamonds", 3, 3), ("Diamonds", 4, 4), ("Diamonds", 5, 5), ("Diamonds", 6, 6),
                      ("Diamonds", 7, 7), ("Diamonds", 8, 8), ("Diamonds", 9, 9), ("Diamonds", 10, 10), ("Diamonds", 11, 10), ("Diamonds", 12, 10),
                      ("Diamonds", 13, 10),
                      ("Hearts", 1, 11), ("Hearts", 2, 2), ("Hearts", 3, 3), ("Hearts", 4, 4), ("Hearts", 5, 5), ("Hearts", 6, 6), ("Hearts", 7, 7),
                      ("Hearts", 8, 8), ("Hearts", 9, 9), ("Hearts", 10, 10), ("Hearts", 11, 10), ("Hearts", 12, 10), ("Hearts", 13, 10)])

    def test_deal_player(self):
        self.assertTrue(len(self._game._player_hand) == 0)

        self._game.deal_player()
        self.assertTrue(len(self._game._player_hand) == 1)

        self._game.deal_player()
        self.assertTrue(len(self._game._player_hand) == 2)

        self._game._deck = [("Hearts", 1, 11)]

        self._game.deal_player()
        self.assertTrue(len(self._game._player_hand) == 3)

        with self.assertRaises(EmptyDeck):
            self._game.deal_player()

    def test_deal_dealer(self):
        self.assertTrue(len(self._game._dealer_hand) == 0)

        self._game.deal_dealer()
        self.assertTrue(len(self._game._dealer_hand) == 1)

        self._game.deal_dealer()
        self.assertTrue(len(self._game._dealer_hand) == 2)

        self._game._deck = [("Hearts", 1, 11)]

        self._game.deal_dealer()
        self.assertTrue(len(self._game._dealer_hand) == 3)

        with self.assertRaises(EmptyDeck):
            self._game.deal_dealer()

if __name__ == '__main__':
    unittest.main()