from random import randrange
from Character import Character
from Constants import *


class Board:

    size_x = 0
    size_y = 0
    max_characters = 20
    active_characters_count = 0
    characters = list()
    created = False
    boardBody = None

    def __init__(self, size_x, size_y):
        self.boardBody = [[None for self.size_y in range(5)] for self.size_x in range(5)]
        self.size_x = size_x
        self.size_y = size_y


    def _is_created(self):
        return self.created

    def add_character_to_board(self, character):

        if self.active_characters_count < self.max_characters and not self._has_character_on_game(character.unique_id):
            self.characters.append(character)
            self._spawn_character(character, TEAM_GOODGUYS)
            self.active_characters_count += 1

            return character
        else:
            return False


    def _has_character_on_game(self, unique_id):
        '''
        :param unique_id:
        :return: Character or False
        '''
        for key, char in self.characters:
                if char.unique_id == unique_id:
                    return char, key

        return False

    def _has_character_on_board(self, unique_id):
        '''
        :param unique_id:
        :return: Tuple(Character, (x,y)) or False

        '''
        for x in range(0, self.size_x):
            for y in range(0, self.size_y):
                if isinstance(Character, self.boardBody[x][y]) and self.boardBody[x][y].unique_id == unique_id:
                    return self.boardBody[x][y], dict({'x': x, 'y': y})
        return False

    def _is_slot_free(self, x, y):
        if isinstance(Character, self.boardBody[x][y]):
            return False
        else:
            return True


    def _spawn_character(self, character, side):

        max_x = 0
        max_y = 0
        min_x = 0
        min_y = 0

        if side == TEAM_GOODGUYS:
            max_x = (self.size_x/2) - 1
            max_y = (self.size_y/2) - 1

            min_x = 0
            min_y = 0
        else:
            max_x = self.size_x
            max_y = self.size_y

            min_x = (self.size_x/2) + 1
            min_y = (self.size_y/2) + 1

        rand_x = randrange(max_x, min_x)
        rand_y = randrange(max_y, min_y)

        if not self._has_character_on_board(character.unique_id) and self._is_slot_free(rand_x, rand_y):
            character.x = rand_x
            character.y = rand_y
            self.boardBody[rand_x][rand_y] = character
        else:
            print('Character already on board or slot is not free')

    def move_character(self, unique_id, x, y):

        if x and y:
            char, pos = self._has_character_on_game(unique_id)

            self.characters[pos].x = x
            self.characters[pos].y = y

        return True








