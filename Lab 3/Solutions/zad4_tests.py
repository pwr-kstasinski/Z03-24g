import unittest
from unittest.mock import patch, MagicMock

from zad4 import *


class GameObjectsTests(unittest.TestCase):
    def test_rock_wins_with_scissor(self):
        self.assertTrue(Rock() > Scissor())
        self.assertFalse(Rock() == Scissor())

    def test_rock_losses_with_paper(self):
        self.assertTrue(Rock() < Paper())
        self.assertFalse(Rock() == Paper())

    def test_rock_draw_with_rock(self):
        self.assertTrue(Rock() == Rock())
        self.assertFalse(Rock() > Rock())
        self.assertFalse(Rock() < Rock())

    def test_rock_str(self):
        self.assertEqual("Rock", str(Rock()))

    def test_scissor_wins_with_paper(self):
        self.assertTrue(Scissor() > Paper())
        self.assertFalse(Scissor() == Paper())

    def test_scissor_losses_with_rock(self):
        self.assertTrue(Scissor() < Rock())
        self.assertFalse(Scissor() == Rock())

    def test_scissor_draw_with_scissor(self):
        self.assertTrue(Scissor() == Scissor())
        self.assertFalse(Scissor() > Scissor())
        self.assertFalse(Scissor() < Scissor())

    def test_scissor_str(self):
        self.assertEqual("Scissor", str(Scissor()))

    def test_paper_wins_with_rock(self):
        self.assertTrue(Paper() > Rock())
        self.assertFalse(Paper() == Rock())

    def test_paper_losses_with_scissor(self):
        self.assertTrue(Paper() < Scissor())
        self.assertFalse(Paper() == Scissor())

    def test_paper_draw_with_paper(self):
        self.assertTrue(Paper() == Paper())
        self.assertFalse(Paper() < Paper())
        self.assertFalse(Paper() > Paper())

    def test_paper_str(self):
        self.assertEqual("Paper", str(Paper()))


class ComputerPlayerTests(unittest.TestCase):
    game_objects = [Rock(), Paper(), Scissor()]

    def setUp(self) -> None:
        self.player = ComputerPlayer(self.game_objects, "player")

    def test_random_choose(self):
        chooses = []
        for i in range(10):
            choice = self.player.get_choice()
            if not any(filter(lambda x: x == choice, chooses)):
                chooses.append(choice)
        self.assertFalse(len(chooses) == 1)
        self.assertFalse(len(chooses) > len(self.game_objects))


class ConsolePlayerTests(unittest.TestCase):
    game_objects = [Rock(), Paper(), Scissor()]

    def setUp(self) -> None:
        self.player = ConsolePlayer(self.game_objects, "player")

    @patch('zad4.get_int_from_input', return_value=0)
    def test_answer_rock(self, input):
        choice = self.player.get_choice()
        self.assertEqual(self.game_objects[0], choice)

    @patch('zad4.get_int_from_input', return_value=1)
    def test_answer_paper(self, input):
        choice = self.player.get_choice()
        self.assertEqual(self.game_objects[1], choice)

    @patch('zad4.get_int_from_input', return_value=2)
    def test_answer_scissor(self, input):
        choice = self.player.get_choice()
        self.assertEqual(self.game_objects[2], choice)


class GameTest(unittest.TestCase):
    def test_round_number_error(self):
        self.assertRaises(AttributeError, lambda: RockPaperScissorGame([], -1))

    def test_ended(self):
        game = RockPaperScissorGame([], 0)
        self.assertTrue(game.ended())

    def test_not_ended(self):
        game = RockPaperScissorGame([], 1)
        self.assertFalse(game.ended())

    def test_next_round_get_choise(self):
        player_mock = Player([], "player")
        player_mock.get_choice = MagicMock(return_value=Rock())
        game = RockPaperScissorGame([player_mock], 10)

        game.nextRound()

        player_mock.get_choice.assert_called_once()
        self.assertEqual(1, game._done_rounds)

    def test_next_round_get_stats(self):
        first_player_mock = Player([], "player")
        first_player_mock.get_choice = MagicMock(return_value=Rock())
        second_player_mock = Player([], "player")
        second_player_mock.get_choice = MagicMock(return_value=Paper())
        game = RockPaperScissorGame([first_player_mock, second_player_mock], 10)

        game.nextRound()

        self.assertEqual({"wins": 0, "draws": 0, "losses": 1}, game.get_stats_for_player(first_player_mock))
        self.assertEqual({"wins": 1, "draws": 0, "losses": 0}, game.get_stats_for_player(second_player_mock))

    def test_next_round_get_stats_more_players(self):
        first = Player([], "player")
        first.get_choice = MagicMock(return_value=Rock())
        second = Player([], "player")
        second.get_choice = MagicMock(return_value=Paper())
        third = Player([], "player")
        third.get_choice = MagicMock(return_value=Scissor())
        fourth = Player([], "player")
        fourth.get_choice = MagicMock(return_value=Scissor())
        game = RockPaperScissorGame([first, second, third, fourth], 10)

        game.nextRound()

        self.assertEqual({"wins": 2, "draws": 0, "losses": 1}, game.get_stats_for_player(first))
        self.assertEqual({"wins": 1, "draws": 0, "losses": 2}, game.get_stats_for_player(second))
        self.assertEqual({"wins": 1, "draws": 1, "losses": 1}, game.get_stats_for_player(third))
        self.assertEqual({"wins": 1, "draws": 1, "losses": 1}, game.get_stats_for_player(fourth))


if __name__ == '__main__':
    unittest.main()
