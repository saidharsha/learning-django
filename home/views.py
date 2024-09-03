from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
''''
# Create your views here.
#def home(request):
   # return HttpResponse("<h1>Hello world</h1>")
#def Indexview(request):
    #return render(request,"app/index.html")
def InsertPageView(request):
    return render(request,"app/insert.html")

def InsertData(request):
    #Data come from HTML to view
    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    contact=request.POST['contact']

    #creating object of model class
    #inserting data inta table
    
    newuser=Student.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact)

     #after insert render on show.html
    #return render(request,"app/show.html")
    return redirect('Showpage')

#show page view
def Showpage(request):
    #return render(request,"app/show.html")
    all_data=Student.objects.all()
    return render(request,"app/show.html",{'key1':all_data})

#Edit page view
def EditPage(request,pk):
    #Fetching the data of particular id
    get_data=Student.objects.get(id=pk)
    return render(request,"app/edit.html",{'key2':get_data})

#update data view
def UpdateData(request,pk):
    udata=Student.objects.get(id=pk)
    udata.Firstname = request.POST['fname']
    udata.Lastname = request.POST['lname']
    udata.Email = request.POST['email']
    udata.Contact = request.POST['contact']

    #query for update
    udata.save()

    #render to show page
    return redirect('Showpage')

def DeleteData(request,pk):
    ddata=Student.objects.get(id=pk)
    ddata.delete()
    return redirect('Showpage')
'''
def IndexPage(request):
    return render(request,"app/index.html")

def UploadImage(request):
    if request.method=="POST":
        imagename=request.POST['imgname']
        pics=request.FILES['image']

        newimg=ImageData.objects.create(Imagename=imagename,Image=pics)
        return redirect('show')
def ImageFetch(request):
    all_img=ImageData.objects.all()
    return render(request,"app/show.html",{'key1':all_img})

