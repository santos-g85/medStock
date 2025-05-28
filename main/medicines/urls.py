from django.urls import path
from .views import medicine, medicineSearch,stock, stockSearch,deleteMedicine,deleteStock,editMedicine
from .views import addMedicine
urlpatterns = [

    #medicine 
    path('', medicine, name='medicine'),
    #search
    path('search/', medicineSearch, name='medicinesearch'),
    path('stock/', stock, name='stock'),
    path('stock/search/', stockSearch, name='stocksearch'),
    path('addMedicine/',  addMedicine, name='addMedicine'),
    path('deletemedicine/<int:id>',  deleteMedicine, name='deleteMedicine'),
    path('deleteStock/<int:id>',  deleteStock, name='deleteStock'),
    path('editMedicine/<int:id>',  editMedicine, name='editMedicine'),
]
