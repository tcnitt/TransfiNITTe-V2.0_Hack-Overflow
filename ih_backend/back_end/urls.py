from django.urls import path
from back_end import views

urlpatterns = [
    path('snippets/', views.Vehicle_list),
]