
class HashTable():
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size
        pass

    def _HashFunc(self, key):
        groove = key % self.size
        return groove

    def _RehashFunc(self, oldKey, step=1):
        groove_new = self._HashFunc(oldKey+step)
        return groove_new

    def put(self, key, val):

        pass

    def get(self, key):

        pass

    def __setitem__(self, key, value):

        pass

    def __getitem__(self, key):

        pass


if __name__ == '__main__':

    pass
