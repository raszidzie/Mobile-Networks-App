from django.urls import path
from .views import *
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('', countries, name="countries"),
    path('<slug:slug>/', operators, name='operators' ),
    path('operator/<slug:slug>/', operator_detail, name='detail' ),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
