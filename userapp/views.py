from django.shortcuts import render,redirect
from . models import reg_tbl,Cart_tbl,Pay_tbl,feed_tbl
from ShopOwner.models import newstock
from django.contrib import messages
from datetime import date,timedelta

# Create your views here.
def index(request):
    return render(request,"index.html")
def reg(request):
    if request.method=='POST':
        fname  = request.POST.get('fn')
        mobile = request.POST.get('mb')
        email = request.POST.get('em')
        psw1 = request.POST.get('ps')
        psw2 = request.POST.get('cps')
        obj = reg_tbl.objects.create(fnm=fname,mob=mobile,eml=email,psw1=psw1,psw2=psw2)
        obj.save()
        if obj:
            return render(request,"login.html")
        else:
            return render(request,"reg.html")
    else:
        return render(request,"reg.html")
def log(request):
    if request.method=='POST':
        email = request.POST.get('em')
        psw1 = request.POST.get('ps')
        obj = reg_tbl.objects.filter(eml=email,psw1=psw1)
        if obj:
            for ls in obj:
                idno=ls.id
            request.session['eml']=email
            request.session['psw']=psw1
            request.session['idl']=idno
            obb=reg_tbl.objects.filter(id=idno)
            return render(request,"home.html",{"user":obb})
        else:
            msg="Invalid Email Id & Password"
            request.session['eml']=''
            request.session['psw']=''
            return render(request,"login.html",{"error":msg})
    else:
        return render(request,"login.html")

def home(request):
    return render(request,"home.html")

def newstockview(request):
    obj = newstock.objects.all()
    return render(request,"newstockview.html",{"card":obj})

def personal(request):
    obj = newstock.objects.filter(cat='personal essentials')
    return render(request,"personal.html",{"data":obj})

def dissearch(request):
    dis = request.POST.get('dis')
    dis=str(dis)
    dis=dis.lower()
    obb = newstock.objects.filter(dis=dis)
    return render(request,"dissearch.html",{"new":obb})
    
def medsearch(request):
    med = request.POST.get('med')
    med=str(med)
    med=med.lower()
    obb = newstock.objects.filter(mnm=med)
    return render(request,"medsearch.html",{"new":obb})

def addtocart(request):
    number = request.GET.get('idn')
    userid = request.session.get('idl')
    uobj = reg_tbl.objects.get(id=userid)
    pobj = newstock.objects.get(id=number)
    cartitem,created = Cart_tbl.objects.get_or_create(customer=uobj,product=pobj)
    if not created:
        cartitem.qty+=1
        cartitem.save()
        messages.success(request,"Item added to cart")
    return redirect('/newstockview')

def viewcart(request):
    cid = request.session.get('idl')
    cusobj = reg_tbl.objects.get(id=cid)
    cartobj = Cart_tbl.objects.filter(customer=cusobj)
    if cartobj:
        total_price = 0
        for i in cartobj:
            pro=i.product.mpr*i.qty
            total_price=total_price+pro
           
        return render(request,"cart.html",{'cartitems':cartobj,'total_price':int(total_price)})
    else:
        return render(request,"cart.html",{"info":"Your Cart is Empty"})
def cartdelete(request):
    number = request.GET.get('idn')
    obj = Cart_tbl.objects.filter(id=number)
    obj.delete()
    return redirect('/newstockview')

def paydirect(request):
    cid = request.session.get('idl')
    cusobj = reg_tbl.objects.get(id=cid)
    obb = reg_tbl.objects.filter(id=cid)
    for ls in obb:
        fnm = ls.fnm
    cartobj = Cart_tbl.objects.filter(customer=cusobj)
    if cartobj:
        total_price = 0
        for i in cartobj:
            pro=i.product.mpr*i.qty
            total_price=total_price+pro
           
        return render(request,"pay.html",{'cartitems':cartobj,'total_price':int(total_price),"user":fnm})
    return render(request,"cart.html")


def pay(request):
    current_date = date.today()
    future_date = current_date + timedelta(days=9)
    idno =  request.session['idl']
    obj = reg_tbl.objects.filter(id=idno)
    for ls in obj:
        fname = ls.fnm
    if request.method=='POST':
        pro = request.POST.get('pro')
        qty = request.POST.get('qty')
        prc = request.POST.get('prc')
        tot = request.POST.get('tot')
        fn = request.POST.get('fn')
        cd = request.POST.get('cd')
        ex = request.POST.get('ex')
        cvv = request.POST.get('cvv')
        obb = Pay_tbl.objects.create(pro=pro,qty=qty,prc=prc,tot=tot,fn=fn,cd=cd,ex=ex,cvv=cvv)
        obb.save()
        if obb:
            msg = "Payment Successfull..."
            return render(request,"success.html",{"success":msg,"ret":fname,"current_date": current_date,"future_date": future_date})
    return render(request,"pay.html")

def feedback(request):
    if request.method=='POST':
        fnm = request.POST.get('fnm')
        eml = request.POST.get('eml')
        feed = request.POST.get('feed')
        obj = feed_tbl.objects.create(fnm=fnm,eml=eml,feed=feed)
        obj.save()
        if obj:
            msg="Feedback Entered Successfully"
            return render(request,"feed.html",{"success":msg})
        else:
            return render(request,"feed.html")
    else:
        return render(request,"feed.html")

def userbill(request):
    idno = request.session['idl']
    cus = reg_tbl.objects.filter(id=idno)
    for ls in cus:
        fnm = ls.fnm
    obb = Pay_tbl.objects.filter(fn=fnm)
    return render(request,"bill.html",{"bill":obb})


