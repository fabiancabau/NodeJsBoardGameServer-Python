from random import randrange
from flask import json
from Board import Board
from Character import Character
from Constants import *

class Server:

    server_id = None
    user_list = list()
    board = Board(1748, 1344)
    turn_queue = list()
    socket = None

    def __init__(self, socket):
        util = ServerUtil()
        self.server_id = util._generate_server_id()
        self.socket = socket


    def _add_user_to_board(self, character, side):

        self.user_list.append(character)

        if self.board.active_characters_count < self.board.max_characters and not self.board._has_character_on_game(character.unique_id):
            self.board.characters.append(character)
            self.board._spawn_character(character, TEAM_GOODGUYS)
            self.board.active_characters_count += 1
            self._add_user_to_turn_queue(character.unique_id)
            return character
        else:
            return False

    def _add_user_to_turn_queue(self, unique_id):
        self.turn_queue.append(unique_id)

    def _get_current_player_turn(self):
        if self.turn_queue[0]:
            return self.turn_queue[0]
        else:
            return False

    def _on_disconnect_remove_turns(self, unique_id):
        self.turn_queue = filter(lambda a: a != unique_id, self.turn_queue)

    def _move_queue(self, unique_id):

        if unique_id == self.turn_queue[0]:
            last_player = self.turn_queue[0]
            self.turn_queue.pop(0)
            self.turn_queue.append(last_player)

            return self.turn_queue

        else:
            return False


    def _get_user_list(self):

        users = list()

        for user in self.user_list:
            users.append(user.to_JSON())

        return users


class ServerUtil:

    def __init__(self):
        pass

    def _generate_server_id(self):
        text = ""
        possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

        for i in range(0, 5):
            rand = randrange(0, len(possible))
            text += possible[rand]

        return text

    def _remove_unique_id_on_list(self, lista, unique_id):
        return filter(lambda a: a != unique_id, lista)





