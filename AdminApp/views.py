from django.shortcuts import render,redirect
from . models import admin_log
from userapp.models import reg_tbl,feed_tbl,Pay_tbl
from ShopOwner.models import newstock

# Create your views here.
def adminlog(request):
    if request.method=='POST':
        eml = request.POST.get('eml')
        psw = request.POST.get('psw')
        obj = admin_log.objects.filter(email=eml,psw=psw)
        if obj:
            request.session['ema']=eml
            request.session['psa']=psw
            return render(request,"adminhome.html")
        else:
            request.session['ema']=''
            request.session['psa']=''
            return render(request,"adminlog.html")
    else:
        return render(request,"adminlog.html")
def adminhome(request):
    return render(request,"adminhome.html")
def userview(request):
    obj=reg_tbl.objects.all()
    return render(request,"details.html",{"data":obj})
def edit(request):
    idno=request.GET.get('idn')
    obj = reg_tbl.objects.filter(id=idno)
    return render(request,"details2.html",{"data":obj})
def update(request):
    if request.method=='POST':
        idl=request.POST.get('idl')
        fn=request.POST.get('fn')
        mb=request.POST.get('mb')
        em=request.POST.get('em')
        ps1=request.POST.get('ps1')
        ps2=request.POST.get('ps2')
        obj = reg_tbl.objects.get(id=idl)
        obj.fnm=fn
        obj.mob=mb
        obj.eml=em
        obj.psw1=ps1
        obj.psw2=ps2
        obj.save()
        return redirect("/AdminApp/userview")
    return render(request,"userdetail2.html")
def delete(request):
    idno=request.GET.get('idn')
    obj = reg_tbl.objects.filter(id=idno)
    obj.delete()
    return redirect("/AdminApp/userview")
def bookings(request):
    obj=Pay_tbl.objects.all()
    return render(request,"bookings.html",{"data":obj})
def confirmbook(request):
    idn = request.GET.get('idn')
    obj = Pay_tbl.objects.filter(id=idn)
    return render(request,"confirm.html",{"success":obj})
   

def cancelbook(request):
    idn = request.GET.get('idn')
    obj = Pay_tbl.objects.filter(id=idn)
    obj.delete()
    return redirect("/AdminApp/bookings")


def newstockview(request):
    obj = newstock.objects.all()
    return render(request,"adminnewstock.html",{"card":obj})

def feedview(request):
    obj = feed_tbl.objects.all()
    return render(request,"feedview.html",{"data":obj})


