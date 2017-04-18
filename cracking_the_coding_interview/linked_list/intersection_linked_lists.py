# coding: UTF-8

'''
    Problem: Write a program to find the intersection of two linked list.

    Solution: Calculate the length of both linked lists and find the difference between the two. Then move a pointer in the 
    longer linked list forward by the difference in lengths, then compare each element of the linked list. If two nodes 
    matches check rest of the linked list and if same, return the intersection point. 

    Example: 
        33 4 8 41 9 6 13 5 4

        8 10 9 6 13 5 4

        Result: 9

'''

import linked_list

def check_Rest_of_node(linked_list1, linked_list2):
    '''When two nodes matches, check if remaining lists are same'''
    while (linked_list1 != None and linked_list2 != None):
        if (linked_list1.data != linked_list2.data):
            return False

        linked_list1 = linked_list1.nextnode
        linked_list2 = linked_list2.nextnode

    return True

def find_intersection(linked_list1, linked_list2, difference):
    '''Check if two linked lists are intersecting'''
    for i in range(difference):
        linked_list1 = linked_list1.nextnode

    while (linked_list1 != None and linked_list2 != None):
        if linked_list1.data == linked_list2.data:
            intersection_node = linked_list1.data
            if check_Rest_of_node(linked_list1, linked_list2):
                return intersection_node
        
        linked_list1 = linked_list1.nextnode
        linked_list2 = linked_list2.nextnode
    
    return False

def find_intersection_helper(linked_list1, linked_list2):
    '''Calculate the difference between length of two linked lists and call find_intersection function'''
    len_1 = linked_list1.get_size()
    len_2 = linked_list2.get_size()

    if len_1 > len_2:
        difference = len_1 - len_2
        return find_intersection(linked_list1.head, linked_list2.head, difference)

    else:
        difference = len2 - len_1
        return find_intersection(linked_list2, linked_list1, difference)

if __name__ == "__main__":
    # Initialize linked list 1
    linked_list1 = linked_list.initialize_linked_list()
    
    # Initialize linked list 2
    linked_list2 = linked_list.LinkedList()
    linked_list2.insert(4)
    linked_list2.insert(5)
    linked_list2.insert(13)
    linked_list2.insert(6)
    linked_list2.insert(9)
    linked_list2.insert(10)
    linked_list2.insert(8)

    linked_list1.print_list()
    linked_list2.print_list()
    print find_intersection_helper(linked_list1, linked_list2)
