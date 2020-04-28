from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic, View
from django.views.generic.edit import FormView
from fantasticApp.models import User, Category, Overall, Entry
from .forms import NameForm, AddCatForm, NewEntryForm
from fantasticApp.utilFunctions import simpleMath

class indexView(generic.ListView):
    template_name = 'fantasticApp/index.html'
    context_object_name = 'users_name'        
    
    def get(self, request, *args, **kwargs):
        form_one = NameForm()
        return render(request, self.template_name, {'form_one': form_one})
                
class getNameView(generic.DetailView):
    template_name = 'fantasticApp/getname.html'
    existing_user_template =  'fantasticApp/catlist.html'
    
    def post(self, request):
        form_one = AddCatForm()
        #form_two = NewEntryForm()
        namer = request.POST['users_name']
        try:
            user_=User.objects.get(user_name=namer)
            return render(request, self.existing_user_template, {'form_one' : form_one, 'current_user' : user_, 'user_name' : namer }    )
        except User.DoesNotExist:
            user = User.objects.create(user_name = namer)            
        return render(request, self.template_name, {'form_one': form_one, 'user' : user, 'user_name' : namer})      

class catlistView(View):
    template_name = 'fantasticApp/catlist.html'

    def post(self, request, users_name):
        usenam = request.POST['user_name']
        user_  = User.objects.get(user_name=usenam)
        form_one = AddCatForm()       
        return render(request, self.template_name, {'form_one' : form_one, 'current_user' : user_, 'user_name' : users_name })
        
    def get(self, request, users_name):
        user_  = User.objects.get(user_name=users_name)
        return render(request, self.template_name, {'form_one' : form_one, 'current_user' : user_, 'user_name' : users_name })

class listcatView(generic.ListView):
    template_name = 'fantasticApp/catlist.html'
    model = Category    
    
    ##is this get function used? determine this at some point in the TBD.
    def get(self, request):
        use_name = request.GET['user_name']
        user_ = User.objects.get(user_name=use_name)
        return HttpResponse("Hello, this is an existing user name %s" % user.id)
        #return render(request, self.template_name, {'form_one' : form_one, 'current_user' : user_, 'user_name' : use_name })        
        
    def post(self, request, user_name):
        form_one = AddCatForm()
        cat_name = request.POST['category_name']
        user_=User.objects.get(user_name=user_name)
                
        new_category = Category()
        new_category.category_name = cat_name
        new_category.owningUser = user_   
        
        
        current_entry = Entry()
        current_entry.amount = request.POST['category_amount']
        current_entry.entry_note = request.POST['category_notes']
        
        new_category.monthly_total = request.POST['category_amount']
        new_category.save()    
        
        current_entry.cat = new_category
        current_entry.save()

        return render(request, self.template_name, {'form_one' : form_one, 'current_user' : user_, 'user_name' : user_name })        

class catdetailView(generic.DetailView):
    template_name = 'fantasticApp/catdetail.html'
    
    def post(self, request, category_name):
        form_one = NewEntryForm()
        user_string = request.GET['user_name']
        user_ = User.objects.get(user_name=user_string)
                
        try:
            cat_set = Category.objects.get(owningUser=user_, category_name=category_name)
            new_category = cat_set
            
        except Category.DoesNotExist:
            new_category = Category()
            new_category.category_name = category_name
            new_category.owningUser = user_   
            new_category.save()    
            
        fail_string = 'fail'
        try:
            entry_amt = float(request.POST['entry_amt'])
            curr_mon_tot = float(new_category.monthly_total)
            entry_note = request.POST['notes']
            fentry_amt = float(entry_amt)
            current_entry = Entry()            
            current_entry.amount = entry_amt
            current_entry.entry_note = entry_note
            new_category.monthly_total = entry_amt + curr_mon_tot
            new_category.save()
            current_entry.cat = cat_set
            current_entry.save()
            u_string = 'try works, made new entry with meaning'
        except:
            fail_string = 'fail, meaningless entry - ' + str(100)
        
        return render(request, self.template_name, {'form_one' : form_one, 'category_name' : category_name, 'user_name' : user_string, 'user_' : user_ , 'cat' : new_category, 'fail_notification' : fail_string})                    




    
class setupView(generic.ListView):
    template_name = 'fantasticApp/setup.html'
    model = Category
    def post(self, request):
        namer = request.POST['category_name']
        user_ =  User.objects.create(user_name='bill')
        overall_ = Overall.objects.create(grandTotal=1, montlyTotal=2)
        
        user = User.objects.create(user_name = namer)
        cat1 = Category(owningUser=user_, overallTotals=overall_,category_name=request.POST['category_name'], monthly_total=1, total_entries=1)
        cat1.save()
        
        return render(request, self.template_name, {'users_name' : namer})     
    
class newcatView(generic.TemplateView):
    template_name = 'fantasticApp/newcat.html'
    ##model = Category    
    
    def post(self, request, user_name):
        form_one = AddCatForm()
        cat_name = request.POST['category_name']
        user_=User.objects.get(user_name=user_name)
                
        new_category = Category()
        new_category.category_name = cat_name
        new_category.owningUser = user_   
        new_category.save()        
        return render(request, self.template_name, {'form_one' : form_one, 'new_cat' : cat_name, 'user_name' : user_name })  
        
    
    
    
# class getPostNameView(generic.DetailView):
    # template_name = 'fantasticApp/getname.html'
   # # context_object_name = 'some_name'
    
    # def post(self, request, nameer = 'Bill'):
        # if request.method == 'POST':
            # form = NameForm(request.POST)
            # if form.is_valid():
                # namer = nameer
            # else:
                # namer = nameer
                
        # return render(request, self.template_name, {'form': form, 'users_name' : namer})  
 
