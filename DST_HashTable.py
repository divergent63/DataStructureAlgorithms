
"""
ADT Map to realize a HashTable
"""
class HashTable():
    def __init__(self, size=11):
        self.size = size
        self.slots = [None] * self.size
        self.samples = [None] * self.size
        pass

    def _HashFunc(self, key):
        groove = key % self.size
        return groove

    def _RehashFunc(self, oldKey, step=1):
        groove_new = (oldKey+step) % self.size
        return groove_new

    def put(self, key, val):
        hash = self._HashFunc(key)
        # 空槽，直接插入值
        if self.slots[hash] is None and self.samples[hash] is None:
            print('origin key:  ', key, '   hash value:  ', hash, '   hash sample:  ', val)
            self.samples[hash] = val
            self.slots[hash] = key

        else:

            # 槽不空且为当前key
            if self.slots[hash] == key:
                print('origin key:  ', key, '   hash value:  ', hash, '   hash sample:  ', val)
                self.samples[hash] = val

            # 槽不空且为另外的key(冲突)，加一法解决冲突
            else:
                while self.slots[hash]:
                    hash = self._RehashFunc(hash)
                print('origin key:  ', key, '   hash value:  ', hash, '   hash sample:  ', val)
                self.samples[hash] = val
                self.slots[hash] = key
        return None

    def get(self, key):
        hash = self._HashFunc(key)
        possible = self.samples[hash]

        # HashTable中存储的键与当前键一致，当前hash值索引的sample是正确的
        if self.slots[hash] == key:
            return possible

        # HashTable中存储的键与当前键不一致，需要重新hash直到存储的键与当前键一致，此时再按照新的hash值重新索引sample
        else:
            while self.slots[hash] != None and self.slots[hash] != key:
                hash = self._RehashFunc(hash)
            if self.slots[hash] is None:
                return None
            possible = self.samples[hash]
            return possible

    def __setitem__(self, key, value):
        self.put(key, value)
        return None

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        hash = self._HashFunc(key)
        if self.slots[hash] == key:
            self.slots[hash] = None
            self.samples[hash] = None
        else:
            while self.slots[hash] != None and self.slots[hash] != key:
                hash = self._RehashFunc(hash)
            if self.slots[hash] is None:
                print('hash table has no key named %d' % key)
                return None
            self.slots[hash] = None
            self.samples[hash] = None
        return None

    def __len__(self):
        return self.size

    def __contains__(self, val):
        if val in self.samples:
            return True
        else:
            return False


if __name__ == '__main__':
    ht = HashTable()
    ht.put(22, 'cat')
    ht.put(3, 'dog')
    # ht.put(33, 'pig')
    ht[33] = 'pig'
    ht.put(35, 'duck')
    # print(ht[35])
    ht[83] = 'sheep'            # influenced by __setitem__
    ht[35] = 'human'
    ht[44] = 'rabbit'
    ht[55] = 'tiger'
    ht[66] = 'monkey'
    print(ht.get(55), ht[35], ht[36])
    print(len(ht))
    del ht[35]
    del ht[36]

    if 'monkey' in ht:
        print('yes')
    else:
        print('no')
    pass
