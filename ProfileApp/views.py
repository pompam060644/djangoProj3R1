from django.shortcuts import render, redirect
import datetime
from ProfileApp.form import *
# Create your views here.
def home(request):
    return render(request,'home.html')
def myinfo(request):
    return render(request, 'myinfo.html')
def education(request):
    return render(request, 'education.html')
def interest(request):
    return render(request, 'interest.html')
def sales(request):
    return render(request, 'sales.html')
def rloemodel(request):
    return render(request, 'rloe.html')
def etc(request):
    return render(request, 'etc.html')
def mydata(request):
    name = "นางสาวพัชราพร ดวงจิตร"
    stdid = "65342310015-1"
    address = "329 ม.11 บ้านนาจาน ต.หนองแปน อ.มัญจาคีรี จ.ขอนแก่น 40160"
    gender = "หญิง"
    weigth = "48"
    heigth = "168"
    colors = "สีชมพู"
    food = "อาหารประเภทเส้น"
    job = "นักศึกษา"
    myproduct = [["รองเท้า adidas", "1,499", "images/141.jpg"],
                 ["รองเท้า nike", "1,599", "images/142.jpg"],
                 ["รองเท้า converse", "1,299", "images/143.jpg"],
                 ["รองเท้า Keds", "1,099", "images/144.jpg"],
                 ["รองเท้า New balance", "1,399", "images/145.jpg"],
                 ["รองเท้า Onitsuka Tiger", "1,199", "images/146.jpg"],
                 ["รองเท้า Reebok", "1,099", "images/147.jpg"],
                 ["รองเท้า Lacoste", "1,399", "images/148.jpg"],
                 ]
    return render(request, 'showmydata.html', {'name':name, 'stdid':stdid, 'address':address, 'gender':gender,
                                          'weigth':weigth, 'heigth':heigth, 'colors':colors, 'food':food,
                                          'job':job, 'myproduct':myproduct})

lstOurProduct = []
# pd1 = product("P01", "รองเท้า adidas", "White", "36", 1499, 1, True)
# lstOurProduct.append(pd1)
def listProduct(request):
    details = "รองเท้า"
    name = "นางสาวพัชราพร ดวงจิตร"
    date = datetime.datetime.now()
    return render(request, 'listProduct.html', {'lstProduct': lstOurProduct,
                                              'details': details, 'name': name,
                                              'date': date.strftime("%A %d-%m-%Y %H : %M")})
def inputProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            pid = form.cleaned_data['pid']
            pname = form.cleaned_data['pname']
            color = form.cleaned_data['colors']
            size = form.cleaned_data['size']
            price = form.cleaned_data['price']
            am = form.cleaned_data['amount']
            promotion = form.cleaned_data['promotion']
            productnew = product(pid, pname, color, size, price, am, promotion)
            lstOurProduct.append(productnew)
            return redirect('listProduct')
        else:
            return redirect('pro_retrive_all')
    else:
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'inputProduct.html', context)
def showGoodsList (request):
    #Query
    result = Goods.objects.all()
    return render(request, 'showGoodsList.html', {'result' : result})

def showGoodsOne (request,gid):
    context ={}
    goodsone_info = Goods.objects.get(gid=gid)
    #result ={'goodsone_info':goodsone_info}
    form = GoodsForm(request.POST or None, instance=goodsone_info)
    context["form"] = form
    return render(request, 'showGoodsOne.html', context)



def newGoodsCreate (request):
    context = {}
    if request.method == 'POST':
        form = GoodsForm(request.POST)
        obj = Goods.objects.filter(gid=request.POST['gid'])
        if obj:
            context["form"] = form
            return render(request, "newGoodsCreate.html", context)
        if form.is_valid():
            form.save()
            return redirect('goodslist')
        else:
            return redirect('pro_retrive_all')
    else:
        form = GoodsForm()
    context = {
        'form': form
    }
    return render(request, 'newGoodsCreate.html', context)
def GoodsUpdate (request,gid):
    context = {}
    obj = Goods.objects.get(gid=gid)
    form = GoodsFormUpdate(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('goodslist')
    else:
        context["form"] = form
        return render(request, "GoodsUpdate.html", context)

def GoodsDel (request,gid):
    goods = Goods.objects.get(gid=gid)
    if request.method =="GET":
        goods.delete()
        return redirect('goodslist')
    # value = {'value': goods}
    # return render(request, 'form/Goodsdel.html', value)

def showCustomerList (request):
    result = Customer.objects.all()
    return render(request, 'showCustomerList.html', {'result': result})

def register (request):
    context = {}
    if request.method == 'POST':
        form = CusForm(request.POST)
        obj = Customer.objects.filter(cid=request.POST['cid'])
        if obj:
            context["form"] = form
            return render(request, "newGoodsCreate.html", context)
        if form.is_valid():
            form.save()
            return redirect('customerList')
        else:
            return redirect('pro_retrive_all')
    else:
        form = CusForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def CustomerUpdate (request,cid):
    context = {}
    obj = Customer.objects.get(cid=cid)
    form = CusFormUpdate(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('customerList')
    else:
        context["form"] = form
        return render(request, "CustomerUpdate.html", context)

def CustomerDel (request,cid):
    Cus = Customer.objects.get(cid=cid)
    if request.method == "GET":
        Cus.delete()
        return redirect('customerList')
    # value = {'value':Cus}
    # return render(request,'form/showCustomerList.html',value)

def showCusOne (request,cid):
    context ={}
    Cusone_info = Customer.objects.get(cid=cid)
    #result ={'goodsone_info':goodsone_info}
    form = CusForm(request.POST or None, instance=Cusone_info)
    context["form"] = form
    return render(request, 'showCusOne.html', context)
