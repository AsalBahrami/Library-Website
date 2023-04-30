from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [

    path('books', views.return_data,name='books'),
    path('',views.homePage,name='home'),
    path('contact',views.contact,name='contact'),
    path('login',views.user_is_already_registered,name='login'),
    path('add',views.user_creates,name='add'),
    path('update/<str:pk>/',views.user_updates,name='update'),
    path('delete/<str:pk>/',views.user_deletes,name='delete'),
    path('loan/<str:pk>/',views.loan,name='loan'),
    path('zurueckgeben/<str:pk>/',views.return_book,name='zurueckgeben'),
    path('filter',views.data_filter,name='filter'),
    path('logout',views.user_logout,name='logout'),
    path('password',views.change_password,name='password'),



]
# handler500 = 'testApp.views.handler500'
# handler404 = 'testApp.views.handler404'
# handler403 = 'testApp.views.permission_denied_view'