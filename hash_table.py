class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Create empty chains

    def _hash(self, key):
        return key % self.size  # Simple hash function

    def insert(self, key, value):
        index = self._hash(key)
        self.table[index].append((key, value))  # Insert (key, value) pair into the chain

    def search(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v  # Return value if key is found
        return None  # Key not found

    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]  # Delete the (key, value) pair
                return
        raise KeyError("Key not found")

# Example usage
ht = HashTable(10)
ht.insert(5, "Apple")
ht.insert(15, "Banana")  # Collision handled by chaining
print("Search 15:", ht.search(15))  # Output: Banana
ht.delete(15)
print("Search 15 after deletion:", ht.search(15))  # Output: None