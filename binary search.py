import time
data = [1, 2, 4, 5, 6, 8, 10, 11, 12, 13, 16, 17, 19, 22, 23, 27, 35, 44, 46, 47, 50, 54, 60, 69, 73, 99, 100, 101, 107, 111]
target = 5
data1 = [5, 10, 7, 19, 3, 1, 24, 0, 6, 11, 2, 100, 31, 44, 77, 69]


# binary tree
class node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


class bst:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    # separate the recursive function in order to make the main insert function neat
    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child is None:
                cur_node.left_child = node(value)
                cur_node.left_child.parent = cur_node
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child is None:
                cur_node.right_child = node(value)
                cur_node.right_child.parent = cur_node
            else:
                self._insert(value, cur_node.right_child)
        else:
            print('Value is in the tree!')

    # measure the height of the tree
    def height(self):
        if self.root is None:
            return 0
        else:
            return self._height(self.root, 0)

    def _height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        left_height = self._height(cur_node.left_child, cur_height + 1)
        right_height = self._height(cur_node.right_child, cur_height + 1)
        return max(left_height, right_height)

    # real searching
    def search(self, value):
        if self.root is not None:
            return self._search(self.root, value)
        else:
            return None  # could be "return False"

    def _search(self, cur_node, value):
        if cur_node.value == value:
            return cur_node  # could return True or False
        elif value < cur_node.value and cur_node.left_child is not None:
            return self._search(cur_node.left_child, value)
        elif value > cur_node.value and cur_node.right_child is not None:
            return self._search(cur_node.right_child, value)
        else:
            return False

    def delete_value(self, value):
        return self.delete_node(self.search(value))

    def delete_node(self, node):

        # returns the node with minimum value in tree rooted at input node
        def min_value_node(n):
            current = n
            while current.left_child is not None:
                current = current.left_child
            return current

        #  returns the number of children for the specified node
        def num_children(n):
            num_children = 0
            if n.left_child is not None:
                num_children += 1
            if n.right_child is not None:
                num_children += 1
            return num_children

        # get the parent of the node to be deleted
        node_parent = node.parent
        # get the number of children of the node to be deleted
        node_children = num_children(node)

        # case1 the target(node) has no children
        if node_children == 0:
            # remove reference to the node from the parent
            if node_parent.left_child == node:
                node_parent.left_child = None
            else:
                node_parent.right_child = None

        # case2 the target has one child
        if node_children == 1:
            # get the single child node
            if node.left_child is not None:
                child = node.left_child
            else:
                child = node.right_child

            # replace the node to be deleted with its child
            if node_parent.left_child == node:
                node_parent.left_child = child
            else:
                node_parent.right_child = child

            # correct the parent pointer in node
            child.parent = node_parent

        # case3 the target has two children
        if node_children == 2:
            # get the in-order traversal successor of the deleted node
            successor = min_value_node(node.right_child)
            # copy the successor's value to the node formerly holding the value we wished to delete
            node.value = successor.value

            # delete the in-order successor now that it's value was copied into the other node
            self.delete_node(successor)

    # print out the nodes
    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child)


from random import sample
num_elements = 10
max_int = 50
# implement sample function to avoid same values in a tree
unsorted_array = sample(list(range(max_int)), num_elements)


def fill_tree(treee):
    for _ in range(num_elements):
        treee.insert(unsorted_array[_])
    return treee


tree = fill_tree(bst())
tree.print_tree()
tree.insert(10)
tree.insert(5)
tree.print_tree()
tree.delete_value(10)
tree.print_tree()
# print(tree.height())
# print(tree.search(20))
# print(tree.search(30))
# print(tree.search(5))


# basic searching
# def linear_search(li, number):
#     for i in li:
#         if i == number:
#             return True
#     return False
#
#
# def binary_search_iterative(li, number):
#     low = 0
#     high = len(li) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if number == li[mid]:
#             return True
#         elif number > li[mid]:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return False
#
#
# def binary_search_recursive(li, number, low, high):
#     if low > high:
#         return False
#     else:
#         mid = (low + high) // 2
#         if number == li[mid]:
#             return True
#         elif number > li[mid]:
#             return binary_search_recursive(li, number, mid + 1, high)
#         else:
#             return binary_search_recursive(li, number, low, mid - 1)
#
#
# t1 = time.perf_counter()
# print(linear_search(data, target))
# t2 = time.perf_counter()
# print(binary_search_recursive(data, target, 0, 29))
# t3 = time.perf_counter()
# print(binary_search_iterative(data, target))
# t4 = time.perf_counter()
# print('It took {} seconds'.format(t2-t1))
# print('It took {} seconds'.format(t3-t2))
# print('It took {} seconds'.format(t4-t3))







