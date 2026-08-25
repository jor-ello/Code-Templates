# Imported libraries/packages/files
import pydantic



#Specific things imported
from pydantic import BaseModel


#Using pydantic BaseModel to ensure typing is clear and enforced

class ClassName(BaseModel):
    # Insert fields here
    # Format is
    # var_name: type | None
    # None included if it is allowed to be null

    #Insert functions here; need an initialization function
    def __init__(self
         ):
        return



def main():
    print("hello world")
    return

if __name__ == '__main__':
    main()
