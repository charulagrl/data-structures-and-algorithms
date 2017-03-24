def arrayEdit(s1, s2):
	length1 = len(s1)
	length2 = len(s2)

	diff = length1 - length2

	if diff < -1 or diff > 1:
		return False

	else:
		flag = False
		index1 = 0
		index2 = 0

		while (index1 < length1 and index2 < length2):
			if diff == 0 and s1[index1] != s1[index2]:
				if !flag:
					flag = True
				else:
					return False

