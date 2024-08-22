class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def last_node(self):
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next

        return current_node

    def insert_last(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            return node
        
        #Traverses the LL to the end in order to add new node.
        last_node = self.last_node()
        last_node.next = node

    def insert_start(self, data):
        prev_head = self.head
        new_head = Node(data)

        new_head.next = prev_head
        self.head = new_head
        return new_head.data

    def insert_at_index(self, data, index):
        new_node = Node(data)
        
        if index == 0:
            self.insert_start(data)
        
        list_index = 0
        current_node = self.head
        while current_node.next != None:
            if list_index == index-1:
                new_node.next = current_node.next
                current_node.next = new_node
            
            list_index += 1
            current_node = current_node.next

        current_node.next = None
        return current_node


    def delete_start(self):
        if self.head == None:
            print("Linked List is empty.")
            return self.head

        self.head = self.head.next

    def delete_end(self):
        if self.head == None:
            print("Linked List is empty. Invalid input.")
            return
        
        #checks if LL is one item.
        if self.head.next == None:
            self.head = None
            return
        
        #.next.next to check 2 lists ahead while staying 1 step behind the final list
        current_node = self.head
        while current_node.next.next != None:
            current_node = current_node.next

        current_node.next = None
        return current_node

    def delete_at_index(self, index):
        if self.head == None:
            print("Linked List is empty. Invalid Input.")
            return

        if index == 0:
            self.delete_start()

        list_index = 0
        current_node = self.head
        while current_node.next != None:
            if list_index == index-1:
                current_node.next = current_node.next.next
                return
            
            list_index += 1
            current_node = current_node.next
        
        print(f"Index {index} is invalid.")
        return
    
    def reverse_LL(self):
        previous_node = None
        current_node = self.head
        
        while current_node != None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        
        self.head = previous_node

    def find_middle_elem(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        
        return slow_pointer if slow_pointer else None


    def print_LL(self):
        #printing the first item of the LL whether a loop or not.
        current_node = self.head
        visited_nodes = set()
        print(f"Head: {current_node.data}")
        visited_nodes.add(current_node)

        #if LL is 1 item, the current_node.next = None. In python, you can't do any operations with None. 
        if current_node.next == None:
            print("Null")
            return
        
        #after checking if LL is not item, normal traversal continues.
        current_node = current_node.next
        
        while current_node.next != None:
            if current_node in visited_nodes:
                print(f"Loop start: {current_node.data}")
                return #end of LL. a loop
            
            print(current_node.data)
            visited_nodes.add(current_node)
            current_node = current_node.next
        
        print(current_node.data)
        print("Null")

    def search_item(self, data):
        current_node = self.head
        while current_node != None:
            if current_node.data == data:
                return True
            
            current_node = current_node.next
            
        print(f"{data} not in linked list.")
        return False
    
    def create_loop(self, index):
        if index < 0:
            print("Invalid index.")
            return
        loop_start = self.head
        last_node = self.last_node()

        for _ in range(index):
            if loop_start == None:
                print("Linked list is empty. Invalid input.")
                return
            
            loop_start = loop_start.next
            
        last_node.next = loop_start
        return

    def check_if_loop(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer.next and fast_pointer != None:
            if slow_pointer.next == fast_pointer.next:
                return True
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        
        return False
    
    def sort_LL(self, head):
        def merge_sorted_LL(llist1, llist2):
            temp_node = Node(0)
            current_node = temp_node
            
            while llist1 and llist2:
                if llist1.data < llist2.data:
                    current_node.next = llist1
                    llist1 = llist1.next
                else:
                    current_node.next = llist2
                    llist2 = llist2.next
                current_node = current_node.next
            
            if llist1:
                current_node.next = llist1
            else:
                current_node.next = llist2
            
            return temp_node.next
        
        def find_middle_elem(head):
            if head is None or head.next is None:
                return head

            slow = head
            fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            return slow
        
        if not head or not head.next:
            return head

        mid = find_middle_elem(head)
        right = mid.next
        mid.next = None

        left = self.sort_LL(head)
        right = self.sort_LL(right)

        return merge_sorted_LL(left, right)

        
ll = LinkedList()

ll.insert_last(3)
ll.insert_last(5)
ll.insert_last(2)
ll.insert_last(1)

ll.print_LL()
ll.head = ll.sort_LL(ll.head)
ll.print_LL()
