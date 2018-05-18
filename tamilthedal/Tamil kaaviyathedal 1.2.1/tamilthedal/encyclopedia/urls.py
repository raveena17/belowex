from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
import os.path
from django.contrib.auth.models import User

 #Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        (r'^i18n/', include('django.conf.urls.i18n')),
    	(r'^pages/', include('pages.urls')),
    	(r'^admin/(.*)', admin.site.urls),
)

urlpatterns += patterns('encyclopedia.tamilthedal',
    (r'^$', direct_to_template, {'template': 'index.html'}),
    (r'^home/', 'views.home'),
    (r'^aboutus/', 'views.about'),
    (r'^contactus/', 'views.contact'),
    (r'^abbreviations/', 'views.abbreviations'),
    (r'^login/', 'views.login'),
    (r'^logout/', 'views.logout'),
    (r'^editentry/', 'views.editentry'),
    (r'^saveentry/', 'views.saveentry'),
    (r'^deleteentry/', 'views.deleteentry'),
    (r'^search/', 'views.search'),
	(r'^letterSearch', 'views.letterSearch'),
	
)


    # Example:
    # (r'^encyclopedia/', include('encyclopedia.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),

if settings.DEBUG:
    urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': os.path.join(os.path.dirname(__file__), "media")}),
)
