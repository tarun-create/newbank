from django.urls import path
from . import views
urlpatterns = [
    path("",views.account,name='account'),
    path("form",views.form,name='form'),
    path("salary",views.salary,name='salary'),  

    path("form_check", views.form_check.as_view(),name="form_check"),
    path("create_form", views.create_form.as_view(),name="create_form"),
    path("view_salary", views.view_salary.as_view(),name="view_salary"),
    path("salary_account", views.salary_account.as_view(),name="salary_account"),

    path("deleteuser", views.deleteuser.as_view(),name="deleteuser"),
    path("deleteaccount", views.deleteaccount.as_view(),name="deleteaccount"),

    path("updateacc", views.updateacc.as_view(),name="updateacc"),
     
]