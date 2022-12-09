
from django.shortcuts import render


from .models import H_W

def h_w_list(request):
    latest_articles_list = H_W.objects.order_by('-pub_date')[:200]
    return render(request, 'h_w_list/h_w_list.html',  {'latest_articles_list':latest_articles_list})





    
    







