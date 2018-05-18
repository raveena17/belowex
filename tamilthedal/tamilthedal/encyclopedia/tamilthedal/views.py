from django.shortcuts import render_to_response
from django.http import  HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from encyclopedia.tamilthedal.models import *
import os, string
import sys
import re
from whoosh.index import open_dir
from whoosh.qparser import QueryParser, MultifieldParser
from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT
from whoosh.query import *

specialchars = ['(', ')', '^',':','"', '{', '}', '[', ']']

def sanitize(query):
    if query:
        for x in specialchars:
            query = query.replace(x, '')
        query = query.strip()
    return query

def __getUserDetails__(request):
    if (request.POST.get('username', '') == '' or request.POST.get('password', '') == ''):
        return None

    return User(username = request.POST.get('username', ''), password = request.POST.get('password', ''))

def home(request):
    return render_to_response('index.html', {}, context_instance=RequestContext(request))

def about(request):
    return render_to_response('aboutus.html', {}, context_instance=RequestContext(request))

def contact(request):
    return render_to_response('contactus.html', {}, context_instance=RequestContext(request))

def abbreviations(request):
    return render_to_response('abbreviations.html', {}, context_instance=RequestContext(request))

def login(request):
    #import pdb; pdb.set_trace()
    UserDetails = __getUserDetails__(request)
    if not UserDetails:
        #This is not a POST request. Check whether we are already logged-in
        if request.user and request.user.is_authenticated():
            #User is already logged-in
            return render_to_response('index.html', {}, context_instance=RequestContext(request))
        else:
            return render_to_response('login.html', {}, context_instance=RequestContext(request))
    else:
        #User is trying to log-in
        user = auth.authenticate(username = UserDetails.username, password = UserDetails.password)
        if user is not None:
            auth.login(request, user)
            return render_to_response('index.html', {}, context_instance=RequestContext(request))
        else:
            return render_to_response('login.html', {'msg': 'Invalid username/password'}, context_instance=RequestContext(request));

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/home/")

@login_required
def editentry(request):
    id = request.GET.get('id', '')
    if id == '':
        return render_to_response('editdata.html', {'mode':'Create'}, context_instance=RequestContext(request));
    else:
        index = open_dir(settings.INDEX_PATH)
        srch = index.searcher()
        parser = QueryParser('id', schema=index.schema)
        qry = parser.parse(id)
        results = srch.search(qry)
        if len(results) > 0:
            return render_to_response('editdata.html', {'mode':'Update', 'result':results[0]}, context_instance=RequestContext(request));
        else:
            return render_to_response('editdata.html', {'mode':'Update'}, context_instance=RequestContext(request));

@login_required
def saveentry(request):
    id = request.POST.get('id', '')
    key_ta = request.POST.get('key-ta', '')
    key_en = request.POST.get('key-en', '')
    content = request.POST.get('context', '')

    if key_ta != '' and content != '':
        if id != '':
            entry = Entry(id, unicode(key_ta), key_en, unicode(content))
        else:
            entry = Entry.objects.create()
            entry.key_ta = unicode(key_ta)
            entry.key_en = key_en
            entry.entry = unicode(content)
        entry.save()
        return render_to_response('index.html', {'msg':'Saved successfully'}, context_instance=RequestContext(request));
        

@login_required
def deleteentry(request):
    id = request.GET.get('id', '')
    msg = ''
    if id != '':
        entries = Entry.objects.filter(id=id)
        if entries and len(entries) > 0:
            for entry in entries:
                entry.delete()
            msg = 'Deleted successfully'
        else:
            msg = 'Could not find entry to delete'
    else:
        msg = 'No record passed for delete'
    return render_to_response('index.html', {'msg':msg}, context_instance=RequestContext(request));


def search(request):
    finalresult = []
    query = request.POST.get('transliterate', None)
    if query:
        query = sanitize(query)
        index = open_dir(settings.INDEX_PATH)
        srch = index.searcher()
        parser = MultifieldParser(['key_ta', 'key_en', 'content'],
        schema=index.schema)
        qry = parser.parse(query)
        results = srch.search(qry)
        for res in results:
            if res['key_ta'] and res['content']:
                key = res['key_ta']
                if res['key_en']:
                    key = key + " (" + res['key_en'] + ")"
                
                finalresult.append({'id':res['id'], 'key':key, 'content':res['content'].encode('utf-8')})

    return render_to_response('index.html', {'result': finalresult, 'searchword': query, \
    'totalres': len(finalresult)}, context_instance=RequestContext(request))

def letterSearch(request):
    finalresult = []
    query = request.GET.get('letter', None)
    if query:
        query = sanitize(query)
        index = open_dir(settings.INDEX_PATH)
        srch = index.searcher()
        parser = QueryParser('key_ta', schema=index.schema)
        qry = parser.parse(query + u'*')
        results = srch.search(qry, sortedby="key_ta")
        for res in results:
            if res['key_ta'] and res['content'] and res['key_ta'].startswith(query):
                key = res['key_ta']
                if res['key_en']:
                    key = key + " (" + res['key_en'] + ")"
                
                finalresult.append({'id':res['id'], 'key':key, 'content':res['content'].encode('utf-8')})
    
    return render_to_response('index.html', {'result': finalresult, 'searchword': query, 'totalres': len(finalresult)},\
    context_instance=RequestContext(request))
