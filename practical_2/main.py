# importing the module 
from typing import List
from module import ModularNumericTable 

# driver function 
if __name__ == '__main__': 
    p : int = int(input("Give a Number: "))
    z : List[str] = ModularNumericTable(p).generate_table() 
    print("--------------------------------")
    print(f"** Table for {p} **")
    for i in z: print(i) 
    print("--------------------------------") 
    