# imports 
import numpy as np 
from numpy.linalg import eig 
from typing import List 
from typing import Any 

# type definations
Vector = List[List[int]]

# Driver Code 
if __name__ == "__main__": 
    p : Vector = [[1,2,3], 
                  [4,5,6],
                  [7,8,9]]
    
    val : List[int] = eig(p)[0]
    vec : Vector = eig(p)[1]
    print(f"Eigen Values are: {val}")
    print(f"Eigen Vectors are : {vec}")

    print("Program executed successfully")