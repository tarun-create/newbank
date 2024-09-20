from django.urls import path
from . import views
urlpatterns = [
    path("",views.bankingadmin,name='bankingadmin'),
    path("createaccountadmin",views.createaccountadmin,name='createaccountadmin'),
    path("deleteaccountadmin",views.deleteaccountadmin,name='deleteaccountadmin'),
    path("updateaccountadmin",views.updateaccountadmin.as_view(),name='updateaccountadmin'),
    path("viewaccountadmin",views.viewaccountadmin.as_view(),name='viewaccountadmin'),

    


]