from django.urls import path
from .views import home, medicineDetail,addMedicine,availableMedicine
from .views import allMedicines,deleteMedicine,userLogin,userLogOut,search

urlpatterns = [

     path('', userLogin, name='login'),
    path('login/', userLogin, name='login'),
    path('logout/', userLogOut, name='logout'),
    path('home/', home, name='home'),
    #medicine 
    path('medicines/details/<int:id>/', medicineDetail, name='medicinedetails'),
    #path('medicines/', medicine, name='medicine'),
    path('medicines/available', availableMedicine, name='availablemedicine'),
    path('medicines/all', allMedicines, name='allmedicines'),
    path('medicines/addMedicine', addMedicine, name='addmedicine'),
    path('medicines/deletemedicine/<int:id>/', deleteMedicine, name='deletemedicine'),
    #search
    path('search/', search, name='search'),
]
