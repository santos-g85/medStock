from django.shortcuts import render
from dashboard.models import Medicine
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

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