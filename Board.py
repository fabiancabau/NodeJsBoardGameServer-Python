from random import randrange, randint
from Character import Character
from Constants import *
import json

class Board:

    size_x = 0
    size_y = 0
    max_characters = 20
    active_characters_count = 0
    characters = list()
    created = False
    boardBody = None

    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.boardBody = [[None for a in range(self.size_y)] for b in range(self.size_x)]
        print('{0}').format(len(self.boardBody))



    def _is_created(self):
        return self.created


    def _has_character_on_game(self, unique_id):
        '''
        :param unique_id:
        :return: Character or False
        '''
        for key, char in enumerate(self.characters):
                if char.unique_id == unique_id:
                    return char, key

        return False

    def _has_character_on_board(self, unique_id):
        '''
        :param unique_id:
        :return: Tuple(Character, (x,y)) or False

        '''
        for x in range(0, len(self.boardBody)):
            for y in range(0, len(self.boardBody[x])):
                if isinstance(self.boardBody[x][y], Character) and self.boardBody[x][y].unique_id == unique_id:
                    return self.boardBody[x][y], dict({'x': x, 'y': y})
        return False

    def _is_slot_free(self, x, y):
        print(self.boardBody)
        if isinstance(self.boardBody[x][y], Character):
            return False
        else:
            return True


    def _spawn_character(self, character, side):
        import math

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

        rand_x = randint(math.floor(min_x), math.floor(max_x))
        rand_y = randint(math.floor(min_y), math.floor(max_y))

        if not self._has_character_on_board(character.unique_id):
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

        return False

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)








