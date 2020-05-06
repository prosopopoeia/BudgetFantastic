from django.db import models
#from datetime import datetime   #I don't think this is needed
from django.utils import timezone
    
class User(models.Model):
    user_name = models.CharField(max_length=200)
    
class Overall(models.Model):
    grandTotal = models.DecimalField(default=0, max_digits=11, decimal_places=2)
    montlyTotal = models.DecimalField(default=0, max_digits=11, decimal_places=2)
    owningUser = models.ForeignKey(User, default=1, on_delete=models.CASCADE)    
    
class Category(models.Model):
    owningUser = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=200)
    overall_total = models.DecimalField(default=0, max_digits=11, decimal_places=2)
    monthly_total = models.DecimalField(default=0, max_digits=11, decimal_places=2)
    last_month_total = models.DecimalField(default=0, max_digits=11, decimal_places=2)
    total_entries = models.IntegerField(default=0)
    
    def __str__(self):
        return self.category_name
    
#a single entry within a category    
class Entry(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    entry_note=models.CharField(default='',max_length=11)
    amount = models.DecimalField(default=0, max_digits=11, decimal_places=2)
    transaction_date=models.DateTimeField('transaction date',default=timezone.now, blank=True)
    
    def is_current_month(self):
        this_moment = timezone.now().month
        return this_moment ==  transaction_date.month
    
    def __str__(self):
        return self.entry_note
        
    
