from django.urls import path
from . import views

urlpatterns = [
	path('<int:id>', views.index, name='index'),
	path('', views.home, name='home'),
	path('create/', views.home, name='home'),
	path('<int:id>', views.index, name='index'),
	
]