from django.urls import path

from . import views

urlpatterns = [
    path("", views.loan_home,name="home"),
    path("loan_apply", views.loan_apply,name="loan_apply"),
    path("loan_status", views.loan_status,name="loan_status"),

    path("create_cloan", views.create_cloan.as_view(),name="create_cloan"),
    path("view_cloan", views.view_cloan.as_view(),name="view_cloan"),
    path("create_loan", views.create_loan.as_view(),name="create_loan"),
    path("view_loan", views.view_loan.as_view(),name="view_loan"),
    path("check_status", views.check_status.as_view(),name="check_status"),
    path("view_lstatus", views.view_lstatus.as_view(),name="view_lstatus"),

    path("delete_status", views.delete_status.as_view(),name="delete_status"),
    path("delete_loan", views.delete_loan.as_view(),name="delete_loan"),

    path("update_loan_details", views.update_loan_details.as_view(),name="update_loan_details"),
]