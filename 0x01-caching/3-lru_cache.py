#!/usr/bin/env python3
"""This module defines LRUCache class."""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching
    and implements a caching system using LRU algorithm.
    """

    def __init__(self):
        """
        Initializes the LRUCache object.
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
            lru_key = self.recently_used.pop(0)
            print("DISCARD:", lru_key)
            del self.cache_data[lru_key]

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
