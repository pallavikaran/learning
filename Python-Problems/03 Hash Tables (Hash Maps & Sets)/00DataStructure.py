"""
A hash table (or hash map) is a data structure that stores key-value pairs and provides very efficient insertion, deletion, and lookup — typically in constant time, O(1).
Python dict is built on hash table.
This uses Linked Lists

Hash table has 3 components:
    Key: A key is the unique identifier you use to store and retrieve data.
    Value: A value is the data associated with the key.
    Index: The index is where a key-value pair is stored in the internal array. Calculated by applying a hash function to the key - index = hash(key) % capacity
           If the index already exists then we update if key exists or add a node(head) at the start of the current hashed index which points to other indexed nodes
"""


# Define a Node
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # Instantiating a node which points to nothing


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity  # The total number of buckets (slots) the hash table can hold. It’s the size of the internal array
        self.size = 0  # The current number of key-value pairs stored in the table. Need to increment & decrement when key-value pairs are added or removed respectively.
        self.table = [[] for _ in range(capacity)]  # list of lists for chaining. This is the hash table's array, used to store data.  Creates a list with capacity number of None(Means the bucket is currently empty (no key-value pair stored yet) elements.

    def hash_function(self, key):  # Convert a key into an index (bucket number).
        return hash(key) % self.capacity  # This method gives you the index in the internal array (self.table) where the key-value pair should be placed.
        # hash(key): This is Python's built-in hash function. It converts the key (which can be a string, number, etc.) into a large integer (can be negative).
        # % self.capacity: This ensures the result fits within the bounds of the hash table. It maps the big hash value to an index between 0 and capacity - 1

    def insert(self, key, value):
        # Find the index for inserting
        index = self.hash_function(key)

        # Check if a node/(key-val) pair already exists in the hash table
        for pair in self.table[index]:  # self.table[index] -> [[0,1], [0,1], [0,1]]
            if pair[0] == key:  # If incoming key exists at this index then update the value
                pair[1] = value  # Update value if key already exists
                return

        self.table[index].append([key, value])
        self.size += 1

    def get(self, key):
        # Find the index for search
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]

        return None

    def delete(self, key):
        # Find the index for search
        index = self.hash_function(key)

        for i, pair in enumerate(self.table[index]):  # Use enumerate() to keep track of both the index (i) and the pair [a tuple like ["apple", 5]]
            if pair[0] == key:
                del self.table[index][i]
                self.size -= 1
                return True

        return False  # key not found


ht = HashTable(10)  # capacity 10
ht.insert("apple", 5)
ht.insert("banana", 3)
print(ht.get("apple"))    # Output: 5
ht.delete("apple")
print(ht.get("apple"))
