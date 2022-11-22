
'''
Write a program that counts fruit.

Input: 
Line 1, n representing how many fruits there will be

Line 2-n, character for fruit followed by how many of each fruit 
are required to create a full glass of juice

Final line, string containing all given fruit in no particular order

ex:
1
F 4
FFFFFFFF

output: 2

1
E 2
EEEEEEE

output: 3

3
F 3
C 4
D 2
CFDDFCCFDCDDFCFDFCDFC

output: 7 

(7 total were made from each type of fruit (f->2, C->2, D->3)))

'''

i = int(0)
numFruits = int(input())

while i < numFruits:
    fruits = input()
    i += 1



