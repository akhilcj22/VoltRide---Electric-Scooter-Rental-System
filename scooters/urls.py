from django.urls import path
from . import views

urlpatterns = [
    # User views
    path('', views.ScooterListView.as_view(), name='scooter_list'),      # Class-based view
    path('start/<int:scooter_id>/', views.start_ride, name='start_ride'), 
    path('end/<int:ride_id>/', views.end_ride, name='end_ride'), 
    path('history/', views.RideHistoryView.as_view(), name='ride_history'),  # Class-based view

    # Admin dashboard and scooter management
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/scooters/', views.ScooterAdminListView.as_view(), name='scooter_admin_list'),
    path('admin/scooters/add/', views.ScooterCreateView.as_view(), name='scooter_add'),
    path('admin/scooters/edit/<int:pk>/', views.ScooterUpdateView.as_view(), name='scooter_edit'),
    path('admin/scooters/delete/<int:pk>/', views.ScooterDeleteView.as_view(), name='scooter_delete'),
]
