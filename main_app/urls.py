from django.urls import path
from . import views

urlpatterns = [
    path('transfer/', views.transfer_funds, name='transfer_funds'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('sign_in/', views.sign_in, name='sign_in'),
]
