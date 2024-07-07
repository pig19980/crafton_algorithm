class Node:
    def __init__(self, val):
        self.val = val
        self.cnt = 1
        self.pnode: Node = None
        self.snode: Node = None
        self.bnode: Node = None

    def scnt(self):
        if self.snode == None:
            return 0
        else:
            return self.snode.cnt

    def bcnt(self):
        if self.bnode == None:
            return 0
        else:
            return self.bnode.cnt

    def print_node(self):
        sv = None if self.snode == None else self.snode.val
        bv = None if self.bnode == None else self.bnode.val
        print(f"{self.val} {self.cnt} -> {sv} {bv} up {self.pnode.val}")
        if self.snode != None:
            self.snode.print_node()
        if self.bnode != None:
            self.bnode.print_node()


class BigSmallTree:
    def __init__(self):
        self.cursor: Node = None
        self.root = Node(None)

    def put(self, val):
        new_node = Node(val)
        if self.cursor == None:
            self.cursor = new_node
            self.cursor.pnode = self.root
            self.root.snode = self.cursor
            self.root.bnode = self.cursor
            return

        cnode = self.cursor

        while True:
            cnode.cnt += 1
            if val < cnode.val:
                next_node = cnode.snode
                if next_node == None:
                    cnode.snode = new_node
                    new_node.pnode = cnode
                    return
            else:
                next_node = cnode.bnode
                if next_node == None:
                    cnode.bnode = new_node
                    new_node.pnode = cnode
                    return
            cnode = next_node

    def right_rot(self, node: Node):
        if node.snode == None:
            print("r rot ERROR")
            exit()

        objnode = node.snode
        if node.pnode.snode == node:
            node.pnode.snode = objnode
        if node.pnode.bnode == node:
            node.pnode.bnode = objnode

        objnode.pnode = node.pnode

        node.snode = objnode.bnode
        objnode.bnode.pnode = node
        objnode.bnode = node
        node.pnode = objnode

        objnode.cnt += 1
        node.cnt -= 1

        return objnode

    def left_rot(self, node: Node):
        if node.bnode == None:
            print("r rot ERROR")
            exit()

        objnode = node.bnode
        if node.pnode.snode == node:
            node.pnode.snode = objnode
        if node.pnode.bnode == node:
            node.pnode.bnode = objnode

        objnode.pnode = node.pnode

        node.bnode = objnode.snode
        objnode.snode.pnode = node
        objnode.snode = node
        node.pnode = objnode

        objnode.cnt += 1
        node.cnt -= 1

        return objnode

    def get_mid(self):
        cur_node = self.cursor
        while (
            cur_node.scnt() != cur_node.bcnt()
            and cur_node.scnt() + 1 != cur_node.bcnt()
        ):
            print(cur_node.val, cur_node.scnt(), cur_node.bcnt())
            if cur_node.scnt() < cur_node.bcnt():
                cur_node = self.left_rot(cur_node)
            else:
                cur_node = self.right_rot(cur_node)

        return cur_node.val

    def print_tree(self):
        if self.cursor != None:
            self.cursor.print_node()


bst = BigSmallTree()
N = int(input())
for _ in range(N):
    got = int(input())
    print(got)
    bst.put(got)
    print("putted")
    bst.print_tree()
    bst.get_mid()
    bst.print_tree()
    print()
