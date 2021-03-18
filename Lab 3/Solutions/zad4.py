import random
from typing import List, Sequence


class GameObject:
    def __str__(self):
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        raise NotImplementedError

    def __gt__(self, other) -> bool:
        raise NotImplementedError

    def __lt__(self, other) -> bool:
        return (not self > other) and (not self == other)


class Rock(GameObject):
    def __str__(self):
        return "Rock"

    def __eq__(self, other) -> bool:
        return isinstance(other, Rock)

    def __gt__(self, other) -> bool:
        return isinstance(other, Scissor)


class Paper(GameObject):
    def __str__(self):
        return "Paper"

    def __eq__(self, other) -> bool:
        return isinstance(other, Paper)

    def __gt__(self, other) -> bool:
        return isinstance(other, Rock)


class Scissor(GameObject):
    def __str__(self):
        return "Scissor"

    def __eq__(self, other) -> bool:
        return isinstance(other, Scissor)

    def __gt__(self, other) -> bool:
        return isinstance(other, Paper)


class Player:
    def __init__(self, game_objects: Sequence[GameObject], player_name):
        self.name = player_name
        self._game_objects = game_objects

    def get_choice(self) -> GameObject:
        raise NotImplementedError

    def __str__(self):
        return self.name

    def send_stats(self, stats):
        raise NotImplementedError


def get_int_from_input(text) -> int:
    return int(input(text))


class ConsolePlayer(Player):

    def send_stats(self, stats):
        print(f"Your stats: {stats}")

    def get_choice(self) -> GameObject:
        text = f"{self.name}\n"
        for o, i in zip(self._game_objects, range(len(self._game_objects))):
            text += f"{str(i)} => {str(o)}\n"
        int_from_input = get_int_from_input(f"{text} Choose: ")
        return self._game_objects[int_from_input]


class ComputerPlayer(Player):
    def send_stats(self, stats):
        pass

    def get_choice(self) -> GameObject:
        return random.choice(self._game_objects)


class RockPaperScissorGame:
    def __init__(self, players: List[Player], rounds: int):
        if rounds < 0:
            raise AttributeError
        self._players = players
        self._stats = []
        for _ in self._players:
            self._stats.append({"wins": 0, "draws": 0, "losses": 0})
        self._all_rounds = rounds
        self._done_rounds = 0

    def ended(self) -> bool:
        return self._all_rounds == self._done_rounds

    def nextRound(self) -> None:
        choices = []
        for player in self._players:
            choices.append(player.get_choice())
        for choice, player_stats in zip(choices, self._stats):
            for other_player_choice in choices:
                if choice > other_player_choice:
                    player_stats["wins"] += 1
                elif choice == other_player_choice:
                    player_stats["draws"] += 1
                else:
                    player_stats["losses"] += 1
            player_stats["draws"] -= 1

        for player, player_stats in zip(self._players, self._stats):
            player.send_stats(player_stats)
        self._done_rounds += 1

    def get_stats_for_player(self, player: Player):
        return self._stats[self._players.index(player)]


def calc_points(stats):
    return stats["wins"] - stats["losses"] + (stats["draws"] / 2)


def main():
    rounds: int = int(input("Rounds number: "))
    game_objects = [Rock(), Paper(), Scissor()]
    players: List[Player] = [ConsolePlayer(game_objects, "player"),
                             ComputerPlayer(game_objects, "computer")]
    game = RockPaperScissorGame(players, rounds)
    while not game.ended():
        game.nextRound()
    players_with_stats = [(player, game.get_stats_for_player(player)) for player in players]
    for player, stats in sorted(players_with_stats, key=lambda t: calc_points(t[1])):
        print(f"{player} => {stats}")
    input()


if __name__ == '__main__':
    main()
