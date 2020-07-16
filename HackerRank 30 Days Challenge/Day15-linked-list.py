class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):

        new_node = Node(data)
        if head is None:
            return new_node

        # head is the linked list with a reference to the head node.
        cur = head

        # Just iterating through the until the last null pointer
        while cur.next:
            cur = cur.next

        # connect the new node with the pointer and now the linked list has one more node
        # modifying the cur list is modifying the head list
        cur.next = new_node

        # return the whole list to be called as another head until the input is finished
        return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)
