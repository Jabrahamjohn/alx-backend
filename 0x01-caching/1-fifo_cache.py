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