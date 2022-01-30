import subprocess

Command = "cat 6yafA.pdb | grep 'CA' | awk '{print $7 \", \" $8 \", \"$9}' "

subprocess.call(Command, shell=True)
