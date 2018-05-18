import argparse
import re
import glob
from config1 import *
def file_searching(word):
  ''' given all word present'''
  # check and condition
  file_path1=[]
  file_path2=[]
  for files in searching_file:
   for x in glob.glob(files): # find the path of the file
    file_open = open(x, 'r')
    contents=file_open.read()
    for strng in word:
      if  strng in contents:
          file_path1.append(strng)
      if strng not in contents:
          file_path2.append(strng)   
   if file_path2 not in file_path2:
        print (x)
def file_searching1(word):
  ''' given anyone word present'''
  # check or condition
  for files in searching_file:
   for x in glob.glob(files): # find the path of the file
    file_open = open(x, 'r')
    contents=file_open.read()
    for strng in word:
      if strng in contents:
        print (x)
        
if __name__=="__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("searchword", nargs='*', help="word1")#pass positional argument
  parser.add_argument("-o", "--verbose",  help="word", action='store_true')# pass optional argument
  args = parser.parse_args()
  #import pdb; pdb.set_trace()
  if args.verbose:
        print (file_searching1(args.searchword))
  else: 
        print (file_searching(args.searchword))
         
      
