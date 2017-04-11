"""Regular Expression Module"""
import re

"""Import TCDB file and create export file called TCDB_Out.txt"""
inp = open('TCDB.faa', 'r')
output = open('TCDB_Out.txt', 'w')

"""Read all lines in file"""
p = inp.read()

"""Remove Extra Information, swap IDs, add dash between IDs, add tab"""
p = re.sub(r'>gnl\|TC-DB\|(\d+)\|([\w\.]+).+\n([\s|\w]+)', r'\2-\1\t\3', p)

"""Remove all the newlines after [A-Z] characters"""
p = re.sub(r'(?<=[A-Z])\r?\n', '', p)

"""Add back the newline after the end of the sequence"""
p = re.sub(r'([A-Z])(\d)', r'\1\n\2', p)

"""Write the substituted string into a .txt file"""
output.write(p)

"""Close files."""
inp.close()
output.close()