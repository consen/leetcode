# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        if not root:
            return []
        view = []
        last_node = root
        # None is separator of levels
        queue = [root, None]
        while queue:
            cur_node = queue.pop(0)
            if cur_node == None:
                view.append(last_node.val)
                if queue: queue.append(None)
            else:
                last_node = cur_node
                if cur_node.left: queue.append(cur_node.left)
                if cur_node.right: queue.append(cur_node.right)
        return view


def main():
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    root.left.right = TreeNode(5)
    print s.rightSideView(root)


if __name__ == '__main__':
    main()
