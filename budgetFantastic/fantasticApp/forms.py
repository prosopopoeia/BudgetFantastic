from django import forms
from django.forms import DecimalField

class NameForm(forms.Form):
    users_name = forms.CharField(label='Enter Name', max_length=100)
    
    
class AddCatForm(forms.Form):
    category_name = forms.CharField(max_length=100, label="Add New Category")
    category_amount =  forms.DecimalField(max_digits=11, decimal_places=2, label="Add Amount")
    category_notes = forms.CharField(max_length=100, label="transaction notes")
    
class NewEntryForm(forms.Form):
    entry_amt = forms.DecimalField(max_digits=11, decimal_places=2, label="Add Amount")
    notes = forms.CharField(max_length=100, label="transaction notes")
    
    