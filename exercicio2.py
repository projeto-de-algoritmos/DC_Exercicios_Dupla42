import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        current = dummy

        heap = [(lists[i].val, i) for i in range(len(lists)) if lists[i]]
        heapq.heapify(heap)

        while heap:
            val, i = heapq.heappop(heap)
            current.next = ListNode(val)
            current = current.next

            if lists[i].next:
                lists[i] = lists[i].next
                heapq.heappush(heap, (lists[i].val, i))

        return dummy.next

def convert_to_linked_lists(lists):
    linked_lists = []
    for lst in lists:
        dummy = ListNode(0)
        current = dummy
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        linked_lists.append(dummy.next)
    return linked_lists

lists = [[1,4,5],[1,3,4],[2,6]]
linked_lists = convert_to_linked_lists(lists)
result = Solution().mergeKLists(linked_lists)

output_list = []
current = result
while current is not None:
    output_list.append(current.val)
    current = current.next

print(output_list)