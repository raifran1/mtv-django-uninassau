from django.urls import path
from .views import index, concessionaria

urlpatterns = [
    path('', index, name='index'),
    path('concessionarias/', concessionaria, name='concessionaria')
]
