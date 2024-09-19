from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from loan.models import loan_reg, loan_creg
from loan.models import loan_check


def loan_home(request):
    # return HttpResponse("Hello, world. You're at the loans index.")
    return render(request,"loan/loan_home.html")

def loan_apply(request):
    # return HttpResponse("Hello, world. You're at the loans index.")
    return render(request,"loan/loan_apply.html")

def loan_status(request):
    # return HttpResponse("Hello, world. You're at the loans index.")
    return render(request,"loan/loan_status.html")

class create_loan(APIView):
    def post(self, request):
        ids = request.POST['ids']
        type = request.POST['type']
        amount = request.POST['amount']
        ir = request.POST['ir']
        emi = request.POST['emi']
        start = request.POST['start']
        end = request.POST['end']
        status = request.POST['status']
        usr = loan_reg()
        usr.ids = ids
        usr.type = type
        usr.amount = amount
        usr.ir = ir
        usr.emi = emi
        usr.start = start
        usr.end = end
        usr.status = status
        usr.save()
        # print(username)
        # print(email)
        # print(password)
        # print(utype)
        return JsonResponse({"status": "pass"})

from django.views.generic import TemplateView

class view_loan(TemplateView):
    template_name = "bankingadmin/viewLoan.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = loan_reg.objects.all()
        context = { 'userdata': user_data}
        return context
    

class create_cloan(APIView):
    def post(self, request):
        ids = request.POST['ids']
        type = request.POST['type']
        amount = request.POST['amount']
        start = request.POST['start']
        end = request.POST['end']
        usr = loan_creg()
        usr.ids = ids
        usr.type = type
        usr.amount = amount
        usr.start = start
        usr.end = end
        usr.save()
        # print(username)
        # print(email)
        # print(password)
        # print(utype)
        return JsonResponse({"status": "pass"})
    
class view_cloan(TemplateView):
    template_name = "bankingadmin/viewCLoan.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = loan_creg.objects.all()
        context = { 'userdata': user_data}
        return context
    



class check_status(APIView):
    def post(self, request):
        id1 = request.POST['id1']
        accid = request.POST['acc1']
        cmob = request.POST['cmob']
        usr = loan_check()
        usr.id1 = id1
        usr.acc1 = accid
        usr.cmob = cmob
        usr.save()
        # print(username)
        # print(email)
        # print(password)
        # print(utype)
        return JsonResponse({"status": "pass"})

from django.views.generic import TemplateView

class view_lstatus(TemplateView):
    template_name = "bankingadmin/viewLoan.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = loan_check.objects.all()
        context = { 'userdata': user_data}
        return context
    


class delete_status(APIView):
    def post(self, request):
        id1 = request.POST['id1']
        loan_check.objects.filter(id1=id1).delete()
        return JsonResponse({"status": "pass"})
    


class delete_loan(APIView):
    def post(self, request):
        ids = request.POST['ids']
        loan_reg.objects.filter(ids=ids).delete()
        return JsonResponse({"status": "pass"})
    

class update_loan_details(APIView):
    def post(self, request):
        ids = request.POST['ids']
        type = request.POST['type']
        amount = request.POST['amount']
        ir = request.POST['ir']
        emi = request.POST['emi']
        start = request.POST['start']
        end = request.POST['end']
        status = request.POST['status']
        loan_reg.objects.filter(ids = ids).update(type=type, amount=amount, ir=ir, emi=emi, start=start, end=end, status=status) 
        return JsonResponse({"status": "pass"})
