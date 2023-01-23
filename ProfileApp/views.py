from django.shortcuts import render

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
