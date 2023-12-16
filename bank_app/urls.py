from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('account_registration/', views.account_registration, name='account_registration'),
    path('get_branches/', views.get_branches, name='get_branches'),
    path('new_index',views.new_index,name='new_index'),
    path('after-reg/', views.after_reg, name='after_reg'),
]