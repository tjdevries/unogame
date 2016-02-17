import random
from unogame import utils


class CustomDict(dict):
    __version__ = '0.3.0'

    def random_key(self):
        random_key = random.sample(self.keys(), 1)[0]
        return random_key

    def random_card(self,  method=None):
        key = self.random_key()
        if method is 'simple':
            pair = self[key][0]
        else:
            pair = None
        return pair

    def suck(self,  ext_dict):
        '''Clones another dictionary'''
        for key in ext_dict:
            if key not in self:
                self[key] = []
            for value in ext_dict[key]:
                self[key].append(value)

    def needs_reshuffling(self):
        if utils.stack.count(self) == 2:
            return True
        return False

    def reshuffle(self,  stack):
        self.suck(stack)

    def refresh(self):
        for k,  v in self.items():
            if len(v) == 0:
                del self[k]
