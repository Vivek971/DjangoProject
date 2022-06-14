from django.shortcuts import render ,HttpResponse
from home.models import Contact
from django.contrib.messages import constants as messages

# Create your views here.
def index(request):
    context={
        "variable1":"HARRY IS GREAT ",
             "variable2":"LOREM IS GREAT "
             }
    return render(request, "index.html", context)
   # return HttpResponse("This is homepage")

def about(request):
    return render(request, "about.html")
    #return HttpResponse("This is about us")    

def services(request):
    return render(request, "services.html")
   # return HttpResponse("This is services")  
    
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phoneno = request.POST.get('phoneno')
        city = request.POST.get('city')
        pin = request.POST.get('pin')
        c1 = Contact(name=name,address=address, phoneno=phoneno, city=city,pin=pin)
        c1.save() 
    return render(request,'contacts.html')
   # return HttpResponse("This is contacts")          