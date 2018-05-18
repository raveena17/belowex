import sys
import argparse
import glob
from config1 import *
#def searching_word():

def file_searching(y):
  for i in searching_file:
   for x in glob.glob(i):
    #print(x)
    f = open(x, 'r')
    #print (f)
    contents=f.read()
    if y in contents:
        print (x)
        
if __name__=="__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("searchword", help="word")
  args = parser.parse_args()
  print file_searching(args.searchword)

