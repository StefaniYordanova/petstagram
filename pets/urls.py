from django.urls import path, include
from pets import views

app_name = 'pets'

urlpatterns = [
    path('add/', views.add_pet, name="add"),
    path('<str:username>/pet/<slug:slug>/', include([
        path('', views.pet_details, name="details"),
        path('edit/', views.edit_pet, name="edit"),
        path('delete/', views.delete_pet, name="delete"),
    ]))
]