import os
import numpy as np
import fileinput
import sys

dirOfNetwork = os.path.dirname(__file__)

with fileinput.FileInput(dirOfNetwork + "/Datasets/mainData_Normalized2.csv", inplace=True) as file:
    for line in file:
        print(line.replace("\n"+"\n", "\n"), end="")

print("\n 1"+"\n 1", end="")
