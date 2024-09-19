from django.urls import path

from . import views

urlpatterns = [
    path("", views.card_manag,name="card_manag"),

    path("take_card",views.take_card.as_view(),name="take_card"),
    path("check_card",views.check_card.as_view(),name="check_card"),
    path("deleteuser",views.deleteuser.as_view(),name="deleteuser"),
    path("update_card_details", views.update_card_details.as_view(),name="update_card_details"),
]
