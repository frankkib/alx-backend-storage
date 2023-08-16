#!/usr/bin/env python3
"""function that creates a Redis instance"""
import uuid
import redis
from typing import Union, Callable


class Cache:
    """class initialization"""
    def __init__(self):
        """class initializer"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """returns a string key id"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key, fn: Callable = None):
        """used to convert the data back to the desired format"""
        value = self._redis.get(key)
        if value is not None and fn is not None:
            value = fn(value)
        return value

    def get_str(self, key):
        """return cache.get"""
        return self.get(key, lambda X: X.decode('utf-8'))

    def get_int(self, key):
        """returns the key"""
        return self.get(key, int)
