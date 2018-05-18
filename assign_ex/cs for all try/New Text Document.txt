    The usege of file_search " that would let one to find all files that have at least one instance of the given text.List of files to be taken 
into consideration for search will be provided in config_file using regular expresssions.I have imported argparse library for getting command 
line argument  and glob library used tofinds all the pathnames matching a specified pattern according to the rules used by the Unix shell, 
although results are returned in arbitrary order. ... pathname can be either absolute (like /usr/src/Python-1.5/Makefile ).File_searching function 
used to can take any number of arguments as strings to find in those files. File_search1 used to will list all files that contains either "cat" OR 
"dog" OR both.