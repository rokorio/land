from django.shortcuts import render,redirect
from models import Payments,ParcelDetail,planingApplication,LandCaution


# Create your views here.
def index(request):
    return render(request,'index.html')

def dashboard(request):
    return render(request,"dashboard.html")


def pay_rate(request):
    if request.method =="POST":
        land_name=request.POST['parcel_num']
        result=Payments.objects.filter(reg_no=land_name)
        if result:
            return render(request,'pay_rate.html',{"result":result})
        
        else:
            return render(request,'pay_rate.html',{"land_name":land_name})

def parcel_search(request):
    if request.method =="POST":
        land_name=request.POST['parcel_num']
        result=ParcelDetail.objects.filter(reg_no=land_name)
        if result:
            return render(request,'parcel_search.html',{"result":result})
        
        else:
            return render(request,'parcel_search.html',{"land_name":land_name})

def planing_application(request):
    if request.method == "POST":
        land_name=request.POST['land_name']
        land_name=ParcelDetail.objects.filter(reg_no=land_name)
        planing=request.POST['amount']
        data=planingApplication(land_name=land_name,paid=planing)
        data.save()
        return redirect('dashbord')
    return render(request,'planing_application.html')

def  caution_application(request):
    if request.method =="POST":
        land_name=request.POST['land_name']
        land_name=ParcelDetail.objects.filter(reg_no=land_name)
        applier_name=request.POST['name']
        id_no=request.POST['idno']
        reason=request.POST['reasonon']
        data=LandCaution(land_name=land_name, applier_name=applier_name,id_no=id_no,reason=reason)
        data.save()
        return redirect('dashbord')

    return render(request,"caution_application.html")

def caution_removal(request,land_name):
    name=ParcelDetail.objects.get(land_name)
    name.delete()
    return redirect("dashboard")
    
    pass


def parcel_transfer(request,land_name):
    pass