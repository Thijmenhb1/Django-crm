from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Register/Logout
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),

    # Client urls 
    path('client_list/', views.client_list, name='client_list'),
    path('client/<int:pk>', views.view_client, name='client'),
    path('add_client/', views.add_client, name='add_client'),
    path('update_client/<int:pk>', views.update_client, name='update_client'),
    path('delete_client/<int:pk>', views.delete_client, name='delete_client'),

    # Ticket urls
    path('ticket_list/', views.ticket_list, name='ticket_list'),
    path('ticket/<int:pk>', views.view_ticket, name='ticket'),
    path('add_ticket/', views.add_ticket, name='add_ticket'),
    path('update_ticket/<int:pk>', views.update_ticket, name='update_ticket'),
    path('delete_ticket/<int:pk>', views.delete_ticket, name='delete_ticket'),


]
