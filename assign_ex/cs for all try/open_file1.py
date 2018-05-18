import glob
import os
#os.chdir( "f:/s" )
#import pdb;pdb.set_trace()

for root, dirs,files in os.walk("c:\\sugn"):
    for name in files:
        result=(os.path.join(root, name))


    #for files in glo
        f = open( result, 'r' )
        file_contents = f.read()
        if "clear" in file_contents:
            print  result
            #print (os.getcwd())
        
    # p=path('f.name').abspath()
    
        '''for root, dirs,files in os.walk("*.py",topdown = False):
                for f.name in files :
                    print(os.path.join(dirs,f.names))'''
        f.close()
