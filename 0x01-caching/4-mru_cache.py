#!/usr/bin/env python3
"""This module defines MRUCache class"""


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching
    and implements a caching system using MRU algorithm.
    """

    def __init__(self):
        """
        Initializes the MRUCache object.
        """
        super().__init__()
        self.recently_used = []

    def put(self, key, item):
        """
        Assigns item value to the dictionary self.cache_data
        for the given key.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.recently_used.pop()
            print("DISCARD:", mru_key)
            del self.cache_data[mru_key]

        self.cache_data[key] = item
        self.recently_used.append(key)

    def get(self, key):
        """
        Returns the value linked to the given key in self.cache_data.
        """
        if key is None or key not in self.cache_data:
            return None

        self.recently_used.remove(key)
        self.recently_used.append(key)

        return self.cache_data[key]
