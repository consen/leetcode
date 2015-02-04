# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.root = root
        self.smallest = None
        

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if not self.root:
            return False
        
        if not self.root.left:
            self.smallest = self.root.val
            self.root = self.root.right
            return True
            
        node = self.root
        node_parent = None 
        while node.left:
            node_parent = node
            node = node.left
            self.smallest = node.val
        if node.right:
            node_parent.left = node.right
        else:
            node_parent.left = None
        return True

    # @return an integer, the next smallest number
    def next(self):
        return self.smallest
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

def main():
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    i = BSTIterator(root)
    while i.hasNext():
        print i.next()

if __name__ == '__main__':
    main()
