''' Agenda: Create a Numpy Array from a List, Tuple with Float datatype '''

# imports
from typing import Any 
from typing import List 

import numpy

print("Numpy imported succesfully") 

# helper function 
def sep() -> None : 
    seperator : str = '-------------------------------------------------'
    print(seperator)
    return None

# Driver Code 
if __name__ == "__main__" :
    
    # List into numpy array 
    p : List[int] = [1,2,3,4,5] 
    p_n : Any = numpy.array(p , dtype=numpy.float64) 
    print(f"Array before: {p}")
    print(f"Numpy Converted: {p_n}") 
    sep() 

    # Tuple into numpy array
    q : List[int] = (1,2,3,4,5)
    q_n : Any = numpy.array(q, dtype=numpy.float64) 
    print(f"Tuple before: {q}")
    print(f"Numpy Converted: {q_n}")
    sep()

    print("Program ran succesfully")