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


def takeInput1():
    file = input("Please enter the first pdb file you want to comapre: ")
    if validateInput(file) is True:
        command1 = ("cat " + file +
                    " | grep 'CA' | awk '{print $7 \", \" $8 \", \"$9}' >> protein.csv")
        subprocess.call(command1, shell=True)
    else:
        takeInput1()


def takeInput2():
    file = input("Please enter the second pdb file you want to comapre: ")
    if validateInput(file) is True:
        command1 = ("cat " + file +
                    " | grep 'CA' | awk '{print $7 \", \" $8 \", \"$9}' >> protein.csv")
        subprocess.call(command1, shell=True)
    else:
        takeInput2()


def CsvToDataframe(DataFrame):
    with open("protein.csv") as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            DataFrame.append(row)

        os.remove("protein.csv")
