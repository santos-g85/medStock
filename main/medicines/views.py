from django.shortcuts import render,redirect, get_object_or_404
from dashboard.models import Medicine,Supplier
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from .forms import MedicineForm  
from django.http import HttpResponseNotFound


pagination_num:int=5
# Create your views here.

@login_required
def medicine(request):
    #set up pagination
    pages = Paginator(Medicine.objects.all().order_by('quantity_in_stock'),pagination_num)  #5 num of item in a page
    page_num = request.GET.get('page')
    medicines = pages.get_page(page_num)
    return render(request,'medicine.html',
                  {"medicines":medicines})

@login_required
def medicineSearch(request):
    query = request.GET.get('q', '')
    page = request.GET.get(1)

    if query:
        items = Medicine.objects.filter(
            Q(name__istartswith=query)
        )
    else:
        items = Medicine.objects.all()

    paginator = Paginator(items, pagination_num)  
    page_obj = paginator.get_page(page)

    context = {
        "medicines": page_obj,
    }

    if query and not items.exists():
        context["message"] = "No items found!"

    return render(request, 'medicine.html', context)

@login_required
def stock(request):
    available_medicine = [x for x in Medicine.objects.all() if x.quantity_in_stock>0]
    pages = Paginator(available_medicine,pagination_num) 
    page_num = request.GET.get('page')
    stock = pages.get_page(page_num) 
    return render(request,'stock.html',{"stock":stock})

@login_required
def stockSearch(request):
    query = request.GET.get('q', '')
    page = request.GET.get('page', 1)

    if query:
        items = Medicine.objects.filter(
            Q(name__istartswith=query),
            quantity_in_stock__gt=0
        )
    else:
        items = Medicine.objects.filter(quantity_in_stock__gt=0)

    paginator = Paginator(items, pagination_num)  
    page_obj = paginator.get_page(page)

    context = {
        "stock": page_obj,
    }

    if query and not items.exists():
        context["message"] = "No items found!"

    return render(request, 'stock.html', context)


@login_required
def addMedicine(request):
    suppliers_list = Supplier.objects.all()

    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            brand = form.cleaned_data["brand"]
            price = form.cleaned_data["price"]
            quantity_in_stock = form.cleaned_data["quantity_in_stock"]
            supplier = form.cleaned_data["suppliers"]

            if Medicine.objects.filter(name=name).exists():
                messages.error(request, "Medicine already exists!")
            else:
                Medicine.objects.create(
                    name=name,
                    brand=brand,
                    price=price,
                    quantity_in_stock=quantity_in_stock,
                    suppliers=supplier
                )
                messages.success(request, "Medicine added successfully!")
                return redirect('medicine')  
    else:
        form = MedicineForm()

    return render(request, 'addmedicine.html', {'form': form, 'suppliers': suppliers_list})
   

@login_required
def deleteMedicine(request, id):
    try:
        medicine = get_object_or_404(Medicine, pk=id)
        medicine.delete()
        messages.success(request, "Medicine deleted successfully.")
    except Exception as e:
        messages.error(request, "An error occurred while deleting medicine.")

    return redirect('medicine')



# def deleteStock(request, id):
#     try:
#         medicine = get_object_or_404(Medicine, pk=id)
#         medicine.delete()
#         messages.success(request, "Stock deleted successfully.")
#     except Exception as e:
#         messages.error(request, "An error occurred while deleting Stock.")

#     return render('deletemedicine.html',{'name':10})


@login_required
def deleteStock(request, id):
    try:
        medicine = Medicine.objects.get(pk=id)
    except Medicine.DoesNotExist:
        return HttpResponseNotFound("Medicine not found.")

    if request.method == 'POST':
        medicine.delete()
        messages.success(request, "Stock deleted successfully.")
        return redirect('stock')

    return render(request, 'deletemedicine.html', {'medicine': medicine})

@login_required
def editMedicine(request, id):
    medicine = get_object_or_404(Medicine, pk=id)

    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('stock')  
    else:
        form = MedicineForm(instance=medicine)

    return render(request, 'editmedicine.html', {'form': form, 'medicine': medicine})