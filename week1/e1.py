"""
Write a function less_than(original, n) that takes
a list of integers (original) and a number $n$, and
returns a new list of the elements in the original
list that were smaller than $n$. Your function should 
use a list comprehension to do this. Write a few simple 
tests of your function.
"""

def less_then(original,n):
	ls = [o for o in original if o < n]		
	return ls

def test_less_then():
	L = [1,2,3,4,5]
	n1 = 2.7; n2 = 4.9
	L_n1 = [1,2]; L_n2 = [1,2,3,4] 
	test_L1 = less_then(L,n1); test_L2 = less_then(L,n2); 
	msg = 'something is wrong'
	if test_L1 == L_n1 and test_L2 == L_n2:
		msg = 'oki-doki'
	print(msg)	

test_less_then()	