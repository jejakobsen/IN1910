"""
Write a function count_chars that takes a string as input, and counts the number of
times each character appears in the string. Case should be ignored, so that both A
and a count as the same letter. The resulting counts should be returned as a dictionary.

Hint 1: Case can be ignored by converting the input to lowercase before analyzing it.
Hint 2: You can loop over the characters of a string
Test your function using the following test-block:
----------------------------------------------
example = "Hello, world!"
for char, count in count_chars(example).items():
    print('{:3}{:10}'.format(char, count))
----------------------------------------------
Finally, copy this print example in the test-block and change it so 
that the characters are lister in alphabetical order. Now add an example where
they are printed in order of how many times they occur in the text.

"""
from collections import Counter
import operator

def count_chars(string): 
	s = string.lower()
	s1 = s.replace(" ","")
	s2 = sorted(s1)
	s3 = Counter(s2)
	return s3

example = "Hello, world!"
for char, count in count_chars(example).items():
    print('{:3}{:10}'.format(char, count))

print('-------------')    

for char, count in sorted(count_chars(example).items(), key=operator.itemgetter(1), reverse = True):
    print('{:3}{:10}'.format(char, count))

"""
C:\\Users\\jensj\\OneDrive\\Skrivebord\\IN1910\\week1>python e3.py
!           1
,           1
d           1
e           1
h           1
l           3
o           2
r           1
w           1
-------------
l           3
o           2
!           1
,           1
d           1
e           1
h           1
r           1
w           1
"""    
