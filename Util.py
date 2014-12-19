from random import randrange
import json

class Util:

    def __init__(self):
        pass

    def _generate_socket_id(self):
        text = ""
        possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

        for i in range(0, 15):
            rand = randrange(0, len(possible))
            text += possible[rand]

        return text


    def to_JSON(self, obj):
        return json.dumps(obj, default=lambda o: o.__dict__, sort_keys=True, indent=4)