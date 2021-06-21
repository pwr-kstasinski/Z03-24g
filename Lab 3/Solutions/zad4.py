import random
from typing import List, Sequence, Dict, Set


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

    def __str__(self) -> str:
        return self.name

    def send_stats(self, stats: Dict[str, Dict[str, int]]) -> None:
        raise NotImplementedError

    def send_winner(self, winner: str) -> None:
        raise NotImplementedError

    def __hash__(self):
        return hash(self.name)


def get_int_from_input(text) -> int:
    return int(input(text))


class ConsolePlayer(Player):

    def send_winner(self, winner: str) -> None:
        input(f"Winner: {winner}")

    def send_stats(self, stats: Dict[str, Dict[str, int]]) -> None:
        for key, value in stats.items():
            print(f"{key} => {value}")

    def get_choice(self) -> GameObject:
        text = f"{self.name}\n"
        for o, i in zip(self._game_objects, range(len(self._game_objects))):
            text += f"{str(i)} => {str(o)}\n"
        int_from_input = get_int_from_input(f"{text} Choose: ")
        return self._game_objects[int_from_input]


class ComputerPlayer(Player):

    def send_winner(self, winner: str) -> None:
        pass

    def send_stats(self, stats: Dict[str, Dict[str, int]]):
        pass

    def get_choice(self) -> GameObject:
        return random.choice(self._game_objects)


class RockPaperScissorGame:
    def __init__(self, players: Set[Player], rounds: int):
        if rounds < 0:
            raise AttributeError
        self._players = list(players)
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
        self.send_stats_to_players()
        self._done_rounds += 1

    def get_stats_for_player(self, player: Player) -> Dict[str, int]:
        return self._stats[self._players.index(player)]

    def send_stats_to_players(self) -> None:
        stats = {}
        for player, player_stats in zip(self._players, self._stats):
            stats[player.name] = player_stats
        for player in self._players:
            player.send_stats(stats)

    def get_winner(self) -> Player:
        points_with_index = [(calc_points(stats), i) for i, stats in enumerate(self._stats)]
        winner_index = max(points_with_index, key=lambda pair: pair[0])[1]
        winner = self._players[winner_index]
        return winner

    def show_winner(self) -> None:
        winner = self.get_winner()
        for player in self._players:
            player.send_winner(winner.name)


def calc_points(stats):
    return stats["wins"] - stats["losses"] + (stats["draws"] / 2)


def main():
    rounds: int = int(input("Rounds number: "))
    player_name = "player"
    computer_name = "computer"
    game_objects: Sequence[GameObject] = [Rock(), Paper(), Scissor()]
    players: Set[Player] = {ConsolePlayer(game_objects, player_name), ComputerPlayer(game_objects, computer_name)}
    game = RockPaperScissorGame(players, rounds)
    while not game.ended():
        game.nextRound()
    game.show_winner()
    input()


if __name__ == '__main__':
    main()
