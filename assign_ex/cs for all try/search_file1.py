import argparse
import glob
from config1 import *
def file_searching(word):
  ''' given all word present'''
  # check and condition
  strng=[]
  lenghth_word=0
  for files in searching_file:
   for x in glob.glob(files): # find the path of the file
    file_open = open(x, 'r')
    contents=file_open.read()
    lenghth_word = len(word)
    #print lenghth_word
    for i in word:
      strng+=i
      #print i
    print len(i)
      #print i
    if str(word) in contents:
       #strng+=i
      #print len(i)
      #print i
      #print (strng)
        print (x)

def file_searching1(word):
  ''' given anyone word present'''
  # check or condition
  for files in searching_file:
   for x in glob.glob(files): # find the path of the file
    file_open = open(x, 'r')
    contents=file_open.read()
    if contents  in word:
        print (x)
        
if __name__=="__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("searchword",  help="word1")
  parser.add_argument("-o", "--verbose",   help="word", action='store_true')
  args = parser.parse_args()
  if args.verbose:        
    for _, value in parser.parse_args()._get_kwargs():
      if value is not None:
          print value
    print file_searching1(value)
    if (str(False)):
           break
      #print file_searching1(verbose)
  else:
    for _, value in parser.parse_args()._get_kwargs():
      if value is not None:
           print value
    print file_searching(value)
    if (str(False)):
             break'''
         print file_searching(searchword)
      
