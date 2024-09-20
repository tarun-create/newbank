from django.shortcuts import render

from rest_framework.views import APIView
from django.http import JsonResponse
from django.views.generic.base import TemplateView

from customer.models import *
from django.views.generic.base import TemplateView


def bankingadmin(request):
    return render(request,"bankingadmin/index.html")

def createaccountadmin(request):
    return render(request,"bankingadmin/createaccountadmin.html")

def deleteaccountadmin(request):
    return render(request,"bankingadmin/deleteaccountadmin.html")

class updateaccountadmin(TemplateView):
    template_name = "updateaccountadmin.html"
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            user_data = Createaccount.objects.all()
            context = {'userdata':user_data}
            return context
    

class viewaccountadmin(TemplateView):
    template_name = "viewaccountadmin.html"
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            user_data = Createaccount.objects.all()
            context = {'userdata':user_data}
            return context
    





  
