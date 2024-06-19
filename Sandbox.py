class MyHashTable:
    def __init__(self, size=100):
        self.size = size  # Initial size of the hash table
        self.buckets = [[] for _ in range(size)]  # List of empty lists (buckets)

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)  # Update value if key exists
                return
        self.buckets[index].append((key, value))  # Add new key-value pair if key doesn't exist

    def get(self, key):
        index = self._hash(key)
        for k, v in self.buckets[index]:
            if k == key:
                return v  # Return value if key is found
        raise KeyError(f'Key {key} not found')  # Raise KeyError if key is not found

    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                del self.buckets[index][i]  # Delete key-value pair if key is found
                return
        raise KeyError(f'Key {key} not found')  # Raise KeyError if key is not found

# Create an instance of MyHashTable
ht = MyHashTable()

# Insert key-value pairs
ht.insert('a', 1)
ht.insert('b', 2)
ht.insert('c', 3)

# Retrieve values
print(ht.get('a'))  # Output: 1
print(ht.get('b'))  # Output: 2

# Delete a key-value pair
ht.delete('b')
print(ht.get('b'))  # Raises KeyError: 'Key b not found'
