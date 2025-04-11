from django.urls import path
from .views import medicine, medicineSearch,stock, stockSearch

urlpatterns = [

    #medicine 
    path('', medicine, name='medicine'),
    #search
    path('search/', medicineSearch, name='medicinesearch'),
    path('stock/', stock, name='stock'),
    path('stock/search/', stockSearch, name='stocksearch'),
]
