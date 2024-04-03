#!/usr/bin/env python3

'''Task 0: Basic Dictionary
'''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''A class 'basciCache' that inherits from 'BasicCaching'
    and is a chaching system
    '''

    def put(self, key, item):
        '''assign to the dictionary 'self.cache' that inherits from 'BaseCaching' and is a caching system
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''return the value in 'self.cache_data' linked to 'key'
        '''

        return self.cache_data.get(key, None)
