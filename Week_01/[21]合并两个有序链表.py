# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
#  
# 
#  示例： 
# 
#  输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#  
#  Related Topics 链表 
#  👍 1179 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = []
        while l1:
            l3.append(l1.val)
            l1 = l1.next
        while l2:
            l3.append(l2.val)
            l2 = l2.next
        l3.sort()

        l4 = ListNode(0)
        curr = l4
        for i in l3:
            node = ListNode(i)
            curr.next = node
            curr = curr.next
        return l4.next


        
# leetcode submit region end(Prohibit modification and deletion)
