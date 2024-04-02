#!/usr/bin/env python3
"""FIFO caching"""

from base_caching import BaseCaching

def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.queue = []
        self.cache_data = {}

def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard = self.queue.pop(0)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
            self.queue.append(key)
            self.cache_data[key] = item