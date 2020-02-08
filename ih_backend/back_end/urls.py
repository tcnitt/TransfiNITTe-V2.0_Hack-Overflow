from django.urls import path
from back_end import views
from django.conf.urls import include

urlpatterns = [
    path('snippets/', views.Vehicle_list.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('snippets/<int:pk>/', views.VehicleDetail.as_view()),
]

