from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import FormView
from fantasticApp.models import User, Category, Overall, Entry

from .forms import NameForm, AddCatForm

class indexView(generic.ListView):
    template_name = 'fantasticApp/index.html'
    context_object_name = 'users_name'        
    
    def get(self, request, *args, **kwargs):
        form_one = NameForm()
        return render(request, self.template_name, {'form_one': form_one})
     
        
class otherView(generic.DetailView):
    template_name = 'fantasticApp/detail.html'
    context_object_name = 'box_contents'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'box_contents': args})


        
class newcatView(generic.TemplateView):
    template_name = 'fantasticApp/newcat.html'
    model = Category    
    def post(self, request, user_name):
        form_one = AddCatForm()
        cat_name = request.POST['category_name']
        user_=User.objects.get(user_name=user_name)
        overall_ = Overall.objects.create(grandTotal=1, montlyTotal=2)
        new_category = Category()
        new_category.overallTotals = overall_ 
        new_category.owningUser = user_   
        new_category.save()        
        return render(request, self.template_name, {'form_one' : form_one, 'new_cat' : cat_name})  
        
class getNameView(generic.DetailView):
    template_name = 'fantasticApp/getname.html'
    context_object_name = 'user'
    
    def post(self, request):
        form_one = AddCatForm()
        namer = request.POST['users_name']        
        try:
            user=User.objects.get(user_name=namer)
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
            
