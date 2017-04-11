"""bz2 Module to decompress .bz2 files"""
import bz2

"""Input file and create export file called RS_Out.txt"""
inp = bz2.BZ2File('RS.txt.bz2', 'r')
output = open('RS_Out.txt', 'w')

"""Initialize dictionary. Keys will be proteins in 1st column and values
    will be candidate binding partner in 2nd column and probability of
    interaction in 4th column"""
dic = {}

"""Initialize list to hold values read from inp"""
lst = []

"""n is a counter to get the first 2000 proteins. Initialize to 0. Increments
    every time a new protein is added to lst.

    While loop to put lines from file into lst.

    readline() reads the lines one at a time. strip() removes newline characters.
    split('\t') removes the tabs. Creates a 2D array since appending to lst one
    length 4 array at a time."""
n = 0
while n <= 2000:    
    lst.append(inp.readline().strip().split('\t'))
    if lst[n] in lst:
        n += 1

"""Add keys (proteins in column 1) and 
    values (proteins in column 2, probability in column 4) to dic"""
for i in range(len(lst)):
    a0 = lst[i][0]
    a1 = lst[i][1]
    a3 = lst[i][3]
    """If new key, add it to dic. If dic already has key, append matching protein"""
    if dic.has_key(a0):
        dic[a0].append((a1,a3))
    else:
        dic[a0] = [(a1,a3)]
        
"""Write a header to output file to make it easy to read"""
output.write('protein \tbest match\tprobability\t\t# matches\n\n')

"""This whole blurb of code is to print it nicely.
    Each loop is for a different protein."""
while len(dic) > 0:
    """p2 will be the protein with the highest probability of interaction.
        prob will be the highest probability of interaction.
        num will be the number of interactions."""
    p2 = ''
    prob = 0
    num = 0
    
    """This for loop finds the number of interactions per protein"""
    for key in dic:
        tempNum = len(dic[key])
        if tempNum > num:
            num = tempNum
            p1 = key
            
    """This for loop finds the highest probability and the associated protein"""
    for protein in dic[p1]:
        tempPro = protein[1]
        if tempPro > prob:
            prob = tempPro
            p2 = protein[0]
            
    """Write the protein, best matching protein, probability of interaction with
        the best matching protein, and number of interactions into the
        output file."""
    s = str(p1)  + "\t" + str(p2) + "\t" + str(prob) + '\t' + str(num) +'\n\n'
    output.write(s)
    """Remove this entry from dic so while loop moves to next protein."""
    dic.pop(p1)

"""Close files"""
inp.close()
output.close()