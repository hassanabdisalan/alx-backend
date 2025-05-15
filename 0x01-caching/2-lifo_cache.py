#!/usr/bin/env python3
""" 2-lifo_cache module """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache implements a LIFO caching system """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.stack = []  # Keep track of insertion order

    def put(self, key, item):
        """ Add an item using LIFO policy """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the last inserted item
                last_key = self.stack.pop()
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")
            self.stack.append(key)
        else:
            # Update existing key position in stack
            self.stack.remove(key)
            self.stack.append(key)

        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve item by key """
        return self.cache_data.get(key, None)
