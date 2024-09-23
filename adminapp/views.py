from django.shortcuts import render,redirect
from.models import *
from userapp.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def catdata(request):
    if request.method=='POST':
        CName=request.POST['CName']
        CImage=request.FILES['CImage']
        data=cat(CName=CName,CImage=CImage)
        data.save()
        return redirect('admin1')
def admin1(request):
    Category=cat.objects.all().count()
    Products=add.objects.all().count()
    Registers=reg.objects.all().count()
    Feedbacks=cont.objects.all().count()
    Checkouts=checkout.objects.all().count()
    return render(request,'admin1.html',{'Category':Category,'Products':Products,'Registers':Registers,'Feedbacks':Feedbacks,'Checkouts':Checkouts})
def category(request):
    return render(request,'category.html')
def table(request):
    data=cat.objects.all()
    return render(request,'table.html',{'data':data})
def edit(request,id):
    data=cat.objects.filter(id=id)
    return render(request,'edit.html',{'data':data})
def update(request,id):
    if request.method=='POST':
        CName=request.POST['CName']
        
        try:
            CImage=request.FILES['CImage']  
            fs = FileSystemStorage()
            file = fs.save(CImage.name, CImage)
        except MultiValueDictKeyError:
            file = cat.objects.get(id=id).CImage
        cat.objects.filter(id=id).update(CName=CName,CImage=CImage)
        return redirect('table')
def delete(request,id):
   data=cat.objects.filter(id=id).delete()
   return redirect('table')
def addproduct(request):
    data5=cat.objects.all()
    return render(request,'addproduct.html',{'data':data5})
def productdata(request):
    if request.method=='POST':
        PName=request.POST['PName']
        PPrice=request.POST['PPrice']
        CName=request.POST['CName']
        PDescription=request.POST['PDescription']
        PImage=request.FILES['PImage']
        data1=add(PName=PName,PPrice=PPrice,PDescription=PDescription,PImage=PImage,PCat=CName)
        data1.save()
        return redirect('admin1')
def producttable(request):
    data1=add.objects.all()
    data5=cat.objects.all()
    return render(request,'producttable.html',{'data1':data1,'data':data5})
def edit1(request,id):
    data1=add.objects.filter(id=id)
    data5=cat.objects.all()
    return render(request,'edit1.html',{'data1':data1,'data':data5})
def update1(request,id):
    if request.method=='POST':
        PName=request.POST['PName']
        PPrice=request.POST['PPrice']
        CName=request.POST['CName']
        PDescription=request.POST['PDescription']
        
        try:
            PImage=request.FILES['PImage']
            fs = FileSystemStorage()
            file = fs.save(PImage.name, PImage)
        except MultiValueDictKeyError:
            file = add.objects.get(id=id).PImage
        add.objects.filter(id=id).update(PName=PName,PPrice=PPrice,PDescription=PDescription,PImage=file,PCat=CName)
        return redirect('producttable')
def delete1(request,id):
   data1=add.objects.filter(id=id).delete()
   return redirect('producttable')
def contacttable(request):
    data2=cont.objects.all()
    return render(request,'contacttable.html',{'data2':data2})
def registertable(request):
    data3=reg.objects.all()
    return render(request,'registertable.html',{'data3':data3})
def checkouttable1(request):
    data4=checkout.objects.all()
    return render(request,'checkouttable1.html',{'data':data4})

    