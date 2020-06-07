#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.key = source # treat as key
        self.value = destination # value

def reconstruct_trip(tickets, length):
    route = []

    ht = HashTable(length)

    # hash the tickets
    for each in tickets:
        ht.put(each.key, each.value)

    # start where source is NONE
    current = ht.get("NONE")
    print('Starting',current)

    # assign that destination as the first in the route
    route.append(current)

    while current != "NONE":
        for _ in range(1,length):
            current = ht.get(current)
            route.append(current)
            print('each', route)

    return route

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

MIN_CAPACITY = 8
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
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash


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
            return self.contents[slot].insert_at_head(Ticket(key, value))

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
