from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest,JsonResponse
from .models import Medicine,Supplier
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.db.models import Q

@login_required
def home(request:HttpRequest)->HttpResponse:
    return render(request, "home.html") 


def userLogin(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':  
        username = request.POST.get('username')  
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  
            messages.success(request, "Login successful") 
            return redirect('home')  

        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')

def userLogOut(request:HttpRequest)->HttpResponse:
    logout(request)
    messages.success(request,"user logged out successfully")  
    return redirect('login')

def search(request:HttpRequest)->JsonResponse:
    query = request.GET.get('q', '')

    if query:
        medicines = Medicine.objects.filter(
            Q(name__icontains=query) |
            Q(supplier__icontains=query) |
            Q(brand__icontains=query)
        )
        results = [{"id": medicine.id, "name": medicine.name} for medicine in medicines]
        return JsonResponse({"results": results})
    else:
        return JsonResponse({"results": []})



"""def medicine(request: HttpRequest) -> HttpResponse:
    all_medicines = Medicine.objects.all()
    available_medicines = [x for x in all_medicines if x.quantity_in_stock > 0]

    context = {
        "all_medicines": all_medicines,
        "available_medicines": available_medicines,
    }
    return render(request, "medicine.html", context)
"""

 
def allMedicines(request: HttpRequest) -> HttpResponse:
    medicines = Medicine.objects.all()
    context = {"medicines": medicines}
    return render(request, "allmedicine.html", context)


def availableMedicine(request: HttpRequest) -> HttpResponse:
    medicines = [x for x in Medicine.objects.all() if x.quantity_in_stock > 0]
    context = {"medicines": medicines}
    return render(request, "medicinelist.html", context)

def medicineDetail(request: HttpRequest, id: int) -> HttpResponse:
    try:
        medicine = Medicine.objects.get(id=id)
        if(medicine):
            context = {
                "medicine": medicine,
            }
    except Medicine.DoesNotExist:
        return HttpResponse("Medicine not found")
    return render(request, "medicinedetails.html", context)

def addMedicine(request:HttpRequest) -> HttpResponse:
    suppliercontext = {"suppliers": Supplier.objects.all()}
    if request.method == "POST":
        name = request.POST.get("name")
        brand = request.POST.get("brand")
        description = request.POST.get("description")
        supplier = request.POST.get("supplier")
        supplier= Supplier.objects.filter(id=supplier).first()
        medicine = Medicine(name=name, 
                            brand=brand,
                            description=description,  
                            supplier=supplier)
        medicine.save()
        messages.success(request, 'Medicine has been successfully added!')
    return render(request, "addmedicine.html",suppliercontext)


def deleteMedicine(request:HttpRequest, id:int)->None:
    try:
        medicine =Medicine.objects.get(id=id)
        if medicine:
            medicine.delete()
            messages.success(request, f'Medicine {medicine.name} has been successfully deleted!')
            return redirect('allmedicines') 
    except Medicine.DoesNotExist:
           messages.error(request, 'Medicine does not exists')
           return redirect('allmedicines')



"""def add_Medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medicine has been successfully added!')
            return redirect('addmedicine')  # Redirect to the same page or another page
    else:
        form = MedicineForm()

    return render(request, 'add_medicine.html', {'form': form})

"""