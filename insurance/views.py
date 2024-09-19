from pydoc import doc
from django.http import JsonResponse
from django.shortcuts import render
from .models import HealthInsuranceApplication
from .models import LifeInsuranceApplication
from .models import VehicleInsuranceApplication
from insurance.models import VehicleInsuranceApplication
from rest_framework.views import APIView

def index(request):
    return render(request, 'insurance/index.html')

def vehicle_insurance(request):
    return render(request, 'insurance/vehicle-insurance.html')

def life_insurance(request):
    return render(request, 'insurance/life-insurance.html')

def health_insurance(request):
    return render(request, 'insurance/health-insurance.html')
from .models import HealthInsuranceApplication

class HealthInsuranceApplication_check(APIView): # type: ignore
    def post(self, request):
        full_name = request.POST['full-name']
        dob = request.POST['dob']
        medical_history=request.POST['medical-history']
        health_doc=request.POST['health-doc']
        
        usr = HealthInsuranceApplication()
        usr.full_name = full_name
        usr.dob = dob
        usr.medical_history=medical_history
        usr.health_doc=health_doc
        usr.save()
       
        return JsonResponse({"status": "pass"})

from django.views.generic import TemplateView

class HealthInsuranceApplication_view(TemplateView):
    template_name = "HealthInsuranceApplication_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = HealthInsuranceApplication.objects.all()
        context = {'userdata': user_data}
        return context


class LifeInsuranceApplication_check(APIView): # type: ignore
    def post(self, request):
        full_name = request.POST['full-name']
        dob = request.POST['dob']
        policy_amount=request.POST['policy_amount']
        identity_doc=request.POST['identity_doc']
        
        usr = LifeInsuranceApplication()
        usr.full_name = full_name
        usr.dob = dob
        usr.policy_amount = policy_amount
        usr.identity_doc=identity_doc
        usr.save()
       
        return JsonResponse({"status": "pass"})

from django.views.generic import TemplateView

class LifeInsuranceApplication_view(TemplateView):
    template_name = "LifeInsurenceApplication_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = LifeInsuranceApplication.objects.all()
        context = { 'userdata': user_data}
        return context






class VehicleInsuranceApplication_check(APIView): # type: ignore
    def post(self, request):
        vehicle_make = request.POST['vehicle-make']
        vehicle_model = request.POST['vehicle-model']
        registration_number=request.POST['registration-number']
        insurance_doc=request.POST['insurance-doc']
        
        usr = VehicleInsuranceApplication()
        usr.vehicle_make = vehicle_make
        usr.vehicle_model = vehicle_model
        usr.registration_number = registration_number
        usr.insurance_doc=insurance_doc
        usr.save()
       
        return JsonResponse({"status": "pass"})

from django.views.generic import TemplateView

class VehicleInsuranceApplication_view(TemplateView):
    template_name = "VehicleInsuranceApplication_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = VehicleInsuranceApplication.objects.all()
        context = { 'userdata': user_data}
        return context

class delete_vehicle(APIView):
    def post(self, request):
       username=request.POST['vehicle_make']
       VehicleInsuranceApplication.objects.filter(vehicle_make=username).delete()
       return JsonResponse({"status":"pass"})
class delete_life(APIView):
    def post(self, request):
       username=request.POST['full_name']
       LifeInsuranceApplication.objects.filter(full_name=username).delete()
       return JsonResponse({"status":"pass"})
class delete_health(APIView):
    def post(self, request):
       username=request.POST['full_name']
       HealthInsuranceApplication.objects.filter(full_name=username).delete()
       return JsonResponse({"status":"pass"})
    
class update_vehicle(APIView):
    def post(self, request):
        vehicle_make = request.POST['vehicle_make']
        vehicle_model = request.POST['vehicle_model']
        registration_number = request.POST['registration_number']
        insurance_doc = request.POST['insurance_doc']
        VehicleInsuranceApplication.objects.filter(vehicle_make = vehicle_make).update(vehicle_model=vehicle_model, registration_number=registration_number, insurance_doc=insurance_doc ) 


class update_life(APIView):
    def post(self, request):
        full_name = request.POST['fname']
        dob = request.POST['dob']
        policy_amount = request.POST['policy_amount']
        identity_doc = request.POST['identity_doc']
        LifeInsuranceApplication.objects.filter(full_name = full_name).update(dob=dob, policy_amount=policy_amount,identity_doc=identity_doc ) 
        return JsonResponse({"status": "pass"})
        
class update_health(APIView):
    def post(self, request):
        full_name = request.data.get('fname')
        dob = request.data.get('dob')
        medical_history = request.data.get('medical_history')
        health_doc = request.data.get('health_doc')

        updated_count = HealthInsuranceApplication.objects.filter(full_name=full_name).update(
            dob=dob,
            medical_history=medical_history,
            health_doc=health_doc
        )

        if updated_count > 0:
            return JsonResponse({"status": "success"})
        else:
            return JsonResponse({"status": "error", "message": "Record not found"})
