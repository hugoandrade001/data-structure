from typing import List
from eg_deque import Deque


class BSTNode:
    def __init__(self, x, left=None, right=None):
        self.val, self.left, self.right = x, left, right


def level_order(root: BSTNode) -> List[int]:
    traversal = []
    queue = Deque()
    queue.enqueue(root)
    while queue.size > 0:
        node = queue.dequeue()
        traversal.append(node.val)
        if node.left is not None:
            queue.enqueue(node.left)
        if node.right is not None:
            queue.enqueue(node.right)
    return traversal


def pre_order(root: BSTNode) -> List[int]:
    traversal = []
    stack = Deque()
    stack.push(root)
    while stack.size > 0:
        node = stack.pop()
        traversal.append(node.val)
        if node.right is not None:
            stack.push(node.right)
        if node.left is not None:
            stack.push(node.left)
    return traversal


def in_order(root: BSTNode) -> List[int]:
    traversal = []
    stack = Deque()
    cur = root
    while cur is not None or stack.size > 0:
        if cur is not None:
            stack.push(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            traversal.append(cur.val)
            cur = cur.right
    return traversal


def post_order(root: BSTNode) -> List[int]:
    s1, s2 = Deque(), Deque()
    s1.push(root)
    while s1.size > 0:
        node = s1.pop()
        s2.push(node)
        if node.left is not None:
            s1.push(node.left)
        if node.right is not None:
            s1.push(node.right)

    traversal = []
    while s2.size > 0:
        traversal.append(s2.pop().val)
    return traversal


def zig_zag(root: BSTNode) -> List[int]:
    pass


""" ========== Testing BST ========== """


def test_bst():
    n4 = BSTNode(4)
    n12 = BSTNode(12)
    n18 = BSTNode(18)
    n24 = BSTNode(24)
    n31 = BSTNode(31)
    n44 = BSTNode(44)
    n66 = BSTNode(66)
    n90 = BSTNode(90)

    n10 = BSTNode(10, n4, n12)
    n22 = BSTNode(22, n18, n24)
    n35 = BSTNode(35, n31, n44)
    n70 = BSTNode(70, n66, n90)

    n15 = BSTNode(15, n10, n22)
    n50 = BSTNode(50, n35, n70)

    r = BSTNode(25, n15, n50)

    # print(level_order(r))
    # print(pre_order(r))
    # print(in_order(r))
    print(post_order(r))


test_bst()
#   U p d a t e d   B S T   i m p l e m e n t a t i o n  
 #   B i n a r y   S e a r c h   T r e e :   O r g a n i z e s   e l e m e n t s   h i e r a r c h i c a l l y   w i t h   e f f i c i e n t   s e a r c h i n g ,   i n s e r t i o n ,   a n d   t r a v e r s a l   c a p a b i l i t i e s .   U s e d   i n   m a p s ,   s e t s ,   a n d   r a n g e   q u e r i e s .  
 