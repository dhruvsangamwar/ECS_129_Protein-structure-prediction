# Protein-structure-prediction
 This is a program that will compare the RSMD (root-mean-square-deviation) between a molecular geometry predicted by AlphaFold, and 
 molecular geometry known through experimentation. The algorithm for this program was derived from this paper : https://www.cs.ucdavis.edu/~koehl/Teaching/ECS129/Projects/Coutsias_2004.pdf

Instructions on how to use the program:  
1. Clone the repository. 
2. Use ```pdparser.py``` to go through the gold standard file and find the single letter notation for all the CA atoms, and then input that into AlphaFold.
3. Ensure that you have both the two pdb files you want to comapre in the working directory. 
4. Use ```python/python3 dataframe.py``` to compile the program if the executable is not given to you. 
