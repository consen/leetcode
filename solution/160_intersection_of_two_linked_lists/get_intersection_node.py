# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
    	a_len = 0
    	b_len = 0
    	node = headA
    	while node:
    		a_len += 1
    		node = node.next
    	node = headB
    	while node:
    		b_len += 1
    		node = node.next

    	diff = abs(a_len - b_len)
    	a_node = headA
    	b_node = headB
    	if a_len < b_len:
    		for i in range(0, diff):
    			b_node = b_node.next
    	elif b_len < a_len:
    		for i in range(0, diff):
    			a_node = a_node.next

    	while a_node:
    		if a_node == b_node:
    			return a_node
    		a_node = a_node.next
    		b_node = b_node.next

    	return None

