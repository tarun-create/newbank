from django.urls import path
from . import views
urlpatterns = [
    path("",views.bankingadmin,name='bankingadmin'),
    path("createaccountadmin",views.createaccountadmin,name='createaccountadmin'),
    path("deleteaccountadmin",views.deleteaccountadmin,name='deleteaccountadmin'),
    path("updateaccountadmin",views.updateaccountadmin.as_view(),name='updateaccountadmin'),
    path("viewaccountadmin",views.viewaccountadmin.as_view(),name='viewaccountadmin'),

    
     path("accountcheck",views.accountcheck,name='accountcheck'),

    path("cardadm", views.cardadm,name="cardadm"),
    path("carddel/", views.carddel,name="carddel"),

    path("takeloan",views.takeloan,name='takeloan'),


    path("lifeinsurancecheck",views.lifeinsurancecheck,name='lifeinsurancecheck'),
    path("healthinsurancecheck",views.healthinsurancecheck,name='healthinsurancecheck'),
    path("vehicleinsurancecheck",views.vehicleinsurancecheck,name='vehicleinsurancecheck'),


]