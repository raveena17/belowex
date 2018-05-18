'''import argparse'''
import os
#import pdb;pdb.set_trace()
'''if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("searchword",help="word")
    #parser.add_argument("result",help="found")
    args = parser.parse_args()'''
    
search_word = raw_input('enter the word=')
#search_word1 = raw_input('enter the word=')
file1=open('config.py','r') 
content = file1.read()
print content
for root, dirs,files in os.walk(content):
      for name in files:
        result=(os.path.join(root, name))
        f = open( result, 'r' )
        file_contents = f.read()
        
        if search_word in file_contents:
            print result
        for root, dirs,files in os.walk("*.py",topdown = False):
                for f.name in files :
                    print(os.path.join(dirs,f.names))
        f.close()
'''import os
search_word=raw_input('enter the word:')
search_filename = open('config.py', 'r')
for file_name in search_filename:
 file_name=os.path.abspath('')
 f = open(file_name, 'r')
 file_contents=f.read()
 if search_word in file_contents:
  print file_name'''

