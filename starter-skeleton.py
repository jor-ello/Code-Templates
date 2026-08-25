# Imported libraries/packages/files
import pydantic
import argparse


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


def configure_CL(parser):
    parser.add_argument('filename')           # positional argument, required input
    parser.add_argument('-c', '--count')      # option that takes a value
    parser.add_argument('-v', '--verbose',
                    action='store_true')  # on/off flag
    args = parser.parse_args()
    return args

def main(arg1="okay",arg2="we",arg3="ride"):
    print(arg1)
    print(arg2)
    print(arg3)
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

    args = configure_CL(parser)
    arg1 = ""
    if(args.filename):
       arg1 = args.filename
    else:
       arg1 = "oops"

    main(arg1=arg1)
