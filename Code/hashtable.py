#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.size = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items(): #iterates over all keys and values in bucket 
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(n) Why and under what conditions? If you have to traverse every item in list"""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        values = 0
        for item in self.buckets:
            values += 1
        return values 
        

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(n) Why and under what conditions? Traversing through each item in th list""" 
        # Collect all pairs of key-value entries in each bucket
        all_value_pairs = []
        for bucket in self.buckets:
            all_value_pairs.extend(bucket.items())
        return all_value_pairs

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(n) Why and under what conditions? Because it takes each bucket times the length to traverse and acquire
        the total value of entries which is equal to O(n). Another way I chose to implment this is to use the self.size property which
        would then be O(1) constant time."""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        key_values = 0
        for bucket in self.buckets:
            for item in bucket.items(): #.items returns list of keys and values
                key_values += 1
        return key_values 
        #return self.size 



    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(l) Why and under what conditions? It is the number of key value entries divided by the number of buckets
        which is the average length of the linkedlist. Has to check through each bucket and its length to find key"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        bucket = self.buckets[self._bucket_index(key)]

        for item_key, item_value in bucket.items():
                if item_key == key:
                    return True
                else:
                    return False
                    
    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(1) best case and average case O(l) because the item could be the first one
        looked at or the item could be last which in this case would take (n/b) time which is O(l) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket = self.buckets[self._bucket_index(key)]
        for item_key, item_value in bucket:
            if item_key == key:
                return item_value
            
        raise KeyError('Key not found: {}'.format(key))


    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(1) best case if the item being updated is the first in the bucket. O(l) due to the average length of 
        the buckets based off of the number of value-entries over the number of buckets """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        bucket = self.buckets[self._bucket_index(key)]

        for item_key, item_value in bucket:
            if item_key == key:
                bucket.delete(item_key, item_value) # update
            else:
                bucket.append((key, value)) # insert 

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(1) because we could be deleting the first element in the linkedlist. O(l) average case because it depends 
        on the load factor or average length of the linkedlist in the buckets. Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket = self.buckets[self._bucket_index(key)]
        for item_key, item_value in bucket.items():
            if item_key == key:
                bucket.delete((item_key, item_value))

        raise KeyError('Delete Failed: {}'.format(key))



def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
