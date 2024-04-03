#!/usr/bin/env python3

"""This module defines MRUCache class, a caching system using MRU algorithm."""

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

        Args:
            key: The key to be used for caching.
            item: The value to be cached.

        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove most recently used item
            mru_key = self.recently_used.pop()
            print("DISCARD:", mru_key)
            del self.cache_data[mru_key]

        self.cache_data[key] = item
        # Move the key to the end to mark it as most recently used
        self.recently_used.append(key)

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

        # Move the key to the end to mark it as most recently used
        self.recently_used.remove(key)
        self.recently_used.append(key)

        return self.cache_data[key]
