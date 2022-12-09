from django.shortcuts import render
from .forms import H_W_Send_Form, H_W_Image_SendForm
from django.views.generic import CreateView
from .models import H_W_Image_Send
from django.views.generic import CreateView

def h_w(request):
    error = ''
    if request.method == 'POST':
        form = H_W_Send_Form(request.POST)
        if form.is_valid():
            form.save()
            
        else:
            error = 'Форма неверна!'

    
    
    form = H_W_Send_Form() 
    context = {
        'form': form
    }
    return render(request, 'h_w/h_w.html', context)


def h_w_i(request):
    pass


class H_W_Image_SendCreate(CreateView):
    
    model = H_W_Image_Send
    
    form_class = H_W_Image_SendForm
    
    extra_context = {'books': H_W_Image_Send.objects.all()}
    
    template_name = 'h_w/h_w_i.html'
    
    success_url = '/'




