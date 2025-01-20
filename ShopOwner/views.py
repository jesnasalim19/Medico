from django.shortcuts import render
from ShopOwner.models import shop_log,newstock
# Create your views here.
def shoplog(request):
    if request.method=='POST':
        email = request.POST.get('em')
        psw1 = request.POST.get('ps')
        obj = shop_log.objects.filter(email=email,pasw=psw1)
        if obj:
            for ls in obj:
                idno=ls.id
            request.session['eml']=email
            request.session['psw']=psw1
            request.session['idl']=idno
            obb=shop_log.objects.filter(id=idno)
            return render(request,"shophome.html",{"user":obb})
        else:
            msg="Invalid Email Id & Password"
            request.session['eml']=''
            request.session['psw']=''
            return render(request,"shoplog.html",{"error":msg})
    else:
        return render(request,"shoplog.html")

       
def shophome(request):
    return render(request,"shophome.html")

def mednewreg(request):
    if request.method=='POST':
        mnm = request.POST.get('mn')
        mnm = str(mnm)
        mnm=mnm.lower()
        mim = request.FILES.get('mi')
        mpr = request.POST.get('pr')
        des = request.POST.get('des')
        dis = request.POST.get('dis')
        dis = str(dis)
        dis = dis.lower()
        cat = request.POST.get('cat')
        cat = str(cat)
        cat = cat.lower()
        bran = request.POST.get('bran')
        mfg = request.POST.get('mfg')
        exp = request.POST.get('exp')
        qt = request.POST.get('qt')
        obj = newstock.objects.create(mnm=mnm,mim=mim,mpr=mpr,des=des,dis=dis,cat=cat,bran=bran,mfg=mfg,exp=exp,qt=qt)
        obj.save()
        if obj:
            msg="Details entered Successfully"
            return render(request,"salesbillnew.html",{"success":msg})
        else:
            return render(request,"mednewreg.html")
    else:
        return render(request,"mednewreg.html")
def salesbillnew(request):
    obj = newstock.objects.all()
    return render(request,"salesbillnew.html",{"data":obj})

