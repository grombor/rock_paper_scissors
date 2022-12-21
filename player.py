
class Player:
    '''
    Player class is responsible for handling player mechanics.
    '''


    def __init__(self, name='Player', score=0):
        self._name = name
        self._score = score


    def get_name(self):
        return self._name


    def get_score(self):
        return self._score


    def add_point(self):
        self._score += 1
