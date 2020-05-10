from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('foods/', views.FoodListView.as_view(), name='foods'),
    path('food/<str:pk>', views.FoodDetailView.as_view(), name='food-detail'),
    
]
urlpatterns += [  
    path('food/create/', views.FoodCreate.as_view(), name='food_create'),
    
]
urlpatterns += [  
    path('food/addtoday/', views.AddtoDiary, name='addtodiary'),
]
