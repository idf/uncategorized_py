__author__ = 'Daniel'


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Traverser(object):
    def morris_inorder(self, root):
        cur = root
        while cur:
            if not cur.left:
                self.consume(cur)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right

                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    self.consume(cur)
                    cur = cur.right

    def morris_preorder(self, root):
        cur = root
        while cur:
            if not cur.left:
                self.consume(cur)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right

                if not pre.right:
                    pre.right = cur
                    self.consume(cur)
                    cur = cur.left
                else:
                    pre.right = None
                    cur = cur.right

    def consume(self, node):
        print node.val


if __name__ == "__main__":
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right = TreeNode(7)
    root.right.right = TreeNode(9)
    root.right.right.left = TreeNode(8)

    traverser = Traverser()
    print traverser.morris_inorder.__name__
    traverser.morris_inorder(root)
    print traverser.morris_preorder.__name__
    traverser.morris_preorder(root)






