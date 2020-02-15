from django.shortcuts import render
from django.http import HttpResponse
from loadplan.models import Ord,Avc,Cpr
# Create your views here.

def loadplan(request):
    return render(request,'hello.html')

def orderdetails(request):
    if request.method == 'POST':
        orderno=request.POST['orderno']
        styleno=request.POST['styleno']
        orderqty=request.POST['orderqty']
        ordercd=request.POST['ordercd']
        plancd = request.POST['plancd']
        ocd=request.POST['ocd']
        ltf=request.POST['ltf']
        ltb=request.POST['ltb']
        s=Ord(orderno=orderno, styleno=styleno, orderqty=orderqty, ordercd=ordercd, plancd=plancd, ocd=ocd, ltf=ltf, ltb=ltb)
        s.save()
        return render(request,'orderdetails.html')
    return render(request, 'orderdetails.html')

def availablecapacity(request):
    if request.method == 'POST':
        lineno=request.POST['lineno']
        noo=request.POST['noo']
        workdays=request.POST['workdays']
        dwh=request.POST['dwh']
        absent = request.POST['absent']
        efficiency=request.POST['efficiency']
        mac=request.POST['mac']
        s1=Avc(lineno=lineno, noo=noo, workdays=workdays, dwh=dwh, absent=absent, efficiency=efficiency, mac=mac)
        s1.save()
        return render(request,'availablecapacity.html')
    return render(request, 'availablecapacity.html')

def capreqd(request):
    if request.method == 'POST':
        orderno=request.POST['orderno']
        ltlc=request.POST['ltlc']
        orderqty=request.POST['orderqty']
        smv=request.POST['smv']
        crm = request.POST['crm']
        capd=request.POST['capd']
        crd=request.POST['crd']
        s2=Cpr(orderno=orderno, ltlc=ltlc, orderqty=orderqty, smv=smv, crm=crm, capd=capd, crd=crd)
        s2.save()
        return render(request,'capreqd.html')
    macfill = Avc.objects.all()
    return render(request,'capreqd.html',{'macfill': macfill})

def ordtable(request):
    allorder = Ord.objects.all()
    return render(request,'ordtable.html', {'allorder': allorder})

def avctable(request):
    allavc = Avc.objects.all()
    return render(request,'avctable.html', {'allavc': allavc})

def cprtable(request):
    allcpr = Cpr.objects.all()
    return render(request,'cprtable.html', {'allcpr': allcpr})

