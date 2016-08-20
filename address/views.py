from django.shortcuts import render
from django.http import HttpResponse
from .models import Address

# Create your views here.
def hello_world(request):
	return HttpResponse('hello world!!!')
'''
def test_html(request):
	f=open("/home/tcloudpython/Documents/Addressbook/src/address/templates/test.html")
	content=f.read()
	return HttpResponse()
''' 

def test_html(request):
	context={}
	return render(request,'address/test.html',context)

#def address_html(request):
#	context={}
#	return render(request,'address.html',context)

#def address_html(request):
#	context={'name1':'student1','name2':'student2','email1':'student1@edu.net','email2':'student2@edu.net'}
#	return render(request,'address.html',context)

# def address_html(request):
# 	context={'namesdb':[{'name':'stud1','email':'stud1@gmail.com'},{'name':'stud2','email':'stud2@gmail.com'}]}
# 	return render(request,'address.html',context)

def address_html(request):
	value = Address.objects.all()
	print value
	context={'namesdb':value}
	return render(request,'address.html',context)