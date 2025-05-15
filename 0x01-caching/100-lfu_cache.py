#!/usr/bin/env python3
""" 100-lfu_cache module """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines a caching system using LFU + LRU eviction policy """

    def __init__(self):
        """ Initialize the LFUCache """
        super().__init__()
        self.freq = {}         # key -> usage frequency
        self.usage_order = []  # keeps insertion/access order (for LRU tie-breaking)

    def put(self, key, item):
        """ Add item to cache using LFU + LRU policy """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update existing key
            self.cache_data[key] = item
            self.freq[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find least frequently used key(s)
                min_freq = min(self.freq.values())
                lfu_keys = [k for k in self.freq if self.freq[k] == min_freq]

                # If multiple LFUs, use LRU tie-breaker
                if len(lfu_keys) > 1:
                    for k in self.usage_order:
                        if k in lfu_keys:
                            discard_key = k
                            break
                else:
                    discard_key = lfu_keys[0]

                # Discard the key
                del self.cache_data[discard_key]
                del self.freq[discard_key]
                self.usage_order.remove(discard_key)
                print(f"DISCARD: {discard_key}")

            # Add new key
            self.cache_data[key] = item
            self.freq[key] = 1
            self.usage_order.append(key)

    def get(self, key):
        """ Retrieve item from cache and update usage frequency and order """
        if key is None or key not in self.cache_data:
            return None

        self.freq[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
