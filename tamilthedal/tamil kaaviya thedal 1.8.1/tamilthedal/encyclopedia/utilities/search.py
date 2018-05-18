# -*- coding: utf-8 -*-

import sys
import os, os.path
from whoosh import *
from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT
from whoosh.index import open_dir
from whoosh.filedb.filestore import FileStorage
from whoosh.analysis import *
from whoosh.qparser import *

#keyword = unicode(str(sys.argv[1]))
#keyword = u'உலா'
#keyword = u'உகாண்டா'
#keyword = u'உ'
#keyword = u'உ*'
#keyword = u'இ*'
#keyword = u'ப்ரம்மா,'
#keyword = u'அவரோத'
#keyword = u'அபயா'
#keyword = u'அபயம்'
#keyword = u'அபிபு'
#keyword = u'அ*'
keyword = u'Karnan'
#keyword = u'Abhala'
#keyword = u'Abhaya'
#keyword = u'கர்ணன்'
#keyword = u'ஹர்யாங்கன்'
keyword = u'பீஷ்மர்'

#analyzer = SpaceSeparatedTokenizer()
#schema = Schema(title=TEXT(stored=True, analyzer=analyzer), content=TEXT(stored=True, analyzer=analyzer))
index_dir = "index"

if not os.path.exists(index_dir):
    sys.exit(0)

index = open_dir(index_dir)
searcher = index.searcher()
parser = MultifieldParser(['key','content'], schema=index.schema)
#parser = MultifieldParser(['key'], schema=index.schema)

query = parser.parse(keyword)
#print query
results = searcher.search(query)

print str(len(results)) + " result(s) found!"
for result in results:
    print result["key"].encode('utf-8')
    print "***"
