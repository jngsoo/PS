class Hash:
    def __init__(self, size=None):
        self.size = size * 2 + 1
        self.keys = [None] * self.size

    def __iter__(self):
        for i in range(self.size):
            yield self.keys[i]

    def find_slot(self, key):
        i = self.hash_function(key)
        start = i
        while (self.keys[i] != None):
            i = (i + 1) % (self.size)
            if i == start:
                return None
        return i

    def set(self, key, value=None):
        i = self.find_slot(key)
        if i == None:  # 다찬경우
            return None
        elif self.keys[i] == None:  # 값이 없어서 추가
            self.keys[i] = key
            return key

    def hash_function(self, key):
        return key % self.size


def solution(k, room_number):
    answer = []
    h = Hash(k)
    for i in room_number:
        answer.append(h.find_slot(i))
        h.set(i)
    return answer