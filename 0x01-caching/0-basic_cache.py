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
        for the given key.

        Args:
            key: The key to be used for caching.
            item: The value to be cached.

        """
        if key is None or item is None:
            return
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
