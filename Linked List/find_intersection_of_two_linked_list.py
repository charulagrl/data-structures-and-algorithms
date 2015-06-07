import initialize 

def find_intersection_of_two_linked_list(head1, head2):
	if not head1 or not head2:
		raise ValueError ("Linked list are empty")

	current1 = head1
	current2 = head2

	while current1 and current2:
		if current1.data < current2.data:
			current1 = current1.nextnode
		elif current2.data < current1.data:
			current2 = current2.nextnode
		elif current1.nextnode == current2.nextnode:
			current1 = current1.nextnode
			current2 = current2.nextnode
			return "Linked list intersect at %s"%str(current1.nextnode.data)
			

	return 'Lists do not intersect'


head1 = initialize.initialize_linked_list_by_array([30,15,9,6, 3])
head2 = initialize.initialize_linked_list_by_array([30, 15, 10])

print find_intersection_of_two_linked_list(head1, head2)