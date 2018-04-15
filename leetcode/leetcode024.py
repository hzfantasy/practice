# Definition for singly-linked list.
import json

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        node = head
        previous_node = None
        if node.next:
            head = node.next

        while node.next:
            current_node = node
            if node.next.next:
                node = node.next.next
                if previous_node:
                    previous_node.next = current_node.next
                previous_node = current_node
                current_node.next.next = current_node
                current_node.next = node
            else:
                if previous_node:
                    previous_node.next = current_node.next
                current_node.next.next = current_node
                current_node.next = None
        return head


def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    while True:
        try:
            line = "[1,2,3,4]\n"
            head = stringToListNode(line)

            ret = Solution().swapPairs(head)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
