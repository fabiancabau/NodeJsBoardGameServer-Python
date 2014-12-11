from Constants import *
from random import randrange

class Character:

    unique_id = None
    nickname = ''
    x = 0
    y = 0
    heroImgPos = None


    def __init__(self, unique_id, nickname, x, y, heroImgPos):
        self.unique_id = unique_id
        self.nickname = nickname
        self.x = 0
        self.y = 0
        self.heroImgPos = heroImgPos


    def _get_random_hero_img_pos(self):
        random = randrange(0, len(heroImageData))
        return heroImageData[random]
