from django import forms
from dashboard.models import Medicine,Supplier

class MedicineForm(forms.ModelForm):
    
    suppliers = forms.ModelChoiceField(queryset=Supplier.objects.all())

    class Meta:
        model = Medicine
        fields = ['name', 'brand', 'price', 'quantity_in_stock']
