# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        ans = ListNode(0)
        node = ans
        a = l1
        b = l2
        while a or b:
            v = 0
            if a:
                v += a.val
                a = a.next
            if b:
                v += b.val
                b = b.next
            v += node.val
            node.val = v % 10
            if v / 10 > 0 or a or b:
                node.next = ListNode(v / 10)
                node = node.next
        return ans

def main():
    s = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    l = s.addTwoNumbers(l1, l2)
    while l:
        print l.val
        l = l.next

if __name__ == '__main__':
    main()


