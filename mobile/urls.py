from django.urls import path
from .views import *
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('', countries, name="countries"),
    path('<int:id>/', operators, name='operators' ),
    path('operator/<int:id>/', operator_detail, name='detail' ),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
