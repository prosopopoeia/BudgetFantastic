from django import forms

class NameForm(forms.Form):
    users_name = forms.CharField(label='Enter Name', max_length=100)
    
    
class AddCatForm(forms.Form):
    category_name = forms.CharField(max_length=100, label="Add New Category")
    
class NewEntryForm(forms.Form):
    entry_amt = forms.CharField(max_length=100, label="Add Amount")
    notes = forms.CharField(max_length=100, label="transaction notes")
    