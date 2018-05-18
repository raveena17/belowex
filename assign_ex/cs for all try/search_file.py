import argparse
import glob
from config1 import *
def file_searching(word,word1):
  for files in searching_file:
   for x in glob.glob(files):
    file_open = open(x, 'r')
    contents=file_open.read()
    if word and word1 in contents:
        print (x)
        
if __name__=="__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("searchword",  help="word1")
  parser.add_argument("searchword1", help="word2")
  args = parser.parse_args()
  print file_searching(args.searchword,args.searchword1)

