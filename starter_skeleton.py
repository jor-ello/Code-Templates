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


def configure_CL(args):
    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
    parser.add_argument('filename')           # positional argument, required input
    parser.add_argument('-c', '--count')      # option that takes a value
    parser.add_argument('-v', '--verbose',
                    action='store_true')  # on/off flag
    parsed_args = parser.parse_args(args)
    return parsed_args

def main(args):
    parsed_args = configure_CL(args)
    return

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
