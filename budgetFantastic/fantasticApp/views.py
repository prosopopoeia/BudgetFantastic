from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import FormView

from .forms import NameForm

class indexView(generic.ListView):
    template_name = 'fantasticApp/index.html'
    context_object_name = 'users_name' 
        
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'users_name': 'New User'})
    
    # def get_queryset(self):
        # return render(request, 'indexUser.objects', users_name='ken')  
    
    # def get_name(request):
        # if request.method == 'POST':
            # form = NameForm(request.POST)
            # return HttpResponseRedirect('/fantasticApp/detail')
        # else:
            # form = NameForm()
        # return render(request, self.template_name, {'form', form})    
        
        
class otherView(generic.DetailView):
    template_name = 'fantasticApp/detail.html'
    context_object_name = 'box_contents'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'box_contents': args})

class setupView(generic.TemplateView):
    template_name = 'fantasticApp/setup.html'
        
    def post(self, request):
        namer = request.POST['item_text']
        return render(request, self.template_name, {'users_name' : namer})  
        
class getNameView(generic.DetailView):
    template_name = 'fantasticApp/getname.html'
   # context_object_name = 'some_name'
    
    def post(self, request):
        if request.method == 'POST':
            form = NameForm(request.POST)
            if form.is_valid():
                namer = form.cleaned_data['item_text']
            else:
                namer = request.POST['item_text']
        ##    return HttpResponseRedirect('/fantasticApp/detail')
        return render(request, self.template_name, {'form': form, 'users_name' : namer})  
    
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
            
