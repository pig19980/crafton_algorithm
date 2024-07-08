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
        print(f"{self.val} {self.cnt} -> {sv} {bv}   up val {self.pnode.val}")
        if self.snode != None:
            self.snode.print_node()
        if self.bnode != None:
            self.bnode.print_node()


class BSTree:
    def __init__(self):
        self.cursor: Node = None
        self.head = Node(0)

    def right_cycle(self, Mnode: Node):
        Snode = Mnode.snode
        bnode = Snode.bnode

        if Mnode.pnode.snode == Mnode:
            Mnode.pnode.snode = Snode
        if Mnode.pnode.bnode == Mnode:
            Mnode.pnode.bnode = Snode

        Mnode.pnode, Snode.pnode = Snode, Mnode.pnode
        if bnode != None:
            bnode.pnode = Mnode

        Snode.bnode = Mnode
        Mnode.snode = bnode

        Mnode.cnt = Mnode.scnt() + Mnode.bcnt() + 1
        Snode.cnt = Snode.scnt() + Snode.bcnt() + 1

    def left_cycle(self, Mnode: Node):
        Bnode = Mnode.bnode
        snode = Bnode.snode

        if Mnode.pnode.snode == Mnode:
            Mnode.pnode.snode = Bnode
        if Mnode.pnode.bnode == Mnode:
            Mnode.pnode.bnode = Bnode

        Mnode.pnode, Bnode.pnode = Bnode, Mnode.pnode
        if snode != None:
            snode.pnode = Mnode
        Bnode.snode = Mnode
        Mnode.bnode = snode

        Mnode.cnt = Mnode.scnt() + Mnode.bcnt() + 1
        Bnode.cnt = Bnode.scnt() + Bnode.bcnt() + 1

    def put(self, val):
        new_node = Node(val)
        if self.cursor == None:
            self.cursor = new_node
            self.cursor.pnode = self.head
            self.head.snode = self.cursor
            self.head.bnode = self.cursor
            return

        next = self.cursor
        while True:
            if next.val < val:
                if next.bnode == None:
                    next.bnode = new_node
                    break
                next = next.bnode
            else:
                if next.snode == None:
                    next.snode = new_node
                    break
                next = next.snode
        new_node.pnode = next

        while next != self.head:
            next.cnt += 1
            next = next.pnode

        print("before cycle")
        self.print_tree()

        cur_node = new_node
        while cur_node != self.cursor:
            pnode = cur_node.pnode
            if pnode.cnt != (pnode.scnt() + pnode.bcnt() + 1):
                print("ERROR")
                print(
                    f"{pnode.val} {pnode.cnt} != ({pnode.scnt()} + {pnode.bcnt()} + 1) "
                )
                exit()
            if (pnode.cnt - 1) // 2 != pnode.scnt():
                if pnode.scnt() == pnode.bcnt() + 1:
                    print(cur_node.val, "right cycle")
                    self.right_cycle(pnode)
                    self.print_tree()
                elif pnode.scnt() + 2 == pnode.bcnt():
                    print(cur_node.val, "left cycle")
                    self.left_cycle(pnode)
                    self.print_tree()
                else:
                    print("ERROR")
                    print(pnode.scnt(), pnode.bcnt())
                    exit()
            cur_node = cur_node.pnode

    def get_mid(self):
        return self.cursor.val

    def print_tree(self):
        if self.cursor != None:
            self.cursor.print_node()


bst = BSTree()
N = int(input())
for _ in range(N):
    got = int(input())
    print(got)
    bst.put(got)
    print(bst.get_mid())
    bst.print_tree()
