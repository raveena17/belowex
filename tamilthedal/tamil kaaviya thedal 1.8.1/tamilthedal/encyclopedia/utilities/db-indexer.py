import sys
import os
from datetime import datetime
from whoosh.analysis import *
from whoosh.index import create_in
from whoosh.fields import *
import sqlite3

DB = "thedal.db" #copied from the django admin application
index_dir = "index"
analyzer = SpaceSeparatedTokenizer()
schema = Schema(id = ID(unique=True, stored=True), \
    key_ta = KEYWORD(stored=True, scorable=True),\
    key_en = KEYWORD(stored=True, scorable=True,lowercase=True), \
    content=TEXT(stored=True,analyzer = analyzer))

#schema = Schema(id = ID(unique=True, stored=True), \
 #   key_ta = KEYWORD(stored=True, scorable=True,analyzer=analyzer),\
 #   key_en = KEYWORD(stored=True, scorable=True,lowercase=True,analyzer=analyzer), \
 #   content=TEXT(stored=True,analyzer = analyzer))

if not os.path.exists(index_dir):
	os.mkdir(index_dir)
else:
    os.system("rm %s/*" % (index_dir))
	
ix = create_in(index_dir, schema)
writer = ix.writer()

try:
    conn = sqlite3.connect(DB)
except:
    print "Failed to connect to DB!"
    sys.exit(0)

c = conn.cursor()
c.execute("SELECT * FROM tamilthedal_Entry")

ct = 0
for id, ta, en, content in c:
    writer.add_document(id = unicode(id), key_ta = ta, key_en = en, content = content) 
    ct = ct + 1
writer.commit()

print "%s entries indexed!" % (str(ct))
sys.exit(0)

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
