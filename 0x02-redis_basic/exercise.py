#!/usr/bin/env python3
"""function that creates a Redis instance"""
import uuid
import redis
from typing import Union, Callable


def counts_calls(method: Callable) -> Callable:
    """function that counts number of calls"""
    def wrapper(*args, **kwargs):
        """this a function decorator"""
        key = f"method:{method.__equalname__}"
        self.-redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callabel:
    """function that increaments number of calls"""
    def wrapper(*args, **kwargs):
        """retuns the number of call increamented"""
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(inputs_key, str(args))
        result = method(self, args, kwargs)
        self._redis.rpush(outputs_key, str(result))
        return result
    return wrapper


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
