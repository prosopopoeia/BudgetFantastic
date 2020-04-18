from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormView
from fantasticApp.models import User, Category, Overall, Entry
from .forms import NameForm, AddCatForm, NewEntryForm

class indexView(generic.ListView):
    template_name = 'fantasticApp/index.html'
    context_object_name = 'users_name'        
    
    def get(self, request, *args, **kwargs):
        form_one = NameForm()
        return render(request, self.template_name, {'form_one': form_one})
        
class newcatView(generic.TemplateView):
    template_name = 'fantasticApp/newcat.html'
    model = Category    
    def post(self, request, user_name):
        form_one = AddCatForm()
        cat_name = request.POST['category_name']
        user_=User.objects.get(user_name=user_name)
                
        new_category = Category()
        new_category.category_name = cat_name
        new_category.owningUser = user_   
        new_category.save()        
        return render(request, self.template_name, {'form_one' : form_one, 'new_cat' : cat_name, 'user_name' : user_name })  
        
        
class listcatView(generic.ListView):
    template_name = 'fantasticApp/catlist.html'
    model = Category    
    def post(self, request, user_name):
        form_one = AddCatForm()
        cat_name = request.POST['category_name']
        user_=User.objects.get(user_name=user_name)
                
        new_category = Category()
        new_category.category_name = cat_name
        new_category.owningUser = user_   
        new_category.save()    
        #cats =  User.objects.all()
        return render(request, self.template_name, {'form_one' : form_one, 'current_user' : user_, 'user_name' : user_name })        

class catdetailView(generic.DetailView):
    template_name = 'fantasticApp/catdetail.html'
    
    def post(self, request, category_name):
        form_one = NewEntryForm()
        user_string = request.GET['user_name']
        user_ = User.objects.all()
        cat_name = category_name
        current_category =  Category.objects.get(category_name = cat_name)
        
        try:
            current_entry = Entry.objects.get(ent_id)
        except:
            current_entry = Entry()
        try:
            current_entry.amount = request.POST['entry_amt']
            current_entry.entry_note = request.POST['notes']
            current_entry.cat = current_category
            current_entry.save()
        except :
            current_entry.cat = current_category
            current_entry.save()
        return render(request, self.template_name, {'form_one' : form_one, 'category_name' : cat_name, 'user_name' : user_string, 'user_' : user_ , 'cat' : current_category})                
        
class getNameView(generic.DetailView):
    template_name = 'fantasticApp/getname.html'
    context_object_name = 'user'
    
    def post(self, request):
        form_one = AddCatForm()
        namer = request.POST['users_name']        
        try:
            user=User.objects.get(user_name=namer)
            return HttpResponse("Hello, this is an existing user name %s" % user.id)
            #return HttpResponseRedirect(reverse('fantasticApp:listcat', namer))
        except User.DoesNotExist:
            user = User.objects.create(user_name = namer)
            
        return render(request, self.template_name, {'form_one': form_one, 'user' : user})      
    
    
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
    
    
    
    
class getPostNameView(generic.DetailView):
    template_name = 'fantasticApp/getname.html'
   # context_object_name = 'some_name'
    
    def post(self, request, nameer = 'Bill'):
        if request.method == 'POST':
            form = NameForm(request.POST)
            if form.is_valid():
                namer = nameer
            else:
                namer = nameer
                
        return render(request, self.template_name, {'form': form, 'users_name' : namer})  
            
