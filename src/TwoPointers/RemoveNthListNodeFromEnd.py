from typing import List, Optional

class ListNode:
    def __init__(self, val: int, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    right = head
    left = head

    for _ in range(n):
        right = right.next

    if not right:
        return head.next

    while right.next:
        right = right.next
        left = left.next

    left.next = left.next.next
    return head

# Helper to build linked list from list
def build_linked_list(values: List[int]) -> ListNode:
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

# Helper to display linked list
def print_linked_list(head: ListNode) -> None:
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

# Driver/test code
if __name__ == "__main__":
    inputs = [
        [23, 89, 10, 5, 67, 39, 70, 28],
        [34, 53, 6, 95, 38, 28, 17, 63, 16, 76],
        [288, 224, 275, 390, 4, 383, 330, 60, 193],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [69, 8, 49, 106, 116, 112, 104, 129, 39, 14, 27, 12]
    ]
    ns = [4, 1, 6, 9, 11]

    for i, (vals, n) in enumerate(zip(inputs, ns), start=1):
        head = build_linked_list(vals)
        print(f"{i}.\tLinked List:\t\t", end="")
        print_linked_list(head)

        print(f"\tn = {n}")
        updated_head = remove_nth_from_end(head, n)
        print(f"\tUpdated Linked List:\t", end="")
        print_linked_list(updated_head)

        print("-" * 100)