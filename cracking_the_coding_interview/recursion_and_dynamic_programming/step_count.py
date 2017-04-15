# -*- coding: UTF-8 -*-

'''
	Problem: A child is running up the staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
	Implement a method to count how many possible ways the child can run up the stairs.
'''

def step_recursive(n):
	''' Recursive solution to count the possible ways to run up the stairs '''
	if n < 0:
		return 0

	if n == 0:
		return 1
	
	else:
		return step_recursive(n-1) + step_recursive(n-2) + step_recursive(n-3)

def step_dynamic(n, mem):
	''' Calculates the possible ways to run up the stairs using dynamic programmic '''
	if n < 0:
		return 0

	if n == 0:
		return 1

	if mem[n] > -1:
		return mem[n]
	else:
		mem[n] = step_dynamic(n-1, mem) + step_dynamic(n-2, mem) + step_dynamic(n-3, mem)
		return mem[n]

if __name__ == "__main__":
	print "Counting possible ways using recursion"
	print step_recursive(4)
	print step_recursive(5)
	print step_recursive(6)
	print "Counting possible ways using dynamic programming"
	print step_dynamic(4, [-1]*5)
	print step_dynamic(5, [-1]*6)
	print step_dynamic(6, [-1]*7)
