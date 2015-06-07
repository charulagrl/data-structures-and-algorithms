import linked_list as ll


def initialize_linked_list():
	lList = ll.LinkedList()
	lList.insert(4)
	lList.insert(5)
	lList.insert(13)
	lList.insert(6)
	lList.insert(9)
	lList.insert(41)
	lList.insert(8)
	lList.insert(27)
	lList.insert(33)

	lList.print_list()
	print lList.search(lList.head, 5, 1)
	return lList.head

def initialize_linked_list_by_array(elements):

	lList = ll.LinkedList()


	for element in elements:
		lList.insert(element)

	lList.print_list()

	return lList.head
