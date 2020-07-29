from django.shortcuts import render,HttpResponse,redirect
from .DBM import addEmp,selectAllEmp,Empdelete,selectEmpById,EmpUpdate
def home(request):
    return HttpResponse("<h1>Hello Developer</h1>")

def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'addUser.html')

def empList(request):
    al=selectAllEmp()
    d={"el":al}
    return render(request,'emplist.html',d)

def third(request):
    return HttpResponse("<h1>Hello Sagar</h1>")

def addUser(request):
    id=request.GET.get('id')
    name=request.GET.get('name')
    contact=request.GET.get('contact')
    address=request.GET.get('address')
    t=(id,name,contact,address)
    addEmp(t)
    return redirect('/')


def deleteEmp(request):
    id=request.GET.get("id")
    Empdelete(id)
    return redirect("/empList")

def editEmp(request):
    id=request.GET.get("id")
    emp=selectEmpById(id)
    print("--------------",emp)
    return render(request,'updateEmp.html',{'e':emp})


def updateEmp(request):
    id=request.POST.get('id')
    name=request.POST.get('name')
    contact=request.POST.get('contact')
    address=request.POST.get('address')
    t=(name,contact,address,id)
    EmpUpdate(t)
    return redirect("/empList")

#Hii 
