#!/usr/bin/env python3

"""This module defines LIFOCache class, a caching system using LIFO algorithm."""

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

    def put(self, key, item):
        """
        Assigns item value to the dictionary self.cache_data
        for the given key.

        Args:
            key: The key to be used for caching.
            item: The value to be cached.

        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Find the last item inserted (LIFO)
            last_key = next(reversed(self.cache_data))
            print("DISCARD:", last_key)
            del self.cache_data[last_key]

        self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value linked to the given key in self.cache_data.

        Args:
            key: The key whose value needs to be retrieved.

        Returns:
            The value associated with the key in self.cache_data,
            or None if the key is None or not found in the cache.

        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
