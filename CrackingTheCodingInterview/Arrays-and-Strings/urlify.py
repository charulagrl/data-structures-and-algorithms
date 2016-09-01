'''

	Problem: Write a program to replace all spaces in a string with "%20". Assuming that string has sufficicient space at the end to hold additional 
	characters, you are given true length of the string.

	example: "Mr John Smith    ", 13
	Output: "Mr%20John%20Smith"

	Solution: Append the letters of the string in a list and when space is found append "%20".

'''

# function to urlify the string
def urlify(s,length):

	count = 0
	new_string = []

	while (count < length):
		if s[count] == " ":
			new_string.append("%")
			new_string.append("2")
			new_string.append("0")

		else:
			new_string.append(s[count])
			
		count += 1

	return ''.join(new_string)



# Testing
s = "Mr John Smith    "
length = 13

print urlify(s, length)

