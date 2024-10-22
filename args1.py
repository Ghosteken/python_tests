import sys

if len(sys.argv) < 2:
    sys.exit("You must enter a filename as a command line argument.")
for arg in sys.argv[1:]:
    print(arg)    