from .level1 import Level1
from .level2 import Level2

class LevelManager:
    def __init__(self):
        self._levels = [Level1, Level2]
        self.idx = 0
        self.level = self._levels[self.idx]()  # instancia actual

    def reload_current(self):
        self.level = self._levels[self.idx]()

    def next_level(self):
        self.idx += 1
        if self.idx >= len(self._levels):
            return False  # no hay más niveles → victoria
        self.level = self._levels[self.idx]()
        return True
