from Constants import *
from random import randrange
import json

class Character:

    unique_id = None
    nickname = ''
    x = 0
    y = 0
    heroImgPos = None


    def __init__(self, unique_id, nickname, x, y):
        self.unique_id = unique_id
        self.nickname = nickname
        self.x = 0
        self.y = 0
        self.heroImgPos = self._get_random_hero_img_pos()


    def _get_random_hero_img_pos(self):
        random = randrange(0, len(heroImageData))
        return heroImageData[random]


    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
