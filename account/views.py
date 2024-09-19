from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from account.models import account_view
from account.models import salary_view


def account(request):
    return render(request,'account/index.html')

def form(request):
    return render(request,'account/form.html')

def salary(request):
    return render(request,'account/salary.html')


class create_form(APIView):
    def post(self, request):
        username = request.POST['Username']
        acc = request.POST['account_number']
        ifsc = request.POST['ifsc']
        branch = request.POST['branch']
        
        usr = account_view()
        usr.username = username
        usr.acc = acc
        usr.ifsc = ifsc
        usr.branch = branch
        usr.save()
        # print(username)
        # print(email)
        # print(password)
        # print(utype)
        return JsonResponse({"status": "pass"})

from django.views.generic import TemplateView

class form_check(TemplateView):
    template_name = "bankingadmin/view_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = account_view.objects.all()
        context = {'userdata': user_data}
        return context
    



class salary_account(APIView):
    def post(self, request):
        acc = request.POST['account']
        branch_name= request.POST['branch_name']
        usr = salary_view()
        usr.acc = acc
        usr.branch = branch_name
        usr.save()
    # print(username)
    # print(email)
    # print(password)
    # print(utype)
        return JsonResponse({"status": "pass"})

from django.views.generic import TemplateView

class view_salary(TemplateView):
    template_name = "view_salary.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = salary_view.objects.all()
        context = { 'userdata': user_data}
        return context
    
class deleteuser(APIView):
    def post(self, request):
        name = request.POST['Username']
        account_view.objects.filter(username=name).delete()
        return JsonResponse({"status" : "pass"})
    
class deleteaccount(APIView):
    def post(self, request):
        name = request.POST['account']
        salary_view.objects.filter(acc=name).delete()
        return JsonResponse({"status" : "pass"})
    
class updateacc(APIView):
    def post(self, request):
        username = request.POST['Username']
        acc= request.POST['acc']
        ifsc = request.POST['ifsc']
        branch = request.POST['branch']

        account_view.objects.filter(acc=acc).update(username=username,ifsc=ifsc,branch=branch)
        return JsonResponse({"status" : "pass"})

