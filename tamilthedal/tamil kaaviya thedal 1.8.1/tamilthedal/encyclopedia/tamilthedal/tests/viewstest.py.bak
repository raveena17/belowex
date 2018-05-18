import os
import re

from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
#from django.core import mail
from django.test.client import Client
#from django.contrib import auth
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from whoosh import index , qparser, query
from whoosh.index import open_dir



def setUp(self):
	self.old_TEMPLATE_DIRS = settings.TEMPLATE_DIRS
	settings.TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__),'../../templates'),)


class searchTest(TestCase):
	urls = 'encyclopedia.urls'


	def setUp(self):
		c = Client()
		self.old_TEMPLATE_DIRS = settings.TEMPLATE_DIRS
		settings.TEMPLATE_DIRS = (
		os.path.join(
		os.path.dirname(__file__), '../../templates'),)
		


	def testEngFullTextSearch(self):
		c = Client()
		response = c.post('/search/', {
		'transliterate' :'Arjunan'}
		)
		print 'English - full text search'
		self.assertEquals(response.status_code, 200)
		
	def testEngPartialTextSearch(self):
		c = Client()
		response = c.post('/search/', {
		'transliterate' :'Ava'}
		)
		print 'English - partial text search'
		self.assertEquals(response.status_code, 200)
		
	def testNumTextSearch(self):
		c = Client()
		response = c.post('/search/', {
		'transliterate' :'81'}
		)
		print 'Number search'
		self.assertEquals(response.status_code, 200)
		
	def testSplNoTextSearch(self):
		c = Client()
		response = c.post('/search/', {
		'transliterate' :'-115'}
		)
		print 'Special char n Num search'
		self.assertEquals(response.status_code, 200)
	
	def testDelimiterTextSearch(self):
		c = Client()
		response = c.post('/search/', {
		'transliterate' :':::'}
		)
		print 'demlimiter text search'
		self.assertEquals(response.status_code, 200)
		
	def testTextandSpaceSearch(self):
		c = Client()
		response = c.post('/search/', {
		'transliterate' :'Kharakarmi, '}
		)
		print 'text and space search'
		self.assertEquals(response.status_code, 200)
		
	def testBraceandTextSearch(self):
		c = Client()
		response = c.post('/search/', {
		'transliterate' :'(Kala '}
		)
		print '( and text search'
		self.assertEquals(response.status_code, 200)
		
	def testspecialchar1Search(self):
		c = Client()
		response = c.post('/search/', {
		'transliterate' :': '}
		)
		print ': search'
		self.assertEquals(response.status_code, 200)
		
	def testspecialchar2Search(self):
		c = Client()
		response = c.post('/search/', {
		'transliterate' :'^'}
		)
		print '^ search'
		self.assertEquals(response.status_code, 200)
	
	def testspecialchar2Search(self):
		c = Client()
		response = c.post('/search/', {
		'transliterate' :')'}
		)
		print ') search'
		self.assertEquals(response.status_code, 200)
		
	def testspecialchar3Search(self):
		c = Client()
		response = c.post('/search/', {
		'transliterate' :"'"}
		)
		print "' search"
		self.assertEquals(response.status_code, 200)
	
	def testspecialchar4Search(self):
		c = Client()
		response = c.post('/search/', {
		'transliterate' :'*'}
		)
		print 'wildcard search'
		self.assertEquals(response.status_code, 200)
	
	def testspecialchar5Search(self):
		c = Client()
		response = c.post('/search/', {
		'transliterate' :'*?'}
		)
		print 'wildcards search'
		self.assertEquals(response.status_code, 200)
	
	def testspecialchar5Search(self):
		c = Client()
		response = c.post('/search/', {
		'transliterate' :'4*?'}
		)
		print 'number and wildcards search'
		self.assertEquals(response.status_code, 200)
		
	def testTamFullTextSearch(self):
		f = open(settings.FILE_NAME)
		cont = f.readline()
		lineone = cont.split(':::')
		c = Client()
		response = c.post('/search/', {
		'transliterate' : lineone[0] }
		)
		print 'Tamil - full text search'
		self.assertEquals(response.status_code, 200)
		
	def testTamPartialTextSearch(self):
		f = open('/home/nanditha/projects/tamilthedal/trunk/src/encyclopedia/utilities/pyunitletters')
		cont = f.readline()
		letter = cont.split(':')
		c = Client()
		response = c.post('/search/', {
		'transliterate' : letter[0]}
		)
		print 'Tamil - Partial text search'
		self.assertEquals(response.status_code, 200)


	def testLetterSearch(self):
		f = open('/home/nanditha/projects/tamilthedal/trunk/src/encyclopedia/utilities/pyunitletters')
		cont = f.readline()
		letter = cont.split(':')
		c = Client()
		response =c.post('/letterSearch/', {
		'letter': letter[0]}
		)
		print 'letter wise search'
		self.assertEquals(response.status_code, 200)
	
	def test_wildcard1(self):
		qp = qparser.QueryParser("content")
		q = qp.parse("hello *the?e* ?star*s? test")
		self.assertEqual(len(q.subqueries), 4)
		self.assertEqual(q[0].__class__.__name__, "Term")
		self.assertEqual(q[0].text, "hello")
		print q[0].text , 
		self.assertEqual(q[1].__class__.__name__, "Wildcard")
		self.assertEqual(q[1].__class__.__name__, "Wildcard")
		self.assertEqual(q[1].text, "*the?e*")
		print q[1].text 
		self.assertEqual(q[2].__class__.__name__, "Wildcard")
		self.assertEqual(q[2].text, "?star*s?")
		print q[2].text 
		self.assertEqual(q[3].__class__.__name__, "Term")
		self.assertEqual(q[3].text, "test")
		print q[3].text 
		
	
	def test_endstar(self):
		qp = qparser.QueryParser("content")
		q = qp.parse("word*")
		self.assertEqual(q.__class__.__name__, "Prefix")
		self.assertEqual(q.text, "word")
		print q.text, 'query text'
		
	def test_tamilprefix(self):
		f = open('/home/nanditha/projects/tamilthedal/trunk/src/encyclopedia/utilities/pyunitwildtext')
		cont = f.readline()
		text = cont.split(':')
		index = open_dir(settings.INDEX_PATH)
		wildtext = unicode(str(text[0]), 'utf-8') + u'*'
		qp = query.Wildcard("content" , wildtext)
		srch = index.searcher()
		res  = srch.search(qp)
		self.assertNotEqual(len(res) , 0)
		print len(res), 'results'
		

	

