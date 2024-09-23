from django.shortcuts import render,redirect
from.models import *
from adminapp.models import *
from django.db.models.aggregates import Sum
# Create your views here.
def regdata(request):
    if request.method=='POST':
        Name=request.POST["Name"]
        email=request.POST["email"]
        Phone=request.POST["Phone"]
        Password=request.POST["password"]
        data=reg(name=Name,email=email,Phone=Phone,Password=Password)
        data.save()
        return redirect('login')
def user1(request):
    data=cat.objects.all()
    return render(request,'user1.html',{'data':data})
def contactdata(request):
    if request.method=='POST':
        Name=request.POST["Name"]
        email=request.POST["email"]
        message=request.POST["message"]
        data1=cont(name=Name,email=email,message=message)
        data1.save()
        return render(request,'contact.html',{'data1':data1})
def contact(request):
    return render(request,'contact.html')
def register(request):
    return render(request,'registration.html')
def login(request):
   data1=reg.objects.all()
   return render(request,'login.html',{'data':data1})
def logdata(request):
    if request.method == "POST":
        Name=request.POST.get('Name')
        password=request.POST.get('password')
        if reg.objects.filter(name=Name,Password=password).exists():
           data = reg.objects.filter(name=Name,Password=password).values('id','Phone','email').first()
           request.session['Name_u'] =Name 
           request.session['id_u'] = data['id']
           request.session['Phone'] = data['Phone'] 
           request.session['email_u'] = data['email'] 
           request.session['password_u'] = password
           return redirect('user1') 
        else:
            return render(request,'login.html',{'msg':'invalid user credentials'})
    else:
        return redirect('registration')
def logout(request):
    del request.session['Name_u']
    del request.session['id_u']
    del request.session['Phone']
    del request.session['email_u']
    del request.session['password_u']
    return redirect('user1')
def catview(request):
    data=cat.objects.all()
    return render(request,'catview.html', {'data':data})
def products(request,category):
    if(category == "all"):
        data=add.objects.all()
    else:
        data=add.objects.filter(PCat=category)
    # data2=add.objects.all()
    return render(request,'product.html', {'data':data})
def productdetail(request,id):
    data=cat.objects.all()
    data2=add.objects.filter(id=id)
    return render(request,'product_detail.html', {'data2':data2, 'data':data})
def checkout1(request):
    c=request.session.get('id_u')
    data3=cartdata.objects.filter(cartuser=c,status=0)
    b=cartdata.objects.filter(cartuser=c,status=0).aggregate(Sum('total'))
    return render(request,'checkout1.html',{'data':data3, 'b':b})
def cart(request):
    return render(request,'cart.html')
def cartdata1(request,id):
    if request.method == 'POST':
        Name_id= request.session.get('id_u')
        quantity=request.POST['quantity']
        total=request.POST['total']
        data3=cartdata(cartuser=reg.objects.get(id=Name_id),cartproduct=add.objects.get(id=id),quantity=quantity,total=total)
        data3.save()
    return redirect('cart')
def cart(request):
    c=request.session.get('id_u')
    data4=cartdata.objects.filter(cartuser=c,status=0)
    return render(request,'cart.html',{'data4':data4})
def cartdelete(request,id):
   data=cartdata.objects.filter(id=id).delete()
   return redirect('cart')
def checkoutdata(request):
    if request.method == 'POST':
        checkoutid= request.session.get('id_u')
        address=request.POST['address']
        city=request.POST['city']
        country=request.POST['country']
        postcode=request.POST['postcode']

        buy=cartdata.objects.filter(cartuser=checkoutid,status=0)

        for i in buy:
          data5=checkout(usercheckout=reg.objects.get(id=checkoutid),checkoutcart=cartdata.objects.get(id=i.id),address=address,city=city,country=country,postcode=postcode)
          data5.save()
          cartdata.objects.filter(id=i.id).update(status=1)
    return redirect('sucess')

def sucess(request):
    c=request.session.get('id_u')
    data4=cartdata.objects.filter(cartuser=c)
    data5=checkout.objects.all()
    return render(request,'sucess.html', {'data':data4,'data':data5})
