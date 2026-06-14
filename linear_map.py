class ProbingHashMap:
    def __init__(self, capacity=19): # Prefers prime number bounding sizes
        self.capacity = capacity
        self.keys = [None] * capacity
        self.frequencies = [0] * capacity

    def _hash_transform(self, key):
        return abs(hash(key)) % self.capacity

    def log_observation(self, key):
        start_idx = self._hash_transform(key)
        i = 0
        
        while i < self.capacity:
            probe_idx = (start_idx + i) % self.capacity
            
            if self.keys[probe_idx] is None:
                self.keys[probe_idx] = key
                self.frequencies[probe_idx] = 1
                return
            if self.keys[probe_idx] == key:
                self.frequencies[probe_idx] += 1
                return
            i += 1 # Advance by linear tracking step increments

    def get_count(self, key):
        start_idx = self._hash_transform(key)
        i = 0
        while i < self.capacity:
            probe_idx = (start_idx + i) % self.capacity
            if self.keys[probe_idx] is None:
                return 0
            if self.keys[probe_idx] == key:
                return self.frequencies[probe_idx]
            i += 1
        return 0
