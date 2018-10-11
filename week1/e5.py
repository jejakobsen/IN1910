"""
(This is Project Euler problem 22)

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name, multiply this value by its 
alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

Hint: By "alphabetical value" they mean the sum of the characters in the name,
if each character is converted into its position in the alphabet, so A=1, B=2, etc.
"""
import os
import string

def read_txt():
    os.chdir(r'C:\Users\jensj\OneDrive\Skrivebord\IN1910\IN1910\exercises\week1')
    with open('names.txt', 'r') as names:
    	data = names.read()
    data1 = data.replace(","," ")
    data2 = data1.replace('"',' ')
    data3 = data2.split()
    return data3

names = sorted(read_txt())

num = range(1,25,1)
alph = dict(zip(string.ascii_uppercase, range(1,28)))

def eval_names(name,i):
	sum_name = 0.0
	letters = list(name)
	for l in letters:
		sum_name += alph[l]
	return sum_name*i

sum_names = 0.0 
for name in names:
	sum_names += eval_names(name,names.index(name)+1)

print(sum_names)	

"""
C:\\Users\\jensj\\OneDrive\\Skrivebord\\IN1910\\week1>python e5.py
871198282.0
"""