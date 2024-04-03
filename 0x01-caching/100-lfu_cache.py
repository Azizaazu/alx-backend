#!/usr/bin/env python3

"""This module defines LFUCache class, a caching system using LFU algorithm."""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching
    and implements a caching system using LFU algorithm.
    """

    def __init__(self):
        """
        Initializes the LFUCache object.
        """
        super().__init__()
        self.frequency = {}

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
            min_frequency = min(self.frequency.values())
            least_frequent_keys = [k for k, v in self.frequency.items() if v == min_frequency]

            if len(least_frequent_keys) > 1:
                # Use LRU algorithm to break tie
                lru_key = min(self.cache_data, key=lambda k: self.cache_data[k]['last_used'])
                print("DISCARD:", lru_key)
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
            else:
                lfu_key = least_frequent_keys[0]
                print("DISCARD:", lfu_key)
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]

        self.cache_data[key] = {'value': item, 'frequency': 1, 'last_used': 0}
        self.frequency[key] = 1

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

        self.cache_data[key]['frequency'] += 1
        self.cache_data[key]['last_used'] += 1
        return self.cache_data[key]['value']
