#!/usr/bin/env python3
""" 3-lru_cache module """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines a caching system with LRU eviction """

    def __init__(self):
        """ Initialize the LRU cache """
        super().__init__()
        self.usage_order = []  # Tracks the usage order of keys

    def put(self, key, item):
        """ Add an item using LRU policy """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update value and usage order
            self.cache_data[key] = item
            self.usage_order.remove(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Evict least recently used key
                lru_key = self.usage_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")
            self.cache_data[key] = item

        # Append as most recently used
        self.usage_order.append(key)

    def get(self, key):
        """ Retrieve item by key, updating usage order """
        if key is None or key not in self.cache_data:
            return None

        # Move key to end (most recently used)
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
