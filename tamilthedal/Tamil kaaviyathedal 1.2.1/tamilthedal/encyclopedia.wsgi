import os
import sys

from django.core.handlers.wsgi import WSGIHandler

sys.path = ['/home/5gtech/webapps/tamilthedal2/', '/home/5gtech/webapps/tamilthedal2/lib/python2.6/', '/home/5gtech/webapps/tamilthedal2/Whoosh-0.3.2', '/home/5gtech/webapps/tamilthedal2/Whoosh-0.3.2/Whoosh-0.3.2/build/lib/'] + sys.path
sys.path.append('/home/5gtech/webapps/tamilthedal2')
sys.path.append('/home/5gtech/webapps/tamilthedal2/encyclopedia')

os.environ['DJANGO_SETTINGS_MODULE'] = 'encyclopedia.settings'
application = WSGIHandler()
