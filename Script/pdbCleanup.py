import subprocess
import sys

file1 = input("Please enter the first pdb file you want to comapre: ")

command1 = ("cat " + file1 + " | grep 'CA' | awk '{print $7 \", \" $8 \", \"$9}' >> protein1.csv")

subprocess.call(command1, shell=True)

file2 = input("Please enter the second pdb file you want to comapre: ")

command2 = ("cat " + file1 + " | grep 'CA' | awk '{print $7 \", \" $8 \", \"$9}' >> protein2.csv")

subprocess.call(command2, shell=True)
