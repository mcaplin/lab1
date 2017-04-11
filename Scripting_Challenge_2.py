"""bz2 Module to decompress .bz2 files"""
import bz2

"""Input file and create export file called RS_Out.txt"""
inp = bz2.BZ2File('RS.txt.bz2', 'r')
output = open('RS_Out.txt', 'w')

"""Initialize dictionary. Keys will be proteins in 1st column and values
    will be candidate binding partner in 2nd column and probability of
    interaction in 4th column"""
dic = {}

"""Initialize list to hold values read from inp to make it easy to
    separate the columns from the input file."""
lst = []

"""This loop adds the first 2000 proteins to dic.
    i is a counter to put first 2000 proteins from file into lst. Initialize to 0.
    Increments every time the while loop runs."""
i = 0
while len(dic) <= 2000: 
    
    """readline() reads the lines one at a time. strip() removes newline characters.
    split('\t') removes the tabs. Creates a 2D array since appending to lst one
    length 4 array at a time."""
    lst.append(inp.readline().strip().split('\t'))

    a0 = lst[i][0]
    a1 = lst[i][1]
    a3 = lst[i][3]
    """If new key, add it to dic. If dic already has key, append matching protein
        and its probability of interaction to key"""
    if dic.has_key(a0):
        dic[a0].append((a1,a3))
    else:
        dic[a0] = [(a1,a3)]
    i += 1
        
"""Write a header to output file to make it easy to read"""
output.write('protein      :  best match  :   probability     : # matches\n\n')

"""This while loop is to print it nicely.
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
    s = str(p1)  + " : " + str(p2) + " : " + str(prob) + ' : ' + str(num) +'\n\n'
    output.write(s)
    """Remove this entry from dic so while loop moves to next protein."""
    dic.pop(p1)

"""Close files"""
inp.close()
output.close()