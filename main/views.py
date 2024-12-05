from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def Index(request):
    context={
        "kirish":Kirish.objects.all(),
        "kirish1":Kirish1.objects.first(),
        "catigory":Catigory.objects.first(),
        "product":Product.objects.all(),
        "f_p":Featured_Product.objects.first(),
        "f_t":Featured_Product1.objects.all(),
    }
    return render(request,'index.html',context)

def About_as(request):
    context={
        "k":About_kirish.objects.first(),
    }
    return render(request,'about.html',context)

def Shop(request):
    context={
        "k":Shop_kirish.objects.first(),
        "sh_k":Shop_kiyimlar.objects.all(),
    }
    return render(request,'shop.html',context)

def Contact(request):
    context={
        "c_k":Contact_kirish.objects.first(),
    }
    return render(request,'contact.html',context)

def Send(request):
    if request.method =="POST":
        ismiz =request.POST['ismiz']
        gmail_ismi =request.POST['gmail_ismi']
        ishi =request.POST['ishi']
        xabar =request.POST['xabar']
        Sms.objects.create(ismiz=ismiz,gmail_ismi=gmail_ismi,ishi=ishi,xabar=xabar)

        return redirect('/')