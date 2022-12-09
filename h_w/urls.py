from django.conf import settings
from django.urls import path
from . import views
from .views import H_W_Image_SendCreate
from django.conf.urls.static import static

app_name = 'h_w'
urlpatterns = [
    path('', views.h_w, name = 'h_w'),
    path('image/', H_W_Image_SendCreate.as_view()),
     path('image/',  views.h_w_i, name = 'h_w_i')
    
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
