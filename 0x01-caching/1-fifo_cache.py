#!/usr/bin/env python3
""" 1-fifo_cache module """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache implements a FIFO caching system """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.queue = []  # Maintain insertion order

    def put(self, key, item):
        """ Add an item using FIFO policy """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the oldest entry
                old_key = self.queue.pop(0)
                del self.cache_data[old_key]
                print(f"DISCARD: {old_key}")

            self.queue.append(key)

        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve item by key """
        return self.cache_data.get(key, None)
