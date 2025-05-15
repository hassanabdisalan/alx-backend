#!/usr/bin/env python3
""" 4-mru_cache module """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines a caching system using MRU eviction policy """

    def __init__(self):
        """ Initialize the MRUCache """
        super().__init__()
        self.usage_order = []  # Tracks usage order; most recently used is last

    def put(self, key, item):
        """ Add item to cache using MRU policy """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update existing key's value and usage
            self.cache_data[key] = item
            self.usage_order.remove(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the most recently used key (last in usage_order)
                mru_key = self.usage_order.pop()
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")
            self.cache_data[key] = item

        # Mark this key as most recently used
        self.usage_order.append(key)

    def get(self, key):
        """ Get item from cache and update its usage """
        if key is None or key not in self.cache_data:
            return None

        # Move accessed key to the end (most recently used)
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
