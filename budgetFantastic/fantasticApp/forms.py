from django import forms

class NameForm(forms.Form):
    item_text = forms.CharField(label='Enter information', max_length=100)
    
    
class AddCatForm(forms.Form):
    category = forms.CharField(max_length=100)
   

    
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_self = forms.BooleanField(required=False)
    
    