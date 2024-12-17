from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),

    # Record urls 
    path('record_list/', views.record_list, name='record_list'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),


    # Ticket urls
    path('ticket_list/', views.ticket_list, name='ticket_list'),
    path('ticket/<int:pk>', views.customer_ticket, name='ticket'),
    path('add_ticket/', views.add_ticket, name='add_ticket'),
    path('update_ticket/<int:pk>', views.update_ticket, name='update_ticket'),
    path('delete_ticket/<int:pk>', views.delete_ticket, name='delete_ticket'),


]
