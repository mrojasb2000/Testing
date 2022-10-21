# contents of test_player_mechanics.py
# Howto run: pytest test_player_mechanics.py

class Player:
    health = 100


class Undead:
    def hit(player):
        player.health = 80
        return player


def create_player():
    return Player()


def create_undead():
    return Undead


def test_player_hit():
    player = create_player()
    assert player.health == 100
    undead = create_undead()
    undead.hit(player)
    assert player.health == 80
