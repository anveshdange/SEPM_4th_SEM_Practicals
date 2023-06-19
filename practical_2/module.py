# creating a module class to be imported into another module/python file 
from typing import List 

class ModularNumericTable :
    ''' This class implements the numeric table of a number''' 
    # Class COnstructor Interface
    def __init__(self, x : int) -> None :
        self.num = x 

    def generate_table(self) -> List[str] :
        table = []
        for i in range(1,11) :
            table.append(f"{self.num} x {i} = {self.num * i}")
        return table
    
# Driver Function 
if __name__ == "__main__" :
    num_table : ModularNumericTable = ModularNumericTable(10)
    print(num_table.generate_table())

