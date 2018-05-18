import sys
import os
from datetime import datetime
from whoosh.analysis import *
from whoosh.index import create_in
from whoosh.fields import *

index_dir = "index"
analyzer = SpaceSeparatedTokenizer()
schema = Schema(docTime = ID(unique=True, stored=True),key= TEXT(stored=True, analyzer=analyzer),content=TEXT(stored=True,analyzer = analyzer))

#schema = Schema(docTime = ID(unique=True, stored=True),key= TEXT(stored=True),content=TEXT(stored=True))

if not os.path.exists(index_dir):
	os.mkdir(index_dir)
	
ix = create_in(index_dir, schema)
writer = ix.writer()

if len(sys.argv) > 1:
	for file in sys.argv[1:]:
		contents = open(file).read()
		arr = contents.split('\n\n')
		print len(arr)
		for line in arr:
			if line == '' or (len(line.split(';;')) <= 1):
				continue
			key = line.split(';;')[0]
			content = ' '.join(line.split(';;')[1:])
			print key
						
			writer.add_document(docTime = unicode(str(datetime.datetime.now()), 'utf-8'),  
				key = key.decode('utf-8'),#unicode(key, 'utf-8'),
				content = content.decode('utf-8'))#unicode(content, 'utf-8') )
		print "Finished indexing " + file
	writer.commit()
else:
	print 'Provide a file name to index'
