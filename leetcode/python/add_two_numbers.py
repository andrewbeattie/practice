"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

https://www.youtube.com/watch?v=wgFPrzTjm7s

1. Add two numbers returning carry over, and remainder
  x + y = z
  if z > 10:
      carry = 1
      z % 10
  return carry, z

2. loop through the list node
    while l1.next or l2.next

3. store in a list node
    l3 = ListNode(0) # create empty list node
    holder = l3      # create a variable to hold values while we loop through


"""
from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:

    def _single_sum(self, n1, n2, carry):
        total_digits = n1 + n2 + carry
        digit = total_digits % 10
        carry = total_digits // 10
        return digit, carry

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l3 = ListNode(0)
        tail = l3
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:

            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0
            digit, carry = self._single_sum(digit1, digit2, carry)

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = l3.next
        l3.next = None
        return result
        
