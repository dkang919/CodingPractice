### Solution by vanAmsen

## Two pointer method 
## Generates two pointer with different speed/moves per turn
## if cycle does exist, then the two pointers will meet again!

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # two-pointer method 
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


## Hash Table Method
## if a node is encountered that already exists in the hash table, a cycle is confirmed

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # hash table method

        records = set()
        current = head

        while current:
            if current in records:
                return True
            records.add(current)
            current = current.next
        
        return False