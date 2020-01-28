import argparse
parser = argparse.ArgumentParser()

## Define command line arguments
## Positional (required) arguments
parser.add_argument("file1", help="some file that we're working on")
parser.add_argument("file2", help="some other file that we're working on")
parser.add_argument("number", help="some integer we need", type=int)
## Optional arguments (starting with --)
parser.add_argument("--flag1", help="some optional flag", action="store_true")
parser.add_argument("--option1", help="some optinal parameter")

## Run parsing
args = parser.parse_args()

## In application body, access parsed parameters as fields of args:
print("File 1 parameter: {}".format(args.file1))
print("File 2 parameter: {}".format(args.file2))
print("Number parameter: {}".format(args.number))

## Only if specified
if(args.flag1): 
    print("flag1 was specified")

## Only if specified
if(args.option1): 
    print("Option1 is specified as: {}".format(args.option1))