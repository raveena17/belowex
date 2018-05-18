def printFileToScreen( fileName ):
    """ simply prints the contents of the file to the screen
        input: fileName, a string with the file's name
    """
    f = file( "cmnd.txt" )       # f is the opened file
    text = f.read()            # text is the name of all of f's text
    f.close()                  # this closes the file f - a good idea
    
    print 'The file contains:' # drumroll
    print                      # blank line
    print text                 # ta da!
