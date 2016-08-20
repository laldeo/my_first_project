from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def newtest_html(request):
	context={}
	return render(request,'newtest_app/test.html',context)