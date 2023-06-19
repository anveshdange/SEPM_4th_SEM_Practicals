# Agenda: Create a Numpy Array from a List, Tuple with Float datatype
import numpy
print("Numpy imported succesfully") 

# helper function 
def sep(): print('-------------------------------------------------')

# List into numpy array 
p = [1,2,3,4,5] 
p_n = numpy.array(p, dtype=numpy.float64) 
print(f"Array before: {p}")
print(f"Numpy Converted: {p_n}") 
sep() 

# Tuple into numpy array
q = (1,2,3,4,5)
q_n = numpy.array(q, dtype=numpy.float64) 
print(f"Tuple before: {q}")
print(f"Numpy Converted: {q_n}")
sep()

print("Program ran succesfully")