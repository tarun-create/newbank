from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('health-insurance/',views.health_insurance,name="health-insurance"),
    path('vehicle-insurance',views.vehicle_insurance,name="vehicle-insurance"),
    path('life-insurance/',views.life_insurance,name="life-insurance"),
    path('HealthInsuranceApplication_check', views.HealthInsuranceApplication_check.as_view(), name='HealthInsuranceApplication_check'),
    path('HealthInsuranceApplication_view', views.HealthInsuranceApplication_view.as_view(), name='HealthInsuranceApplication_view'),
    path('LifeInsuranceApplication_check', views.LifeInsuranceApplication_check.as_view(), name='LifeInsuranceApplication_check'),
    path('LifeInsuranceApplication_view', views.LifeInsuranceApplication_view.as_view(), name='LifeInsuranceApplication_view'),
    path('VehicleInsuranceApplication_check', views.VehicleInsuranceApplication_check.as_view(), name='VehicleInsuranceApplication_check'),
    path('VehicleInsuranceApplication_view', views.VehicleInsuranceApplication_view.as_view(), name='VehicleInsuranceApplication_view'),
    path('delete_vehicle', views.delete_vehicle.as_view(), name='delete_vehicle'),
    path('delete_life', views.delete_life.as_view(), name='delete_life'),
    path('delete_health', views.delete_health.as_view(), name='delete_health'), 
    path('update_vehicle', views.update_vehicle.as_view(),name='update_vehicle'),
    path('update_life', views.update_life.as_view(),name='update_life'),
    path('update_health', views.update_health.as_view(),name='update_health'),
]
