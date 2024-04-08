from add_two_numbers import Solution, ListNode
import unittest

class TestAddTwoNumbers(unittest.TestCase):
    def test_add_two_numbers(self):
        s = Solution()
        l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=ListNode())))
        l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=ListNode())))
        l3 = s.addTwoNumbers(l1, l2)
        l3_expected = ListNode(val=7, next=ListNode(val=0, next=ListNode(val=8, next=ListNode())))

        assert l3.val == l3_expected.val

