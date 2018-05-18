from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import  User, Book, Comment
from django.db import IntegrityError

def login(request):
	msg = ""
	username = request.POST.get('username')
	password = request.POST.get('password')
	administer_details = Administer.objects.get(pk=1)
	user_detail = User.objects.get(id=1)
	if administer_details.username == username and administer_details.password == password:
		return HttpResponseRedirect('/blog/view_admindetail/')
	if user_detail.username == username and user_detail.password == password :
	    return HttpResponseRedirect('/blog/view_userdetail/')
	#elif administer_details.username != username or administer_details.password != password or user_detail.username != username or user_detail.password != password : 
	#else:
		#msg = "invalid login"
	    #return HttpResponseRedirect('/blog/')
	return render(request, 'login.html', {'error':msg})

def view_admindetail(request):
	postlist = Book.objects.all()
	context = {'postlist': postlist}
	return render(request, 'administerdetail.html',{'postlist':postlist})

def view_userdetail(request):
	postlist = Book.objects.all()
	context = {'postlist': postlist}
	return render(request, 'view_userdetail.html',{'postlist':postlist})

def get_value(request):
	return render(request,'get.html')
	
def add_book(request):
	bookname = request.POST.get('bookname')
	authorname = request.POST.get('authorname')
	book = Book.objects.create(book_name = bookname, book_author = authorname)
	return HttpResponse('book added successfully')

def delete(request, id):
	book = Book.objects.filter(pk = id).delete()
	return HttpResponse('book deleted successfully')

def get_comment(request,id):
	postlist = Book.objects.get(id = id)
	return render(request,'get_comment.html',{'postlist':postlist})

def add_comment(request, id):
	book = Book.objects.get(id = id)
	#comment_id = book.id
	comment = request.POST.get('comment')
	comment = Comment.objects.create(book=book, comment = comment)
	commentlist = Comment.objects.all()
	return render(request, 'logout.html', {'commentlist':commentlist})

def logout(request):
	return HttpResponse('logout successfully')
    