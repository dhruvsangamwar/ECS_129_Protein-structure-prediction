# this program needs to parse through the C- alpha mcl. gold standard file and
# return the recognized letters for alphafold
import subprocess
import os
import os.path
import csv


def validateInput(file):
    cur_dir = os.getcwd()
    while True:
        file_list = os.listdir(cur_dir)

        if file in file_list:
            return True
        else:
            print("File does not exist in the current directory.")
            print("Accepted format: filename.pdb")
            return False


def takeInput():
    file = input("Please enter the pdb file you want to use for alphaFold: ")
    if validateInput(file) is True:
        command1 = ("awk '{if($3==\"CA\") print $4}' " + file + ">> AF.txt")
        subprocess.call(command1, shell=True)
    else:
        takeInput()


takeInput()

# add the if statements here and append the file
string = "One Letter Sequence: "
with open("AF.txt") as file:
    for line in file:
        if line.rstrip() == "ALA":
            string = string + "A"

        if line.rstrip() == "ARG":
            string = string + "R"

        if line.rstrip() == "ASN":
            string = string + "N"

        if line.rstrip() == "ASP":
            string = string + "D"

        if line.rstrip() == "CYS":
            string = string + "C"

        if line.rstrip() == "GLU":
            string = string + "E"

        if line.rstrip() == "GLN":
            string = string + "Q"

        if line.rstrip() == "GLY":
            string = string + "G"

        if line.rstrip() == "HIS":
            string = string + "H"

        if line.rstrip() == "ILE":
            string = string + "I"

        if line.rstrip() == "LEU":
            string = string + "L"

        if line.rstrip() == "LYS":
            string = string + "K"

        if line.rstrip() == "MET":
            string = string + "M"

        if line.rstrip() == "PHE":
            string = string + "F"

        if line.rstrip() == "PRO":
            string = string + "P"

        if line.rstrip() == "SER":
            string = string + "S"

        if line.rstrip() == "THR":
            string = string + "T"

        if line.rstrip() == "TRP":
            string = string + "W"

        if line.rstrip() == "TYR":
            string = string + "Y"

        if line.rstrip() == "VAL":
            string = string + "V"

print(string)

os.remove("AF.txt")
