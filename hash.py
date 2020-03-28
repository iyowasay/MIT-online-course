class HashMap:
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size

    def _get_hash_index(self, key):
        hashy = 0
        for char in str(key):
            hashy += ord(char)
        return hashy % self.size

    def add(self, key, value):
        key_hash = self._get_hash_index(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            # check whether the key is already in the hash in order to update the value
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            # things after return being executed won't be executed
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash_index(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash_index(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return None

    def print(self):
        print('---PHONEBOOK---')
        for item in self.map:
            if item is not None:
                print(str(item))


h = HashMap()
h.add('Joe', '0978361629')
h.add('Bob', '0935777308')
h.add('Gina', '0915921015')
h.add("Home", "04-23190490")
h.add('Trump', 'What an incredible president of United States')
h.print()
h.delete('Bob')
h.print()
# print(h.get('Joe'))
h.add('Joe', 'tue')
h.add('Trump', 'USA vs China')
print(h.map)


# solve collision via linked list(chaining)
class Node:
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d


class LinkedList:
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, d):
        self.size += 1
        new_node = Node(d, self.root)
        self.root = new_node

    def remove(self, d):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.get_data() == d:
                if prev_node is not None:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.get_data() == d:
                return d
            elif this_node.get_next() is None:
                return 'No this value'
            else:
                this_node = this_node.get_next()


def main():
    lu = LinkedList()
    lu.add(5)
    lu.add(12)
    lu.add(1)
    lu.add(3)
    lu.add(10)
    lu.add(2)
    lu.add(7)
    lu.add(0)
    print('Size of this list: ' + str(lu.get_size()))
    lu.remove(12)
    print('Size of this list: ' + str(lu.get_size()))
    print(lu.find(101))


main()











