# create a node class to store the data

class Node:

    def __init__(self,key,val) -> None:
        self.key = key
        self.val = val
        self.next = None



# create a hash table class
class HashTable:

    def __init__(self,m: int) -> None:
        self.table = [None for i in range(m)]

    # computes the hash function
    def hash_function(self,key):
        lower_key = key.lower()
        hash_val = 0
        for i in range(len(lower_key)):
            hash_val += ord(lower_key[i])
        return hash_val

    # get the index using the hash value
    def get_index(self,key):
        return self.hash_function(key) % len(self.table)

    # inserts into the hash map
    def insert(self,key,val):
        index = self.get_index(key)
        head = self.table[index]
        new_node = Node(key,val)
        if head is not None:
            new_node.next = head
        self.table[index] = new_node

    # gets a value from the hash map
    def search(self,key):
        index = self.get_index(key)
        head = self.table[index]
        if head is None:
            return head
        else:
            current_node = head
            value = None
            while current_node is not None:
                if key == current_node.key:
                    value = current_node.val
                    break
                current_node = current_node.next
            return value
                
    # deletes a value from the hash map
    def delete(self,key):
        index = self.get_index(key)
        if index is not None:
            perivous_node = self.table[index]
            current_node = perivous_node.next
            if perivous_node.key == key:
                self.table[index] = current_node
            while current_node is not None:
                if current_node.key == key:
                    perivous_node.next = current_node.next
                    print(f"Delete entry with key: {key}")
                    break
                current_node = current_node.next
                perivous_node = perivous_node.next
            


if __name__ == "__main__":
    hash_table = HashTable(5)
    print("inserting values")
    hash_table.insert('Amir',25)
    hash_table.insert('Drogba',50)
    hash_table.insert('Adam',20)
    hash_table.insert('Ajuz',50)
    hash_table.insert('Tahir',27)
    hash_table.insert('Habib',79)
    hash_table.insert('Salim',16)
    hash_table.insert('Alamin',30)
    hash_table.insert('Kura',40)
    hash_table.insert('Mbahi', 34)
    print("Searching values")
    print(hash_table.search('Tahir'))
    print(hash_table.search('Kura'))
    print(hash_table.search('Mbahi'))
    print("Deleting values")
    hash_table.delete('Mbahi')
    print(hash_table.search('Mbahi'))