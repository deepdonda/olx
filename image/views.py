from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import *
from django.db.models import Subquery
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.db.models import Q


# Create your views here.
def  hotel_image_view(request):
    if 'cid' in request.session:
        if request.method == 'POST':
            form=imageform(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('success')
            else:
                form=imageform()
                return render (request,'images.html',{'form' : form})
        else:
            cid=request.session['cid']
            "your cid is:"+str(cid)
            messages.info(request, "your cid is:"+str(cid))
            return render(request,'images.html')
    else:
        messages.info(request, 'you need to login')
        return redirect('login')

def success(request):
    return HttpResponse('successfully uploades')
def myproduct(request):
    if "cid" not in request.session:
        messages.info(request, 'you need to login')
        return redirect('login')
    else:
        info=image.objects.all()
        return render(request,'showproduct.html',{'info' : info})

def removemyproduct(request):
    id=request.GET['submit']
    #image.replace('/media/','/')
    if 'cid' in request.session:
        info=image.objects.get(id=id )
        info.delete()
        return redirect('myproduct')
    else:
        messages.info(request, 'you need to login')
        return redirect('login')

    
def city(request):
    city=request.session['city']
    category=request.session['category']
   # ingo=image.objects.get(city=city and category=category)
    return render(request,'serch.html',{'info':info})
def setsession(request,category,city):
    if '{}'.format(city) == 'Any':
        request.session['category']='{}'.format(category)
    if '{}'.format(category) == 'Any':
        request.session['city']='{}'.format(city)
    #info=image.objects.all()
    #return render(request,'serch.html',{'info' : info})
    if request.session['city'] =='Any' and  request.session['category']=='Any':
        info=image.objects.all()
        return render(request,'serch.html',{'info':info})
    if request.session['city']=='Any' and request.session['category'] != 'Any':
        info=image.objects.filter(category = request.session['category'])
        return render(request,'serch.html',{'info':info})
    if request.session['city']!='Any' and request.session['category'] == 'Any':
        info=image.objects.filter(city = request.session['city'])
        return render(request,'serch.html',{'info':info})
    if request.session['city']!='Any' and request.session['category'] != 'Any':
        info=image.objects.filter(city=request.session['city'],category=request.session['category'])
        return render(request,'serch.html',{'info':info})
def setsession1(request,category):
    if '0' in '{}'.format(category):
        request.session['category']='Any'
    if '1' in '{}'.format(category):
        request.session['city']='Any'
    if request.session['city'] =='Any' and  request.session['category']=='Any':
        info=image.objects.all()
        return render(request,'serch.html',{'info':info})
    if request.session['city']=='Any' and request.session['category'] != 'Any':
        info=image.objects.filter(category = request.session['category'])
        return render(request,'serch.html',{'info':info})
    if request.session['city']!='Any' and request.session['category'] == 'Any':
        info=image.objects.filter(city = request.session['city'])
        return render(request,'serch.html',{'info':info})
    if request.session['city']!='Any' and request.session['category'] != 'Any':
        info=image.objects.filter(city=request.session['city'],category=request.session['category'])
        return render(request,'serch.html',{'info':info})
def productditail(request,id):
    id='{}'.format(id)
    info=image.objects.get(id=id)
    return render(request,'addtocart.html',{'info':info})
def addtocart(request):
    if 'cid' in request.session:
        id=request.POST['addtocart']
        cid=request.session['cid']
        t=cart(id=id,cid=cid)
        t.save()
        return HttpResponse('product added to cart')
    else:
        messages.info(request, 'you need to login')
        return redirect('login')


def mycart(request):
    if 'cid' in request.session:
        cid=request.session['cid']
        info=cart.objects.filter(cid=cid)
        products=image.objects.filter(id=Subquery(info.values('id')))
        return render(request,'mycart.html',{'products':products})
    else:
        messages.info(request, 'you need to login')
        return redirect('login')

def removeformcart(request):
    if 'cid' in request.session:
        id=request.POST['remove from cart']
        cid=request.session['cid']
        c=cart.objects.get(id=id,cid=cid)
        c.delete()
        return redirect('mycart')
    else:
        messages.info(request, 'you need to login')
        return redirect('login')
    
def myprofile(request):
    if 'cid' in request.session:
        id=request.session['cid']
        
        info=User.objects.filter(id=id)
        #request.session["mobile"]=User.objects.filter(id=id).values('username')
        return render(request,'myprofile.html',{'info':info})
    else:
        messages.info(request, 'you need to login')
        return redirect('login')
def updateprofileform(request):
    return render(request, 'updateprofile.html')
def updateprofile(request):
    id=request.session['cid']
    user = User.objects.get(id=id)
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
       
        email = request.POST['email']

        
        if User.objects.filter(username=username ).filter(~Q(id=id)).exists() :
            messages.info(request, 'User already exists!!')
            return redirect('myprofile')
        elif User.objects.filter(email=email).filter(~Q(id=id)).exists():
            messages.info(request, 'Email already linked with other account')
            return redirect('myprofile')
        else:
            user.first_name = first_name
            user.save(update_fields=['first_name'])
            user.last_name = last_name
            user.save(update_fields=['last_name'])
            user.username = username
            user.save(update_fields=['username'])
            user.email = email
            user.save(update_fields=['email'])
            user.save()
            

        
        messages.info(request, 'You have successfully update profile!!')
        return redirect( 'myprofile')
    else:
        return render(request, 'updateprofile.html')

