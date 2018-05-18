import argparse
import glob
from config1 import *
def file_searching(word):
  ''' given all word present'''
  # check and condition
  strng=' '
  strng1=''
  for files in searching_file:
   for x in glob.glob(files): # find the path of the file
    file_open = open(x, 'r')
    contents=file_open.read()
    #print word
    #strng=' '.join(word)
    #print strng
    #for i in word:
        #print i
        #print i
        #strng=''.join(i)
        #for i1 in strng:
       # print strng
     #print i
    strng=' '.join(word)
    print strng
    #for strng in word:   
     #print strng
    #strng1=strng.split(' ')
    #print(word)
    if  strng in contents:
        print(x)

def file_searching1(word):
  ''' given anyone word present'''
  # check or condition
  for files in searching_file:
   for x in glob.glob(files): # find the path of the file
    file_open = open(x, 'r')
    contents=file_open.read()
    if word  in contents:
        print (x)
        
if __name__=="__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("searchword", nargs='*', help="word1")
  #parser.add_argument("searchword1", help="word2")
  parser.add_argument("-o", "--verbose",  help="word", action='store_true')
  #parser.add_argument("-v", "--verbose1", help="word", action='store_true')
  #args = parser.parse_args()
  for _, value in parser.parse_args()._get_kwargs():
    if value is not None:
      print value
      #if value.verbose:
        #print file_searching1(value)
      #else: 
      print file_searching(value)
      if (str(False)):
        break
      #\\
      (str(False))

