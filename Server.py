from Board import Board
from Character import Character


class Server:

    server_id = None
    user_list = list()
    board = Board(1748, 1344)
    turn_queue = list()

    def __init__(self):
        pass


    def _add_user_to_list(self, user_info, unique_id):
        character = Character(unique_id, user_info.get('nickname'), 0, 0, user_info.get('heroImgPos'))
        self.user_list.append(character)
        self._add_user_to_turn_queue(character.unique_id)

        return character

    def _add_user_to_turn_queue(self, unique_id):
        self.turn_queue.append(unique_id)

    def _get_current_player_turn(self):
        if self.turn_queue[0]:
            return self.turn_queue[0]
        else:
            return False

    def _on_disconnect_remove_turns(self, unique_id):
        return (lambda a: a != unique_id, self.turn_queue)

    def move_queue(self, unique_id):

        if unique_id == self.turn_queue[0]:
            last_player = self.turn_queue[0]
            self.turn_queue.pop(0)
            self.turn_queue.append(last_player)

            return self.turn_queue

        else:
            return False




