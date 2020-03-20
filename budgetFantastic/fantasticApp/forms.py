from django import forms

class NameForm(forms.Form):
    users_name = forms.CharField(label='Enter Name', max_length=100)
    
    
class AddCatForm(forms.Form):
    category_name = forms.CharField(max_length=100, label="Add New Category")
   
class NewEntryForm(forms.Form):
    entry_amount = forms.CharField(max_length=100, label="Add Amount") 
    notes = forms.CharField(max_length=100, label="transaction note")
    
    
   

   
# class ContactForm(forms.Form):
    # subject = forms.CharField(max_length=100)
    # message = forms.CharField(widget=forms.Textarea)
    # sender = forms.EmailField()
    # cc_self = forms.BooleanField(required=False)
    
    