from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from card.models import card_db


def card_manag(request):
    return render(request,"card/card_management.html")

class deleteuser(APIView):
    def post(self, request):
        customer_id = request.POST['customer_id']
        card_db.objects.filter(customer_id = customer_id).delete()
        return JsonResponse({"status": "pass"})
    
class login_check(APIView):
    def post(self, request):
        username = request.POST['user']
        password = request.POST['password']
        if username == 'test':
            return JsonResponse({"status": "pass"})
        else:
            return JsonResponse({"status": "fail"})


class take_card(APIView):
    def post(self, request):
        card_id = request.POST['card_id']
        customer_id = request.POST['customer_id']
        card_type = request.POST['card_type']
        card_number = request.POST['card_number']
        expiry_date = request.POST['expiry_date']
        cvv = request.POST['cvv']
        status = request.POST['status']
        usr = card_db()
        usr.card_id = card_id
        usr.customer_id = customer_id
        usr.card_type = card_type
        usr.card_number = card_number
        usr.expiry_date = expiry_date
        usr.cvv = cvv
        usr.status = status
        usr.save()
        # print(card_id)
        # print(customer_id)
        return JsonResponse({"status": "pass"})

from django.views.generic import TemplateView

class check_card(TemplateView):
    template_name = "bankingadmin/viewcardadm.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = card_db.objects.all()
        context = { 'userdata': user_data}
        return context
    

class update_card_details(APIView):
    def post(self, request):
        card_id = request.POST['card_id']
        customer_id = request.POST['customer_id']
        card_type = request.POST['card_type']
        card_number = request.POST['card_number']
        expiry_date = request.POST['expiry_date']
        cvv = request.POST['cvv']
        status = request.POST['status']
        print("**************^^^^^^^^^")
        card_db.objects.filter(customer_id = customer_id).update(card_id=card_id, card_type=card_type, card_number=card_number, expiry_date=expiry_date, cvv=cvv, status=status) 
        return JsonResponse({"status": "pass"})




