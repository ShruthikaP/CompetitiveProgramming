class Trie(object):
    def __init__(self):
        self.root = {}
    def check(self, word):
        current = self.root
        flag = False     
        for char in word:
            if char not in current:
                flag = True
                current[char] = {}
            current = current[char]
        if "End Of Word" not in current:
            flag = True
            current["End Of Word"] = {}
        return flag