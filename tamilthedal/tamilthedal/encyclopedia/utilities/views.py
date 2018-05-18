import sys
from datetime import datetime
from whoosh.index import create_in
from whoosh.fields import *
schema = Schema(docTime = ID(unique=True, stored=True),key= TEXT(stored=True),content=TEXT(stored=True))
ix = create_in ("index",schema)
writer = ix.writer()
if len(sys.argv) > 1:
	for file in sys.argv[1:]:
		f = open(file)
		cont = f.read()        	
		eachline = cont.split(':::')
		for each in eachline:
			eachterm = each.split(':') + ['']
			content_G = eachterm[1]
			for i in range(2,len(eachterm)):
				content_G += eachterm[i]				
			print eachterm[0],'first term',content_G , 'second term'
			writer.add_document(docTime = unicode(str(datetime.datetime.now()), 'utf-8'),  
			key = unicode(str(eachterm[0]), 'utf-8'),
			content = unicode(str(content_G), 'utf-8') )
		writer.commit()                
		f.close()
else:
	print 'Provide a file name to index'