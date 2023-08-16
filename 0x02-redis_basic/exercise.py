#!/usr/bin/env python3
"""function that creates a Redis instance"""
import uuid
import redis
from typing import Union


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
