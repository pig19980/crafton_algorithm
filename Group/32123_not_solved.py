# 10:07
import sys


class node:
    def __init__(self, add, size):
        self.add = add
        self.size = size
        self.prev: node = None
        self.next: node = None


class linked_list:
    def __init__(self):
        self.head: node = None
        self.tail: node = None

    def push_back(self, node: node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.add, cur_node.size)
            cur_node = cur_node.next


input = sys.stdin.readline

N, K = map(int, input().split(" "))
adds = list(map(int, input().rstrip()))

ll = linked_list()
idx = 0
while idx < len(adds):
    node_add = adds[idx]
    size = 0
    while idx < len(adds) and adds[idx] == node_add:
        size += 1
        idx += 1
    new_node = node(node_add, size)
    ll.push_back(new_node)

ll.print_list()


ll = linked_list()
idx = 0
while idx < len(adds):
    node_add = adds[idx]
    size = 0
    while idx < len(adds) and adds[idx] == node_add:
        size += 1
        idx += 1
    new_node = node(node_add, size)
    ll.push_back(new_node)

ll.print_list()
