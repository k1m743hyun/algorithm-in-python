# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_val = []
        while True:
            l1_val.append(l1.val)
            if l1.next == None:
                break
            l1 = l1.next
        num1 = int(''.join(map(str, l1_val[::-1])))

        l2_val = []
        while True:
            l2_val.append(l2.val)
            if l2.next == None:
                break
            l2 = l2.next
        num2 = int(''.join(map(str, l2_val[::-1])))

        for idx, val in enumerate(map(int, list(str(num1 + num2)))):
            if idx == 0:
                ln = ListNode(val=val)
            else:
                ln = ListNode(val, ln)

        return ln
