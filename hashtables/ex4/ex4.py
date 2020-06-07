# def has_negatives(a):
#     capacity = len(a)
#     ht = HashTable(capacity)
#     result = []

#     for each in a:
#         if each > 0:
#             if ht.get(each) is None:
#                 ht.put((each * -1), each)
        
            
#     for each in a:
#         if each < 0:
#             result.append(ht.get(each))

#     return result
# if __name__ == "__main__":
#     print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

### IT WORKS, BUT REALLY SLOWLY ###

def has_negatives(a):
    seen = {}
    result = []

    for each in a:
        seen[each] = None

        if each != 0 and -each in seen:
            result.append(abs(each))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))



class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f'HashTableEntry({repr(self.key)}, {repr(self.value)})'


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self,node):
        node.next = self.head
        self.head = node
        return self.head.value

    def find(self, key):
        current = self.head
        # look until the end
        while current is not None:
            # is the current value the one we want? If yes, return the current node
            if current.key == key:
                return current
            current = current.next
        
        return None

    def delete(self, key):
        current = self.head

        # special case of deleting the head of the list
        if current.key == key:
            self.head = self.head.next
            return current
        
        # general case
        previous = current
        current = current.next

        while current is not None:
            if current.key == key:
                previous.next = current.next # cuts old node out of sll
                return current
            else:
                previous = previous.next
                current = current.next

        return None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        self.capacity = capacity
        self.contents = [LinkedList()] * self.capacity

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        
        return key


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # first find slot
        slot = self.hash_index(key)

        # search the LinkedList
        current = self.contents[slot].find(key)
        if current is not None:
            # if found, overwrite
            current.value = value
            return current.value
        else: 
            # if not found, insert
            return self.contents[slot].insert_at_head(HashTableEntry(key, value))


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        if not key:
            return None
        else: 
            slot = self.hash_index(key)
            
        if self.contents[slot] is not None:
            desired = self.contents[slot].find(key)

            if desired is not None:
                return desired.value

        return None

print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))