import time 

class Cache:
    # timeout the time the cache will be valid in millis
    def __init__(self, timeout, callback) -> None:
        self.cb = callback
        self.value = None
        self.timeout = timeout
        self.timeout_cache = timeout + time.time() * 1000 
    def get_value(self):
        if time.time() * 1000 >= self.timeout_cache or self.value == None:
            # get a new value 
            self.timeout_cache = self.timeout + time.time() * 1000 
            self.value = self.cb()
        return self.value
    def reset_cache(self):
        self.timeout_cache = 0
        return self.value 
