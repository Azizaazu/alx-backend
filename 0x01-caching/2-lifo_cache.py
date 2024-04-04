#!/usr/bin/env python3
"""This module defines LIFOCache class"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching
    and implements a caching system using LIFO algorithm.
    """

    def __init__(self):
        """
        Initializes the LIFOCache object.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Assigns item value to the dictionary self.cache_data
        for the given key.
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[-1]))
                del self.cache_data[self.order[-1]]
                del self.order[-1]
            if key in self.order:
                del self.order[self.order.index(key)]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value linked to the given key in self.cache_data.
        """
        if key is not None or key in self.cache_data.keys():
            return self.cache_data[key]
        return None
