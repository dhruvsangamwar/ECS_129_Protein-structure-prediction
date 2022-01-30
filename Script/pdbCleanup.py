import subprocess

Command = "cat 6yafA.pdb | grep 'CA' | awk '{print $7 \", \" $8 \", \"$9}' >> degrees.csv"

subprocess.call(Command, shell=True)
