#!/usr/bin/env python3
"""This module defines BasicCache class, a caching system."""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching
    and implements a caching system without limit.
    """

    def put(self, key, item):
        """
        Assigns item value to the dictionary self.cache_data
        for the given key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value linked to the given key in self.cache_data.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
