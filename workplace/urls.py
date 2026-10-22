# workplace\urls.py


from django.urls import path

from . import views

app_name = 'workplace'

urlpatterns = [
    path('', views.wp_list, name='wp_list'),
    path('<int:pk>/', views.wp_detail, name='wp_detail'),
]
