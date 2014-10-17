__author__ = 'olexandr'

import time


SOURCE_TYPES = {
    1: 'SQL',
    2: 'NOSQL',
    3: 'FILES',
}


class Timer:    
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start