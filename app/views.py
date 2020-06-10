from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import models
# Create your views here.

def home_page(request):
	return render(request,'register_form.html')

def save_data(request):
	obj=models.Person(fullname=request.POST['txtn'],nationalid=request.POST['txtnid'],
		age=request.POST['age'],gender=request.POST['gender'],socialstatus=request.POST['status'],
		address=request.POST['txtadd'],phone1=request.POST['phone1'],phone2=request.POST['phone2'],
		email=request.POST['email'])
	obj.save()
	return HttpResponseRedirect('/home')

def show_data(request):
	objects=models.Person.objects.all()
	return render(request,'showdata.html',{'persons':objects})

def delete(request,id):
	obj=models.Person(id=id)
	obj.delete()
	return HttpResponseRedirect('/home')

def update(request,id):
	obj=models.Person.objects.get(id=id)
	return render(request,'update_form.html',{'person':obj})


